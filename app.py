import streamlit as st

from ai.tasks import AITask
from config import APP_NAME, APP_VERSION
from services.ai_service import AIService
from services.document_repository import DocumentRepository
from analysis.analysis_planner import AnalysisPlanner
from services.repository_analysis_service import RepositoryAnalysisService


def main() -> None:
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="📄",
        layout="wide",
    )

    st.title(APP_NAME)
    st.caption(f"Version {APP_VERSION}")

    repository = DocumentRepository()
    ai_service = AIService()

    #
    # AIチャット
    #
    st.header("AIチャット")

    question = st.text_input("質問")

    if st.button("送信") and question:

        answer = ai_service.ask(question)

        st.write(answer)

    st.divider()

    #
    # 文書管理
    #
    st.header("Document Repository")

    uploaded_file = st.file_uploader(
        "ファイルを選択",
        type=["txt", "md"],
    )

    if uploaded_file is not None:

        if st.button("アップロード"):

            repository.save(
                filename=uploaded_file.name,
                data=uploaded_file.getvalue(),
            )

            st.success("アップロードしました。")

            st.rerun()

    #
    # 検索
    #
    keyword = st.text_input("検索（ファイル名）")

    if keyword:

        documents = repository.search(keyword)

    else:

        documents = repository.list_documents()

    if not documents:

        st.info("保存済み文書はありません。")

        return

    file_names = [doc.name for doc in documents]

    selected_name = st.selectbox(
        "保存済み文書",
        file_names,
    )

    #
    # 文書情報
    #
    info = repository.get_info(selected_name)

    st.subheader("文書情報")

    st.write(f"**ファイル名** : {info.name}")
    st.write(f"**サイズ** : {info.size:,} Byte")
    st.write(
        f"**更新日時** : {info.updated_at.strftime('%Y/%m/%d %H:%M:%S')}"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("削除"):

            repository.delete(selected_name)

            st.success("削除しました。")

            st.rerun()

    #
    # 文書表示
    #
    document = repository.read(selected_name)

    st.subheader("文書内容")

    st.text_area(
        "文書",
        document,
        height=300,
        disabled=True,
    )

    #
    # AI解析
    #
    st.subheader("AI解析")

    task = st.selectbox(
        "解析内容",
        [
            AITask.SUMMARY,
            AITask.KEYWORD,
            AITask.TAG,
            AITask.CLASSIFY,
        ],
        format_func=lambda t: t.value,
    )

    if st.button("解析する"):

        with st.spinner("解析中..."):

            result = ai_service.analyze(
                document=document,
                task=task,
            )

        st.text_area(
            "解析結果",
            result,
            height=250,
            disabled=True,
        )

    planner = AnalysisPlanner()
    repository_analysis_service = RepositoryAnalysisService()

    st.divider()

    st.header("Repository Analysis")

    instruction = st.text_input(
        "分析指示",
        placeholder="例：2026年4月の請求金額を合計して",
    )

    if st.button("分析実行"):

        if instruction:

            plan = planner.create_plan(instruction)

            with st.spinner("分析中..."):

                result = repository_analysis_service.execute(
                    repository=repository,
                    plan=plan,
                )

            st.text_area(
                "分析結果",
                value=result,
                height=300,
                disabled=True,
            )



if __name__ == "__main__":
    main()
