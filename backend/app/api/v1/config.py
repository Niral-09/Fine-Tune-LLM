from fastapi import APIRouter, HTTPException
from .schemas import ConfigRequest
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

router = APIRouter()

model_name = "./fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

@router.post("/")
def configure_model(config: ConfigRequest):
    global model, tokenizer, qa_pipeline
    try:
        model = AutoModelForQuestionAnswering.from_pretrained(config.model_name)
        tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
        return {"message": f"Model loaded successfully: {config.model_name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
