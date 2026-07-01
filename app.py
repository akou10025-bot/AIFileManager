import streamlit as st

from config import APP_NAME
from config import APP_VERSION

from services.ai_service import AIService

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📄",
    layout="wide"
)

st.title(APP_NAME)

st.caption(f"Version {APP_VERSION}")

st.divider()

st.success("Sprint1 Package2")

service = AIService()

if st.button("AI接続テスト"):

    answer = service.ask("こんにちは")

    st.success(answer)
