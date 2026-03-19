from pathlib import Path

from sentence_transformers import SentenceTransformer

from app.core.config import BASE_DIR, EMBEDDING_MODEL_NAME

FINE_TUNED_MODEL_DIR = BASE_DIR / "trained_models" / "fine_tuned"

_model = None


def get_model_path() -> str:
    if FINE_TUNED_MODEL_DIR.exists() and any(FINE_TUNED_MODEL_DIR.iterdir()):
        return str(FINE_TUNED_MODEL_DIR)
    return EMBEDDING_MODEL_NAME


def load_embedding_model():
    global _model

    if _model is None:
        model_path = get_model_path()
        _model = SentenceTransformer(model_path)

    return _model


def generate_embedding(text: str):
    model = load_embedding_model()
    return model.encode(text)


def reset_embedding_model():
    global _model
    _model = None