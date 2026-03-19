from typing import List, Optional

from pydantic import BaseModel


class JobItem(BaseModel):
    id: int
    title: str
    description: str


class JobListResponse(BaseModel):
    jobs: List[JobItem]


class MatchJobResponse(BaseModel):
    id: int
    title: str


class MatchResponse(BaseModel):
    message: str
    job: MatchJobResponse
    filename: str
    saved_to: str
    resume_text_preview: str
    match_score: Optional[float]
    matched_keywords: List[str]