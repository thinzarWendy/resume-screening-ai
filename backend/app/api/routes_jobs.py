from fastapi import APIRouter

from app.models.response_models import JobListResponse
from app.services.job_service import get_all_jobs

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.get("/", response_model=JobListResponse)
def get_jobs():
    jobs = get_all_jobs()
    return {"jobs": jobs}