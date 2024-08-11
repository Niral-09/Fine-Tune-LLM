from pydantic import BaseModel

class QARequest(BaseModel):
    question: str

class ConfigRequest(BaseModel):
    model_name: str