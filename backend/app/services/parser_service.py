from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from fastapi import UploadFile

from app.core.config import ALLOWED_EXTENSIONS
from app.utils.file_handler import ensure_directory, get_safe_file_path


def save_uploaded_resume(upload_file: UploadFile, upload_dir: Path) -> Path:
    ensure_directory(upload_dir)

    file_path = get_safe_file_path(upload_dir, upload_file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())

    return file_path


def get_file_extension(filename: str) -> str:
    return Path(filename).suffix.lower()


def is_allowed_file(filename: str) -> bool:
    return get_file_extension(filename) in ALLOWED_EXTENSIONS


def extract_text_from_pdf(file_path: Path) -> str:
    text_parts = []

    with fitz.open(file_path) as pdf:
        for page in pdf:
            text_parts.append(page.get_text())

    return "\n".join(text_parts).strip()


def extract_text_from_docx(file_path: Path) -> str:
    doc = Document(file_path)
    text_parts = [paragraph.text for paragraph in doc.paragraphs]
    return "\n".join(text_parts).strip()


def extract_text_from_resume(file_path: Path) -> str:
    extension = get_file_extension(file_path.name)

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)
    if extension == ".docx":
        return extract_text_from_docx(file_path)

    raise ValueError("Unsupported file format")