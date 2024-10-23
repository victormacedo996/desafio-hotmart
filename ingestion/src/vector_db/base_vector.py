import abc
from typing import List, Dict


class BaseVectorDb(abc.ABC):
    
    @abc.abstractmethod
    def upsert_vectors(self, contents: str, vector: List[float] | List[List[float]] | Dict[str, List[float] | List[List[float]]]):
        raise NotImplementedError()