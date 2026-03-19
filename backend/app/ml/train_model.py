from pathlib import Path

from sentence_transformers import SentenceTransformer, losses
from torch.utils.data import DataLoader

from app.core.config import BASE_DIR, EMBEDDING_MODEL_NAME
from app.ml.prepare_training_data import prepare_training_data


TRAINED_MODEL_DIR = BASE_DIR / "trained_models" / "fine_tuned"


def train_model(
    output_dir: Path = TRAINED_MODEL_DIR,
    batch_size: int = 8,
    num_epochs: int = 3
):
    train_examples, val_examples = prepare_training_data()

    model = SentenceTransformer(EMBEDDING_MODEL_NAME)

    train_dataloader = DataLoader(
        train_examples,
        shuffle=True,
        batch_size=batch_size
    )

    train_loss = losses.CosineSimilarityLoss(model)

    output_dir.mkdir(parents=True, exist_ok=True)

    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=num_epochs,
        warmup_steps=0,
        output_path=str(output_dir)
    )

    return {
        "message": "Training completed successfully",
        "train_samples": len(train_examples),
        "validation_samples": len(val_examples),
        "model_saved_to": str(output_dir)
    }


if __name__ == "__main__":
    result = train_model()
    print(result)