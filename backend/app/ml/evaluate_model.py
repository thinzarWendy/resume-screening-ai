from pathlib import Path
from typing import List, Dict

from sentence_transformers import SentenceTransformer, util

from app.core.config import BASE_DIR, EMBEDDING_MODEL_NAME
from app.ml.prepare_training_data import prepare_training_data


TRAINED_MODEL_DIR = BASE_DIR / "trained_models" / "fine_tuned"


def load_model(model_path: Path = TRAINED_MODEL_DIR):
    if model_path.exists() and any(model_path.iterdir()):
        return SentenceTransformer(str(model_path))
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


def evaluate_model(model_path: Path = TRAINED_MODEL_DIR) -> List[Dict]:
    _, val_examples = prepare_training_data()
    model = load_model(model_path)

    results = []

    for idx, example in enumerate(val_examples, start=1):
        resume_text = example.texts[0]
        job_description = example.texts[1]
        true_score = float(example.label)

        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        job_embedding = model.encode(job_description, convert_to_tensor=True)

        predicted_score = util.cos_sim(resume_embedding, job_embedding).item()

        results.append(
            {
                "pair_index": idx,
                "true_score": round(true_score, 4),
                "predicted_score": round(predicted_score, 4),
                "absolute_error": round(abs(true_score - predicted_score), 4),
            }
        )

    return results


def summarize_evaluation(results: List[Dict]) -> Dict:
    if not results:
        return {
            "total_pairs": 0,
            "mean_absolute_error": 0.0,
        }

    mae = sum(item["absolute_error"] for item in results) / len(results)

    return {
        "total_pairs": len(results),
        "mean_absolute_error": round(mae, 4),
    }


if __name__ == "__main__":
    evaluation_results = evaluate_model()
    summary = summarize_evaluation(evaluation_results)

    print("Evaluation Results:")
    for item in evaluation_results:
        print(item)

    print("\nSummary:")
    print(summary)