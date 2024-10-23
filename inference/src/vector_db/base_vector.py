import abc
from typing import Sequence, Tuple, List


class BaseVectorDb(abc.ABC):
    
    @abc.abstractmethod
    def search_vectors(self, query_vector: Sequence[float] | Tuple[str, List[float]]) -> List[str]:
        raise NotImplementedError()