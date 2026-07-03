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

    st.header("文書アップロード")

    uploaded_file = st.file_uploader(
        "ファイルを選択",
        type=["txt", "md", "pdf", "docx", "xlsx"],
    )

    if uploaded_file is not None:
        saved_path = file_service.save(
            filename=uploaded_file.name,
            data=uploaded_file.getvalue(),
        )
        document = document_service.read(saved_path)

        st.subheader("文書内容")

        st.text_area(
            label="",
            value=document,
            height=300,
            disabled=True,
        )

        st.subheader("AI解析")

        if st.button("要約する"):
            with st.spinner("AIが要約しています..."):
                try:
                    summary = ai_service.summarize(document)

                    st.success("要約が完了しました。")

                    st.text_area(
                        label="要約結果",
                        value=summary,
                        height=250,
                        disabled=True,
                    )

                except Exception as ex:
                    st.error(f"AI解析に失敗しました。\n{ex}")

        st.success(f"保存しました: {saved_path.name}")

    st.subheader("保存済みファイル")

    files = file_service.list_files()

    if not files:
        st.info("保存されているファイルはありません。")
    else:
        for file in files:
            st.write(f"📄 {file.name}")


if __name__ == "__main__":
    main()
