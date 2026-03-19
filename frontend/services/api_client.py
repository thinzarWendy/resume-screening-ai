import requests

from utils.constants import API_BASE_URL


def get_jobs():
    response = requests.get(f"{API_BASE_URL}/jobs/", timeout=10)
    response.raise_for_status()
    return response.json()


def match_resume(job_id: int, uploaded_file):
    files = {
        "resume_file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type,
        )
    }
    data = {
        "job_id": job_id
    }

    response = requests.post(
        f"{API_BASE_URL}/match/",
        files=files,
        data=data,
        timeout=60
    )
    response.raise_for_status()
    return response.json()