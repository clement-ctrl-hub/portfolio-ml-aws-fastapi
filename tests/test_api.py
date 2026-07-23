from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient

import app.main as main_module


fake_model = MagicMock()
fake_model.predict.return_value = [2.5]


def test_home():
    with patch.object(
        main_module,
        "load_model",
        return_value=fake_model,
    ):
        with TestClient(main_module.app) as client:
            response = client.get("/")

    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_predict():
    payload = {
        "MedInc": 8.3,
        "HouseAge": 41,
        "AveRooms": 6.9,
        "AveBedrms": 1.0,
        "Population": 322,
        "AveOccup": 2.5,
        "Latitude": 37.88,
        "Longitude": -122.23,
    }

    with patch.object(
        main_module,
        "load_model",
        return_value=fake_model,
    ):
        with TestClient(main_module.app) as client:
            response = client.post(
                "/predict",
                json=payload,
            )

    assert response.status_code == 200
    assert response.json()["prediction"] == 2.5