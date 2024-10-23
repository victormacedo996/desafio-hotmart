import abc
from typing import Sequence


class BaseEmbedding(abc.ABC):
    @abc.abstractmethod
    def create_embeddings(self, sentence: str) -> Sequence[float]:
        raise NotImplementedError()