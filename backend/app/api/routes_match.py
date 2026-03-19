from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.core.config import UPLOAD_DIR
from app.models.response_models import MatchResponse
from app.services.embedding_service import generate_embedding
from app.services.job_service import get_job_by_id
from app.services.keyword_service import extract_matched_keywords
from app.services.parser_service import extract_text_from_resume, save_uploaded_resume
from app.services.similarity_service import (
    calculate_similarity_score,
    convert_score_to_percentage,
)
from app.utils.helper import generate_text_preview
from app.utils.text_cleaner import clean_text
from app.utils.validators import validate_job_exists, validate_resume_filename

router = APIRouter(prefix="/match", tags=["Match"])


@router.post("/", response_model=MatchResponse)
async def match_resume(
    job_id: int = Form(...),
    resume_file: UploadFile = File(...)
):
    if not validate_resume_filename(resume_file.filename):
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    if not validate_job_exists(job_id):
        raise HTTPException(
            status_code=404,
            detail="Job not found."
        )

    job = get_job_by_id(job_id)
    saved_file_path = save_uploaded_resume(resume_file, UPLOAD_DIR)

    resume_text = clean_text(extract_text_from_resume(saved_file_path))
    if not resume_text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the uploaded resume."
        )

    job_description = clean_text(job.get("description", ""))
    if not job_description:
        raise HTTPException(
            status_code=400,
            detail="Selected job description is empty."
        )

    resume_embedding = generate_embedding(resume_text)
    job_embedding = generate_embedding(job_description)

    similarity_score = calculate_similarity_score(resume_embedding, job_embedding)
    match_score = convert_score_to_percentage(similarity_score)

    matched_keywords = extract_matched_keywords(resume_text, job_description)
    resume_text_preview = generate_text_preview(resume_text)

    return {
        "message": "Resume matched successfully",
        "job": {
            "id": job["id"],
            "title": job["title"]
        },
        "filename": resume_file.filename,
        "saved_to": str(saved_file_path),
        "resume_text_preview": resume_text_preview,
        "match_score": match_score,
        "matched_keywords": matched_keywords
    }