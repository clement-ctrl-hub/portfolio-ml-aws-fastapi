from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Charger le modèle
from pathlib import Path

MODEL_PATH = Path("app/model.joblib")

model = None

if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)

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
    return {"message": "ML API is running 🚀"}

from fastapi import FastAPI, HTTPException

@app.post("/predict")
def predict(data: Features):
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not available"
        )

    df = pd.DataFrame([data.model_dump()])
    prediction = model.predict(df)

    return {"prediction": float(prediction[0])}