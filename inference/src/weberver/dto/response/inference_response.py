from pydantic import BaseModel

class InferenceResponse(BaseModel):
    response: str
