import abc
from typing import Dict, List


class BaseVectorDb(abc.ABC):
    
    @abc.abstractmethod
    def upsert_vectors(self, contents: str, vector: List[float] | List[List[float]] | Dict[str, List[float] | List[List[float]]]):
        raise NotImplementedError()


    @abc.abstractmethod
    def create_collection(self):
        raise NotImplementedError()