from src.vector_db.base_vector import BaseVectorDb
from src.config import Config
from typing import Dict, List
from qdrant_client import QdrantClient, models
import uuid


class QdrantVectorDb(BaseVectorDb):
    def __init__(self, config: Config) -> None:
        self.qdrant_client = QdrantClient(host=config.qdrant_endpoint, port=config.qdrant_port)
        self.config = config


    def upsert_vectors(self, contents: str, vector: List[float] | List[List[float]] | Dict[str, List[float] | List[List[float]]]):
    
        self.qdrant_client.upsert(
            collection_name=self.config.qdrant_collection_name,
            points=[
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    payload={
                        "pergunta": contents.partition('\n')[0],
                        "conteudo": contents.partition('\n')[2]
                    },
                    vector=vector
                )
            ]
        )