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


## Prerequisites

- Python 3.x installed on your machine.
- `pip` (Python package installer) available.
- `virtualenv` for creating a virtual Python environment.
- `make`  for managing the build and execution process.

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-repo/project-name.git
cd project-name
```

### 2. Create and Activate the Python Environment

Create a virtual environment in the project directory:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
```bash
.\venv\Scripts\activate
```

- On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Start Project

You can start both the backend and frontend by running the following command:

```bash
make up
```

-----

# Sentiment Analysis Model Documentation

This document provides an overview of the sentiment analysis model created in the notebook `fine-tuned-model.ipynb`. The model has been fine-tuned and saved locally in a folder named `fine-tuned-model`.

## Model Creation

### Notebook: `FineTuning.ipynb`
The entire process of creating and fine-tuning the sentiment analysis model is documented in the Jupyter notebook `FineTuning.ipynb`. The notebook includes the following steps:

1. **Dataset Loading**: The IMDb dataset was loaded using the `datasets` library.
2. **Tokenization**: The text data was tokenized using the `AutoTokenizer` from Hugging Face's Transformers library.
3. **Model Selection**: A pre-trained model (`distilbert-base-uncased`) was chosen and loaded using the `AutoModelForSequenceClassification` class.
4. **Fine-Tuning**: The model was fine-tuned on the IMDb dataset to classify movie reviews as positive or negative.

### Local Model Storage

After fine-tuning, the model was saved locally in the `fine-tuned-model` folder. This folder contains all the necessary files for loading and using the model, including the tokenizer and the model's configuration.

## Using the Model

### Inference with Local Model

The model can be loaded from the `fine-tuned-model` folder and used for sentiment analysis on new text data. Below is a brief guide on how to load and use the model:

1. **Loading the Model**:
    ```python
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    model_name = "fine-tuned-model"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    ```

2. **Performing Sentiment Analysis**:
    ```python
    def predict_sentiment(review_text):
    inputs = tokenizer(review_text, padding=True, truncation=True, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predictions = torch.softmax(logits, dim=-1)

    predicted_label = torch.argmax(predictions, dim=-1).item()
    sentiment = "Positive" if predicted_label == 1 else "Negative"

   return sentiment, predictions[0].cpu().numpy()
    ```

This will return the sentiment of the input text, classifying it as either positive or negative.

## Conclusion

The `FineTuning.ipynb` notebook serves as the complete guide for creating and fine-tuning the sentiment analysis model. By leveraging the DistilBERT model, the notebook demonstrates how to efficiently train a robust sentiment analysis model and use it for inference. The resulting model is stored locally and can be loaded for further use in various applications.
