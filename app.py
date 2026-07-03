import streamlit as st

from config import APP_NAME, APP_VERSION
from services.ai_service import AIService
from services.document_repository import DocumentRepository
from ai.tasks import AITask


def main() -> None:
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="📄",
        layout="wide",
    )

    st.title(APP_NAME)
    st.caption(f"Version {APP_VERSION}")

    ai_service = AIService()

    repository = DocumentRepository()

    st.header("AIチャット")

    question = st.text_input("質問")

    if st.button("送信"):
        if question:
            answer = ai_service.ask(question)
            st.write(answer)

    st.divider()

    st.header("Document Repository")

    uploaded_file = st.file_uploader(
        "ファイルを選択",
        type=["txt", "md"],
    )

    if uploaded_file is not None:
        if st.button("アップロード"):
            saved_path = repository.save(
            filename=uploaded_file.name,
            data=uploaded_file.getvalue(),
        )

            st.success(f"{saved_path.name} を保存しました。")

    files = repository.list_documents()

    file_names = [file.name for file in files]

    selected_name = st.selectbox(
        "保存済み文書",
        file_names,
    )

    if st.button("削除"):
        repository.delete(selected_name)

        st.success("削除しました。")

        st.rerun()

    if selected_name:

        info = repository.get_info(selected_name)

        document = repository.read(selected_name)

        st.subheader("文書情報")

        st.write(f"**ファイル名** : {info.name}")
        st.write(f"**サイズ** : {info.size:,} Byte")
        st.write(
            f"**更新日時** : {info.updated_at.strftime('%Y/%m/%d %H:%M:%S')}"
        )
        st.subheader("文書内容")

        st.text_area(
            "",
            document,
            height=300,
            disabled=True,
        )

        st.subheader("AI解析")

        task = st.selectbox(
            "解析内容",
            (
                AITask.SUMMARY,
                AITask.KEYWORD,
                AITask.TAG,
                AITask.CLASSIFY,
            ),
            format_func=lambda task: {
                AITask.SUMMARY: "要約",
                AITask.KEYWORD: "キーワード（未実装）",
                AITask.TAG: "タグ生成（未実装）",
                AITask.CLASSIFY: "文書分類（未実装）",
            }[task],
        )

        if st.button("解析実行"):

            with st.spinner("解析中..."):

                if task == AITask.SUMMARY:
                    result = ai_service.analyze(
                        document=document,
                        task=task,
                    )
                else:
                    result = "この機能は次のPackageで実装予定です。"

            st.text_area(
                "解析結果",
                result,
                height=250,
                disabled=True,
            )

if __name__ == "__main__":
    main()
