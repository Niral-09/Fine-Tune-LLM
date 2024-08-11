from pydantic import BaseModel

class QARequest(BaseModel):
    context: str
    question: str

class ConfigRequest(BaseModel):
    model_name: str