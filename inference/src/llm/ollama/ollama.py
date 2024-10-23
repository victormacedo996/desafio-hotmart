from src.llm.base_llm import BaseLLM
from src.config import Config
from llama_index.llms.ollama import Ollama
from src.decorators.singleton import singleton


@singleton
class OllamaLLM(BaseLLM):

    def __init__(self, config: Config) -> None:
        self.llm = Ollama(model=config.ollama_model_name, base_url=config.ollama_endpoint)


    def answer(self, prompt: str) -> str:
        return self.llm.complete(prompt=prompt).text
