

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
2. **FastAPI-based API**: An API for serving predictions, deployed in a Docker container, allowing users to send requests with abalone data and receive predictions.
3. **Prefect Flow**: Used for training and re-training the model.
4. **MLflow**: Placeholder section for model tracking and experiment management (details to be added).

## Setup Instructions

### Installation Requirements

Before you proceed, make sure your environment meets the following prerequisites:

- Python 3.12
- Docker
- `requirements.txt` is updated and ready to use.

To ensure the installation is smooth:

1. **Use a Virtual Environment**:
   - We recommend `venv` or `conda` to manage dependencies.
2. **Pre-commit Hooks**:
   - Install pre-commit hooks to ensure code formatting.

Run the following commands:
- [xhec-mlops-project-student](#xhec-mlops-project-student)
  - [Table of Contents](#table-of-contents)
  - [Deliverables and Evaluation](#deliverables-and-evaluation)
    - [Deliverables](#deliverables)
    - [Evaluation](#evaluation)
  - [Steps to reproduce to build the deliverable](#steps-to-reproduce-to-build-the-deliverable)
    - [Pull requests in this project](#pull-requests-in-this-project)
    - [Tips to work on this project](#tips-to-work-on-this-project)

## Deliverables and notation

### Deliverables

The deliverable of this project is a copy of this repository with the industrialization of the Abalone age prediction model. We expect to see:

1. a workflow to train a model using Prefect
- The workflows to train the model and to make the inference (prediction of the age of abalone) are in separate modules and use Prefect `flow` and `task` objects
- The code to get the trained model and encoder is in a separate module and must be reproducible (not necessarily in a docker container)
2. a Prefect deployment to retrain the model regularly
3. an API that runs on a local app and that allows users to make predictions on new data
  - A working API which can be used to make predictions on new data
    - The API can run on a docker container
    - The API has validation on input data (use Pydantic)

### Evaluation

Each of your pull requests will be graded based on the following criteria:

- **Clarity** and quality of code
  - good module structure
  - naming conventions
  - use of docstrings and type hinting
- **Formatting**
  - respect of clear code conventions

  *P.S. you can use a linter and automatic code formatters to help you with that*

- Proper **Functioning** of the code
  - the code must run without bugs

Bseides the evaluation of the pull requests, we will also evaluate:
- **Reproducibility** and clarity of instructions to run the code (we will actually try to run your code)
  - Having a clear README.md with
    - the context of the project
    - the name of the participants and their github users
    - the steps to recreate the Python environment
    - the instructions to run all parts of the code
- Use of *Pull Requests* (see below) to coordinate your collaboration

## Steps to reproduce to build the deliverable

To help you with the structure and order of steps to perform in this project, we created different pull requests templates.
Each branch in this repository corresponds to a future pull request and has an attached markdown file with the instructions to perform the tasks of the pull request.
Each branch starts with a number.
You can follow the order of the branches to build your project and collaborate.

> [!NOTE]
> There are "TODO" in the code of the different branches. Each "TODO" corresponds to a task to perform to build the project.
> [!IMPORTANT]
> Remember to remove all code that is not used before the end of the project (including all TODO tags in the code).

**Please follow these steps**:

- If not done already, create a GitHub account
- If not done already, create a [Kaggle account](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F) (so you can download the dataset)
- Fork this repository (one person per group)

**WARNING**: make sure to **unselect** the option "Copy the `master` branch only", so you have all the branches in the forked repository.

- Add the different members of your group as admin to your forked repository
- Follow the order of the numbered branches and for each branch:
  - Read the PR_i.md (where i is the number of the branch) file to understand the task to perform
   > [!NOTE]
   > Dont forget to integrate your work from past branches (except for when working on branch #1 obviously (!))
   > ```bash
   > git checkout branch_number_i
   > git pull origin master
   > # At this point, you might have a VIM window opening, you can close it using the command ":wq"
   > git push
   > ```
    - Read and **follow** all the instructions in the the PR instructions file
    - Do as many commits as necessary on the branch_number_i to perform the task indicated in the corresponding markdown file
    - Open **A SINGLE** pull request from this branch to the main branch of your forked repository
    - Once done, merge the pull request in the main branch of your forked repository

### Pull requests in this project

Github [Pull Requests](https://docs.github.com/articles/about-pull-requests) are a way to propose changes to a repository. They have for purpose to integrate the work of *feature branches* into the main branch of the repository, with a collaborative review process.

**PR tips:**

Make sure that you select your own repository when selecting the base repository:

![PR Wrong](assets/PR_wrong.png)

It should rather look like this:

![PR Right](assets/PR_right.png)

### Tips to work on this project

- Use a virtual environment to install the dependencies of the project (conda or virtualenv for instance)

- Once your virtual environment is activated, install pre-commit hooks to automatically format your code before each commit:

```bash
pip install pre-commit
pre-commit install
```

3. **Maintain `requirements.txt` and `requirements.in`**:
   - Use `pip-compile` to maintain `requirements.txt` from `requirements.in`.

```bash
pip-compile requirements.in
```

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

## Model Training

*(Content to be added)*

This section will describe how to train the model, including the commands and steps to train it inside or outside the Docker container.

## MLflow Integration

*(Content to be added)*

This section will describe the integration with MLflow for tracking experiments and visualizing model performance metrics.

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
