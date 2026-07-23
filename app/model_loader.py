import os
from pathlib import Path

import boto3
import joblib


BUCKET_NAME = os.getenv(
    "MODEL_S3_BUCKET",
    "clement-portfolio-ml-models",
)

MODEL_KEY = os.getenv(
    "MODEL_S3_KEY",
    "models/model.joblib",
)

MODEL_PATH = Path(
    os.getenv(
        "MODEL_LOCAL_PATH",
        "/tmp/model.joblib",
    )
)


def download_model_if_needed() -> Path:
    """
    Télécharge le modèle depuis S3 s'il n'existe pas déjà localement.
    """

    if MODEL_PATH.exists():
        print(f"Modèle déjà présent : {MODEL_PATH}")
        return MODEL_PATH

    MODEL_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(
        f"Téléchargement du modèle depuis "
        f"s3://{BUCKET_NAME}/{MODEL_KEY}"
    )

    s3_client = boto3.client(
        "s3",
        region_name="eu-west-3",
    )

    s3_client.download_file(
        BUCKET_NAME,
        MODEL_KEY,
        str(MODEL_PATH),
    )

    print(f"Modèle téléchargé dans {MODEL_PATH}")

    return MODEL_PATH


def load_model():
    """
    Télécharge puis charge le modèle ML.
    """

    model_path = download_model_if_needed()
    return joblib.load(model_path)