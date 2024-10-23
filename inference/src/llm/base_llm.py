import abc


class BaseLLM(abc.ABC):
    @abc.abstractmethod
    def answer(self, prompt: str) -> str:
        raise NotImplementedError()