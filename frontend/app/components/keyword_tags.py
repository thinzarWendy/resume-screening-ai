import streamlit as st

from utils.formatter import format_keywords


def render_keyword_tags(matched_keywords):
    st.subheader("Matched Keywords")
    st.write(format_keywords(matched_keywords))