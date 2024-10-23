from pydantic import BaseModel

class UploadFileResponse(BaseModel):
    detail: str
