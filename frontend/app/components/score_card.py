import streamlit as st

from components.keyword_tags import render_keyword_tags
from utils.formatter import format_match_score


def render_score_card(result: dict):
    st.subheader("Match Result")

    st.write(f"**Job Title:** {result['job']['title']}")
    st.write(f"**Filename:** {result['filename']}")
    st.write(f"**Match Score:** {format_match_score(result['match_score'])}")

    matched_keywords = result.get("matched_keywords", [])
    render_keyword_tags(matched_keywords)

    st.subheader("Resume Text Preview")
    st.text(result.get("resume_text_preview", "No preview available."))