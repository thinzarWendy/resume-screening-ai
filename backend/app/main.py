from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_jobs import router as jobs_router
from app.api.routes_match import router as match_router
from app.core.config import API_DESCRIPTION, API_TITLE, API_VERSION

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobs_router)
app.include_router(match_router)


@app.get("/")
def root():
    return {
        "message": "Resume Screening AI API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "resume-screening-backend"
    }