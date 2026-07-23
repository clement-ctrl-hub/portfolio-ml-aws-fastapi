from contextlib import asynccontextmanager

import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.model_loader import load_model


model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Charge le modèle une seule fois au démarrage de l'API.
    """

    global model

    try:
        model = load_model()
        print("Modèle chargé avec succès.")
    except Exception as error:
        model = None
        print(f"Erreur lors du chargement du modèle : {error}")

    yield

    model = None


app = FastAPI(
    title="Portfolio ML API",
    lifespan=lifespan,
)


class Features(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {
        "message": "ML API is running 🚀",
        "model_loaded": model is not None,
    }


@app.get("/health")
def health():
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not available",
        )

    return {
        "status": "healthy",
        "model_loaded": True,
    }


@app.post("/predict")
def predict(data: Features):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not available",
        )

    dataframe = pd.DataFrame(
        [data.model_dump()]
    )

    prediction = model.predict(dataframe)

    return {
        "prediction": float(prediction[0])
    }