from pydantic import BaseModel

class InferenceRequest(BaseModel):
    question: str