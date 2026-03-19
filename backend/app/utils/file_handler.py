from pathlib import Path


def ensure_directory(directory_path: Path):
    directory_path.mkdir(parents=True, exist_ok=True)


def get_safe_file_path(upload_dir: Path, filename: str) -> Path:
    return upload_dir / filename