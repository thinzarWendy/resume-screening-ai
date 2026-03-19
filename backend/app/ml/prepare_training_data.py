import csv
from pathlib import Path
from typing import List, Tuple

from sentence_transformers import InputExample
from sklearn.model_selection import train_test_split

from app.core.config import DATA_DIR


LABELED_PAIRS_FILE = DATA_DIR / "labeled_pairs.csv"


def load_labeled_pairs(file_path: Path = LABELED_PAIRS_FILE) -> List[dict]:
    if not file_path.exists():
        raise FileNotFoundError(f"Labeled pairs file not found: {file_path}")

    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return rows


def convert_to_input_examples(rows: List[dict]) -> List[InputExample]:
    examples = []

    for row in rows:
        resume_text = row["resume_text"].strip()
        job_description = row["job_description"].strip()
        normalized_score = float(row["normalized_score"])

        example = InputExample(
            texts=[resume_text, job_description],
            label=normalized_score
        )
        examples.append(example)

    return examples


def split_training_data(
    examples: List[InputExample],
    test_size: float = 0.2,
    random_state: int = 42
) -> Tuple[List[InputExample], List[InputExample]]:
    train_examples, val_examples = train_test_split(
        examples,
        test_size=test_size,
        random_state=random_state,
        shuffle=True
    )
    return train_examples, val_examples


def prepare_training_data():
    rows = load_labeled_pairs()
    examples = convert_to_input_examples(rows)
    train_examples, val_examples = split_training_data(examples)

    return train_examples, val_examples