import streamlit as st

from utils.constants import NO_JOBS_MESSAGE


def render_job_selector(jobs):
    if not jobs:
        st.warning(NO_JOBS_MESSAGE)
        return None, {}

    job_options = {job["title"]: job["id"] for job in jobs}

    selected_job_title = st.selectbox(
        "Select a job position",
        options=list(job_options.keys())
    )

    return selected_job_title, job_options