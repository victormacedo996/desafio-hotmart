import os
from src.config import Config
from src.embedding.ollama.ollama_embedding import EmbeddingOllama
from src.vector_db.qdrant.qdrant import QdrantVectorDb
import requests


config = Config()
embedding_llm = EmbeddingOllama(config)
vector_db = QdrantVectorDb(config)


def create_vector_db_collections():
    vector_db.create_collection()

def ingest_default_data():
    default_files = [file for file in os.listdir(config.default_ingest_files_path) if file.startswith("default_")]
    for file in default_files:
        with open(f"{config.default_ingest_files_path}/{file}") as read:
            content = read.read()
        
        embedding = embedding_llm.create_embeddings(content)
        vector_db.upsert_vectors(content, embedding)


def setup_llm_model():
    request_body = {
        "name": config.ollama_model_name
    }
    response = requests.post(f"{config.ollama_endpoint}/api/pull", json=request_body)
    response.raise_for_status()
    

if __name__ == "__main__":
    setup_llm_model()
    create_vector_db_collections()
    ingest_default_data()
    