import numpy as np
import scipy
from prefect import task
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error


@task
def train_model(X: scipy.sparse.csr_matrix, y: np.ndarray) -> LinearRegression:
    """
    Train a linear regression model on the given training data.

    Args:
        X (scipy.sparse.csr_matrix): The feature matrix in sparse format.
        y (np.ndarray): The target values corresponding to the features.

    Returns:
        LinearRegression: The trained linear regression model.
    """
    lr = LinearRegression()
    lr.fit(X, y)
    return lr


def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Evaluate the performance of the model by calculating the RMSE.

    Args:
        y_true (np.ndarray): The true target values.
        y_pred (np.ndarray): The predicted target values from the model.

    Returns:
        float: The calculated RMSE value, indicating the model's prediction error.
    """
    return np.sqrt(root_mean_squared_error(y_true, y_pred))
