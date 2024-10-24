from fastapi import FastAPI

from src.web_service.app_config import (
    APP_DESCRIPTION,
    APP_TITLE,
    APP_VERSION,
    PATH_TO_MODEL,
    PATH_TO_PREPROCESSOR,
)
from src.web_service.lib.inference import run_inference
from src.web_service.lib.models import InputData, PredictionOut

# Other imports
from src.web_service.utils import load_model, load_preprocessor

# Initialize the FastAPI application
app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.get("/")
def home() -> dict:
    """
    Health check endpoint.

    Returns:
    -------
    dict
        A simple health check response indicating that the app is up and running.
    """
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData) -> dict:
    """
    Endpoint to run predictions on input data.

    Parameters:
    ----------
    payload : InputData
        The input data for prediction in the specified format.

    Returns:
    -------
    dict
        A dictionary containing the predicted age.
    """
    # Load the preprocessor and model
    dv = load_preprocessor(PATH_TO_PREPROCESSOR)
    model = load_model(PATH_TO_MODEL)

    # Run inference
    y = run_inference([payload], dv, model)

    # Return the prediction result
    return {"age_prediction": y[0]}
