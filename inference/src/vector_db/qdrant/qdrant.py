from src.vector_db.base_vector import BaseVectorDb
from src.config import Config
from typing import Sequence, Tuple, List
from qdrant_client import QdrantClient


class QdrantVectorDb(BaseVectorDb):
    def __init__(self, config: Config) -> None:
        self.qdrant_client = QdrantClient(host=config.qdrant_endpoint, port=config.qdrant_port)
        self.config = config


    def search_vectors(self, query_vector: Sequence[float] | Tuple[str, List[float]]) -> List[str]:
        search_result = self.qdrant_client.search(
            collection_name=self.config.qdrant_collection_name,
            query_vector=query_vector,
            limit=2
        )

        context_str = [result.payload["conteudo"] for result in search_result]
        context_str = "\n".join(context_str)
        return context_str