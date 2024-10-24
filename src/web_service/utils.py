import os
import pickle
from functools import lru_cache

from loguru import logger


@lru_cache
def load_preprocessor(filepath: os.PathLike):
    """
    Load the preprocessor from a specified file.

    Parameters:
    ----------
    filepath : os.PathLike
        The path to the preprocessor file.

    Returns:
    -------
    object
        The loaded preprocessor object.
    """
    logger.info(f"Loading preprocessor from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)


@lru_cache
def load_model(filepath: os.PathLike):
    """
    Load a model from a specified file.

    Parameters:
    ----------
    filepath : os.PathLike
        The path to the model file.

    Returns:
    -------
    object
        The loaded model object.
    """
    logger.info(f"Loading model from {filepath}")
    with open(filepath, "rb") as f:
        return pickle.load(f)
