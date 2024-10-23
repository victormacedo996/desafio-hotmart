from pydantic import BaseModel
import os
from src.decorators.singleton import singleton

@singleton
class Config(BaseModel):
    ollama_endpoint: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model_name: str = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")
    qdrant_endpoint: str = os.getenv("QDRANT_ENDPOINT", "localhost")
    qdrant_port: int = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_collection_name: str = os.getenv("QDRANT_COLLECTION", "hotmart")
