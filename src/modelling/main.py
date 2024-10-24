import argparse
from pathlib import Path

import pandas as pd
from preprocessing import process_data
from training import train_model
from utils import save_pickle


def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    csv_path = Path("../../data/abalone.csv")
    df = pd.read_csv(csv_path)
    # Preprocess data
    x, y, dv = process_data(df)
    # (Optional) Pickle encoder if need be

    # Train model
    model = train_model(x, y)

    # Save model
    save_pickle(
        Path("../web_service/local_objects/model.pkl"),
        model,
    )
    save_pickle(
        Path("../web_service/local_objects/dv.pkl"),
        dv,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train a model using the data at the given path."
    )
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(args.trainset_path)
