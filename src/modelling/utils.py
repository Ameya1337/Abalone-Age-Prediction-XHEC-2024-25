import pickle
from pathlib import Path
from typing import Any


def load_pickle(path: Path) -> Any:
    """
    Load a Python object from a pickle file.

    Args:
        path (Path): The file path to the pickle file.

    Returns:
        Any: The Python object that was stored in the pickle file.
    """
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


def save_pickle(path: Path, obj: Any) -> None:
    """
    Save a Python object to a pickle file.

    Args:
        path (Path): The file path to save the pickle file.
        obj (Any): The Python object to be saved.

    Returns:
        None
    """
    with open(path, "wb") as f:
        pickle.dump(obj, f)
