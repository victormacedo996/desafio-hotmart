from src.embedding.base_embedding import BaseEmbedding
from src.config import Config
from typing import Sequence
from llama_index.embeddings.ollama import OllamaEmbedding
from src.decorators.singleton import singleton


@singleton
class EmbeddingOllama(BaseEmbedding):
    def __init__(self, config: Config) -> None:
        self.ollama_embedding = OllamaEmbedding(model_name=config.ollama_model_name,base_url=config.ollama_endpoint, ollama_additional_kwargs={"mirostat": 0})

    def create_embeddings(self, sentence: str) -> Sequence[float]:
        return self.ollama_embedding.get_query_embedding(sentence)
