import json

from app.core.config import JOBS_FILE


def load_jobs():
    if not JOBS_FILE.exists():
        return []

    with open(JOBS_FILE, "r", encoding="utf-8") as file:
        jobs = json.load(file)

    return jobs


def get_all_jobs():
    return load_jobs()


def get_job_by_id(job_id: int):
    jobs = load_jobs()

    for job in jobs:
        if job.get("id") == job_id:
            return job

    return None