from pydantic import BaseModel

class QARequest(BaseModel):
    command: str

class ConfigRequest(BaseModel):
    model_name: str