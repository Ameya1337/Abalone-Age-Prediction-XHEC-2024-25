from typing import List

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.base import BaseEstimator
from sklearn.feature_extraction import DictVectorizer

from src.web_service.app_config import CATEGORICAL_VARS
from src.web_service.lib.models import InputData


def encode_categorical_cols(
    df: pd.DataFrame, categorical_cols: List[str] = None
) -> pd.DataFrame:
    """
    Encode categorical columns in the DataFrame.

    Parameters:
    ----------
    df : pd.DataFrame
        The DataFrame containing the data to be encoded.
    categorical_cols : List[str], optional
        The list of categorical columns to encode. If None,
        defaults to CATEGORICAL_VARS.

    Returns:
    -------
    pd.DataFrame
        The DataFrame with categorical columns encoded as strings,
        filling missing values with -1.
    """
    if categorical_cols is None:
        categorical_cols = CATEGORICAL_VARS

    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("str")
    return df


def run_inference(
    input_data: List[InputData], dv: DictVectorizer, model: BaseEstimator
) -> np.ndarray:
    """
    Run inference on the provided input data using the given vectorizer and model.

    Parameters:
    ----------
    input_data : List[InputData]
        A list of InputData objects containing the input features.
    dv : DictVectorizer
        The vectorizer used to transform input data into the model's expected format.
    model : BaseEstimator
        The trained model used for making predictions.

    Returns:
    -------
    np.ndarray
        The predicted ages in rings for the input data.
    """
    logger.info(f"Running inference on:\n{input_data}")

    # Convert input data to DataFrame
    df = pd.DataFrame([x.dict() for x in input_data])

    # Encode categorical columns
    df = encode_categorical_cols(df)

    # Transform DataFrame into a format suitable for the model
    dicts = df[CATEGORICAL_VARS].to_dict(orient="records")
    X = dv.transform(dicts)

    # Run the model prediction
    y = model.predict(X)

    logger.info(f"Predicted age in rings:\n{y}")
    return y
