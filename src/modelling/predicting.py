from pathlib import Path

import numpy as np
import scipy
from utils import load_pickle


def predict(X: scipy.sparse.csr_matrix, path_to_model: Path) -> np.ndarray:
    """
    Use a trained linear regression model to make predictions on the given feature data.

    Args:
        X (scipy.sparse.csr_matrix): The feature matrix in sparse format.
        model (LinearRegression): The trained linear regression model.

    Returns:
        np.ndarray: The predicted target values.
    """
    try:
        model = load_pickle(path_to_model)  # Save (pickle) the object
    except ValueError as e:
        raise (e)
    return model.predict(X)
