from app.services.job_service import get_job_by_id
from app.services.parser_service import is_allowed_file


def validate_resume_filename(filename: str) -> bool:
    if not filename:
        return False
    return is_allowed_file(filename)


def validate_job_exists(job_id: int) -> bool:
    job = get_job_by_id(job_id)
    return job is not None