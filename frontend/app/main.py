import os
import sys

import streamlit as st

# Get the frontend folder path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))   # frontend/app
FRONTEND_DIR = os.path.dirname(CURRENT_DIR)                # frontend

# Add frontend folder to Python path
if FRONTEND_DIR not in sys.path:
    sys.path.append(FRONTEND_DIR)

from components.file_uploader import render_file_uploader
from components.job_selector import render_job_selector
from components.score_card import render_score_card
from services.api_client import get_jobs, match_resume
from utils.constants import (
    APP_DESCRIPTION,
    APP_TITLE,
    NO_BACKEND_JOBS_MESSAGE,
    SELECT_JOB_WARNING_MESSAGE,
    SUCCESS_MESSAGE,
    UPLOAD_WARNING_MESSAGE,
)

st.set_page_config(page_title=APP_TITLE, page_icon="📄", layout="centered")

st.title(APP_TITLE)
st.write(APP_DESCRIPTION)

jobs = []

try:
    jobs = get_jobs().get("jobs", [])
except Exception as e:
    st.error(f"Could not load jobs from backend: {e}")

selected_job_title, job_options = render_job_selector(jobs)
uploaded_file = render_file_uploader()

if st.button("Match Resume"):
    if not jobs:
        st.warning(NO_BACKEND_JOBS_MESSAGE)
    elif uploaded_file is None:
        st.warning(UPLOAD_WARNING_MESSAGE)
    elif selected_job_title is None:
        st.warning(SELECT_JOB_WARNING_MESSAGE)
    else:
        selected_job_id = job_options[selected_job_title]

        try:
            with st.spinner("Matching resume..."):
                result = match_resume(selected_job_id, uploaded_file)

            st.success(SUCCESS_MESSAGE)
            render_score_card(result)

        except Exception as e:
            st.error(f"Error while matching resume: {e}")