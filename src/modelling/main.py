import os
from pathlib import Path

import pandas as pd
from prefect import flow, serve
from preprocessing import process_data
from training import train_model
from utils import save_pickle


@flow(name="Train model")
def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle)."""
    # Read data
    csv_path = Path(trainset_path).resolve()
    df = pd.read_csv(csv_path)

    # Preprocess data (task)
    x, y, dv = process_data(df).result()

    base_path = Path(__file__).resolve().parent.parent.parent

    # Train model (task)
    model = train_model(x, y).result()

    # Save model and dv (tasks)
    model_path = os.path.join(base_path, "src/web_service/local_objects/model.pkl")
    dv_path = os.path.join(base_path, "src/web_service/local_objects/dv.pkl")

    save_pickle(model_path, model)
    save_pickle(dv_path, dv)


if __name__ == "__main__":
    # Set the Prefect API URL
    os.environ["PREFECT_API_URL"] = "http://127.0.0.1:4200/api"

    deployment = main.to_deployment(
        name="train-model",
        version="0.1",
        cron="0 0 * * *",
    )
    serve(deployment)
