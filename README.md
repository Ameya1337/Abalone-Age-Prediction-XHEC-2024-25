

<div align="center">

# Abalone Age Prediction with FastAPI & Docker

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Linting: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-informational?logo=pre-commit&logoColor=white)](https://github.com/artefactory/xhec-mlops-project-student/blob/main/.pre-commit-config.yaml)
</div>

This project focuses on industrializing the [Abalone age prediction](https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset) using FastAPI, Docker, and Prefect for API deployment. The age of abalone is predicted based on physical measurements.

## Table of Contents

- [Project Overview](#project-overview)
- [Deliverables](#deliverables)
- [Setup Instructions](#setup-instructions)
  - [Installation Requirements](#installation-requirements)
  - [Setting up the Environment](#setting-up-the-environment)
  - [Using Docker](#using-docker)
  - [API Usage](#api-usage)
- [Model Training](#model-training)
- [MLflow Integration](#mlflow-integration)
- [Project Structure](#project-structure)

---

## Project Overview

This repository is dedicated to the industrialization of the Abalone age prediction task, leveraging machine learning models to predict the number of rings on abalone shells based on easier-to-measure physical attributes. The API is deployed in a Docker container, where users can send a set of abalone attributes and receive a predicted age as a response.

## Deliverables

This project delivers:

1. **Machine Learning Model**: A model to predict the age of abalones based on physical characteristics.
2. **Prefect Flow**: Used for training and re-training the model.
3. **FastAPI-based API**: An API for serving predictions, deployed in a Docker container, allowing users to send requests with abalone data and receive predictions.


## Setup Instructions

### Installation Requirements

Before you proceed, make sure your environment meets the following prerequisites:

- Python 3.12
- Docker

### Setting Up the Environment

Follow these steps to set up the environment:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Abalone-Age-Prediction-XHEC-2024-25.git
   cd Abalone-Age-Prediction-XHEC-2024-25
   ```

2. **Create a Virtual Environment**:
   - Using `venv`:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

   - Using `conda`:
     ```bash
     conda env create --file=environment.yml
     conda activate abalone
     ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Pre-commit Hooks**:
    ```bash
    pip install pre-commit
    pre-commit install
    ```

### Set up a Regular Training Pipeline Using Prefect

1. **Start the Prefect Server**
   - Run the following command to start the Prefect server:
     ```bash
     prefect server start
     ```

2. **Deploy the Training Flow**
   - Use the following command to deploy the training flow:
     ```
     prefect src/modelling/main.py
     ```

3. **Configure and Verify the Schedule**
   - Visit [Prefect Dashboard](http://localhost:4000/).
   - Navigate to the "Deployments" section.
   - On the right side of the screen, toggle the 'Schedule' on.
   - Verify just below that the training is set to rerun everyday at midnight.



### Using Docker

To run the API inside a Docker container:

1. **Build the Docker Image**:
   ```bash
   docker build -t abalone_age_predictor .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -p 4201:4201 -p 8001:8001 abalone_age_predictor
   ```

**Note**: Ports `4201` and `8001` are exposed for Prefect and Uvicorn, respectively. You can change the image name to a more descriptive one if desired.

### API Usage

Once the Docker container is up and running, you can access the API documentation and test the `/predict` endpoint at:

- **URL**: `http://0.0.0.0:8001/docs`

**Sample request body** for the `/predict` endpoint:

```json
{
  "Sex": "M",
  "Length": 0.45,
  "Diameter": 0.35,
  "Height": 0.15,
  "Whole_weight": 0.8,
  "Shucked_weight": 0.4,
  "Viscera_weight": 0.2,
  "Shell_weight": 0.25
}
```

This will return the predicted age of the abalone based on the input features.

## Project Structure

The project is organized as follows:

```bash
├── app/                      # Contains API and application code
│   ├── main.py               # Main FastAPI application
│   ├── models/               # ML models and related files
├── bin/
│   └── run_services.sh        # Script to run Prefect and Uvicorn services
├── data/                     # Folder containing abalone.csv dataset from Kaggle
├── docker/                   # Docker-related files
├── mlruns/                   # MLflow tracking experiments folder (auto-generated)
├── prefect_flows/            # Prefect workflows for model training
├── requirements.txt          # Dependencies for the project
├── requirements.in           # Base dependencies list
└── README.md                 # This file
```

## Tips for Contributors

- Use a virtual environment like `conda` or `venv` to install dependencies.
- Follow the code style using `pre-commit` to enforce linting and formatting.
- Make sure to regularly update `requirements.txt` from `requirements.in` using `pip-compile`.

Before making any changes:

1. Create a new branch:
   ```bash
   git checkout -b feature/new-feature
   ```

2. Test your code, ensure it works as expected, and update this `README.md` if needed.
