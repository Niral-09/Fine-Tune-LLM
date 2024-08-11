from fastapi import APIRouter, HTTPException
from .schemas import QARequest
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

router = APIRouter()

model_name = "./fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

@router.post("/")
def get_answer(request: QARequest):
    try:
        result = qa_pipeline({
            'question': request.question,
        })
        return {"answer": result['answer'], "score": result['score']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
