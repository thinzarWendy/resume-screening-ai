from pathlib import Path
from typing import Dict, List

from sentence_transformers import SentenceTransformer, util

from app.core.config import BASE_DIR, EMBEDDING_MODEL_NAME
from app.ml.prepare_training_data import prepare_training_data


FINE_TUNED_MODEL_DIR = BASE_DIR / "trained_models" / "fine_tuned"


def load_base_model():
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def load_fine_tuned_model():
    if FINE_TUNED_MODEL_DIR.exists() and any(FINE_TUNED_MODEL_DIR.iterdir()):
        return SentenceTransformer(str(FINE_TUNED_MODEL_DIR))
    return None


def compare_models() -> List[Dict]:
    _, val_examples = prepare_training_data()

    base_model = load_base_model()
    fine_tuned_model = load_fine_tuned_model()

    results = []

    for idx, example in enumerate(val_examples, start=1):
        resume_text = example.texts[0]
        job_description = example.texts[1]
        true_score = float(example.label)

        base_resume_emb = base_model.encode(resume_text, convert_to_tensor=True)
        base_job_emb = base_model.encode(job_description, convert_to_tensor=True)
        base_score = util.cos_sim(base_resume_emb, base_job_emb).item()

        fine_tuned_score = None
        if fine_tuned_model is not None:
            ft_resume_emb = fine_tuned_model.encode(resume_text, convert_to_tensor=True)
            ft_job_emb = fine_tuned_model.encode(job_description, convert_to_tensor=True)
            fine_tuned_score = util.cos_sim(ft_resume_emb, ft_job_emb).item()

        results.append(
            {
                "pair_index": idx,
                "true_score": round(true_score, 4),
                "base_model_score": round(base_score, 4),
                "fine_tuned_model_score": round(fine_tuned_score, 4) if fine_tuned_score is not None else None,
                "base_abs_error": round(abs(true_score - base_score), 4),
                "fine_tuned_abs_error": round(abs(true_score - fine_tuned_score), 4) if fine_tuned_score is not None else None,
            }
        )

    return results


def summarize_comparison(results: List[Dict]) -> Dict:
    if not results:
        return {
            "total_pairs": 0,
            "base_model_mae": 0.0,
            "fine_tuned_model_mae": None,
        }

    base_mae = sum(item["base_abs_error"] for item in results) / len(results)

    fine_tuned_errors = [
        item["fine_tuned_abs_error"]
        for item in results
        if item["fine_tuned_abs_error"] is not None
    ]

    fine_tuned_mae = None
    if fine_tuned_errors:
        fine_tuned_mae = sum(fine_tuned_errors) / len(fine_tuned_errors)

    return {
        "total_pairs": len(results),
        "base_model_mae": round(base_mae, 4),
        "fine_tuned_model_mae": round(fine_tuned_mae, 4) if fine_tuned_mae is not None else None,
    }


if __name__ == "__main__":
    comparison_results = compare_models()
    summary = summarize_comparison(comparison_results)

    print("Model Comparison Results:")
    for item in comparison_results:
        print(item)

    print("\nSummary:")
    print(summary)