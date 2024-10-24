from typing import List, Tuple

import numpy as np
import pandas as pd
import scipy
from sklearn.feature_extraction import DictVectorizer
from prefect import task

CATEGORICAL_COLS = ["Sex"]


def filter_outliers(
    df: pd.DataFrame, min_rings: int = 1, max_rings: int = 20
) -> pd.DataFrame:
    """
    Remove rows corresponding to negative/zero
    and too high target' values from the dataset
    """
    return df[df["Rings"].between(min_rings, max_rings)]


def encode_categorical_cols(
    df: pd.DataFrame, categorical_cols: List[str] = None
) -> pd.DataFrame:
    """Encode categorical columns as strings"""
    if categorical_cols is None:
        categorical_cols = CATEGORICAL_COLS
    df.loc[:, categorical_cols] = df[categorical_cols].fillna(-1).astype("str")
    df.loc[:, categorical_cols] = df[categorical_cols].astype("str")
    return df


def extract_x_y(
    df: pd.DataFrame,
    categorical_cols: List[str] = None,
    dv: DictVectorizer = None,
    with_target: bool = True,
) -> Tuple[scipy.sparse.csr_matrix, np.ndarray, DictVectorizer]:
    """Extract X and y from the dataframe"""
    if categorical_cols is None:
        categorical_cols = CATEGORICAL_COLS
    dicts = df[categorical_cols].to_dict(orient="records")

    y = None
    if with_target:
        if dv is None:
            dv = DictVectorizer()
            dv.fit(dicts)
        y = df["Rings"].values

    x = dv.transform(dicts)
    return x, y, dv

@task
def process_data(
    df: pd.DataFrame, dv=None, with_target: bool = True
) -> scipy.sparse.csr_matrix:
    """
    Load data from a parquet file
    Compute target (duration column) and apply threshold filters (optional)
    Turn features to sparse matrix
    :return The sparce matrix, the target' values and the
    dictvectorizer object if needed.
    """
    if with_target:
        df2 = filter_outliers(df)

        df3 = encode_categorical_cols(df2)

        return extract_x_y(df3, dv=dv)
    else:

        df2 = encode_categorical_cols(df)

        return extract_x_y(df2, dv=dv, with_target=with_target)
