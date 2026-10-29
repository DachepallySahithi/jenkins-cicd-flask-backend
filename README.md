

\# Flask Backend - Jenkins CI/CD



\## Overview

A Flask REST API backend with automated tests and a Jenkins pipeline.



\## Features

\- Flask REST API

\- Health check endpoint

\- Greeting endpoint

\- Automated unit tests

\- Jenkins CI/CD pipeline



\## Technology Stack

\- Python

\- Flask

\- unittest

\- Jenkins

\- Git and GitHub



\## API Endpoints

| Method | Endpoint | Description |

|---|---|---|

| GET | `/` | Welcome message |

| GET | `/health` | Health check |

| GET | `/api/greet/<name>` | Greeting response |



\## Run Locally

Create and activate a virtual environment:



```bash

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

python app.py

```



\## Run Tests

```bash

python -m unittest -v

```



\## CI/CD

The `Jenkinsfile` defines the pipeline for installing dependencies, running tests, and performing deployment steps.



\## Repository

https://github.com/DachepallySahithi/jenkins-cicd-flask-backend



