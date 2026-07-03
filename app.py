import streamlit as st

from config import APP_NAME, APP_VERSION
from services.ai_service import AIService
from services.file_service import FileService
from services.document_service import DocumentService


def main() -> None:
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="📄",
        layout="wide",
    )

    st.title(APP_NAME)
    st.caption(f"Version {APP_VERSION}")

    ai_service = AIService()
    file_service = FileService()
    document_service = DocumentService()

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
            saved_path = file_service.save(
                filename=uploaded_file.name,
                data=uploaded_file.getvalue(),
            )

            st.success(f"{saved_path.name} を保存しました。")

    files = file_service.list_files()

    file_names = [file.name for file in files]

    selected_name = st.selectbox(
        "保存済み文書",
        file_names,
    )

    if selected_name:

        path = file_service.get(selected_name)

        document = document_service.read(path)

        st.subheader("文書内容")

        st.text_area(
            "",
            document,
            height=300,
            disabled=True,
        )

    st.subheader("AI解析")

    if st.button("要約する"):

        with st.spinner("要約中..."):

            summary = ai_service.summarize(document)

        st.text_area(
            "要約結果",
            summary,
            height=250,
            disabled=True,
        )

if __name__ == "__main__":
    main()
