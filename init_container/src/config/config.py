from pydantic import BaseModel
import os


class Config(BaseModel):
    ollama_endpoint: str = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model_name: str = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")
    qdrant_endpoint: str = os.getenv("QDRANT_ENDPOINT", "localhost")
    qdrant_port: int = int(os.getenv("QDRANT_PORT", "6333"))
    qdrant_collection_name: str = os.getenv("QDRANT_COLLECTION", "hotmart")
    qdrant_vector_size: int = int(os.getenv("QDRANT_VECTOR_SIZE", "896"))
    default_ingest_files_path: str = os.getenv("DEFAULT_INGEST_FILES_PATH", "./")

