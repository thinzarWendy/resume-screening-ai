import streamlit as st

from utils.constants import SUPPORTED_FILE_TYPES


def render_file_uploader():
    uploaded_file = st.file_uploader(
        "Upload resume",
        type=SUPPORTED_FILE_TYPES
    )
    return uploaded_file