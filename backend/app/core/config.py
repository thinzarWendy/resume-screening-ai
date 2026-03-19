from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = BASE_DIR / "uploads" / "resumes"

JOBS_FILE = DATA_DIR / "sample_jobs.json"

ALLOWED_EXTENSIONS = {".pdf", ".docx"}

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

API_TITLE = "Resume Screening AI API"
API_DESCRIPTION = "Backend API for Resume Screening AI project"
API_VERSION = "1.0.0"