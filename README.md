# Fine Tuning LLM

## Overview

This project consists of a FastAPI backend for question answering and a Streamlit frontend to interact with the model.

## Backend

- **FastAPI**: API for handling question answering and model configuration.
- **Endpoints**:
  - `/qa/`: Post context and question to get an answer.
  - `/config/`: Post a model name to configure the model.

## Frontend

- **Streamlit**: Interactive web interface for question answering and model configuration.

## Setup

1. **Backend**:
   - Navigate to the `backend` directory.
   - Install dependencies: `pip install -r requirements.txt`.
   - Run the server: `uvicorn app.main:app --host 0.0.0.0 --port 8000`.

2. **Frontend**:
   - Navigate to the `frontend` directory.
   - Install dependencies: `pip install -r requirements.txt`.
   - Run the app: `streamlit run app.py`.

## Docker

- **Backend Dockerfile**: Containerizes the FastAPI backend.
- **Frontend Dockerfile**: Containerizes the Streamlit frontend.
