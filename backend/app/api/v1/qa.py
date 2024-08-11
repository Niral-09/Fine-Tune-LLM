from fastapi import APIRouter, HTTPException
from .schemas import QARequest
from transformers import AutoModelForSequenceClassification
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from app.models import predict_sentiment

router = APIRouter()

model_name = "fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_safetensors=True)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

@router.post("/")
def get_answer(request: QARequest):
    try:
        sentiment, probs = predict_sentiment(request.command)
        probs = [float(prob) for prob in probs]
        print({"review": request.command, "sentiment": sentiment, "probs": probs})
        return {"review": request.command, "sentiment": sentiment, "probs": probs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
