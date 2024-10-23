from fastapi import FastAPI
from src.weberver.dto.request.inference_request import InferenceRequest
from src.weberver.dto.response.inference_response import InferenceResponse
from src.config import Config
from src.vector_db.qdrant.qdrant import QdrantVectorDb
from src.embedding.ollama.ollama_embedding import EmbeddingOllama
from src.llm.ollama.ollama import OllamaLLM


app = FastAPI()
config = Config()
vector_db = QdrantVectorDb(config)
embedding = EmbeddingOllama(config)
llm = OllamaLLM(config)


@app.get("/health")
async def health() -> str:
    return "inference"



@app.post("/inference")
async def inference(inference_request: InferenceRequest) -> InferenceResponse:

    query_embedding = embedding.create_embeddings(inference_request.question)

    context_str = vector_db.search_vectors(query_embedding)

    prompt = f"""
    A partir do contexto abaixo
    ---------------------
    {context_str}
    ---------------------
    Dada a informação acima, por favor, resposta a pergunta: {inference_request.question}
    """
    response = llm.answer(prompt=prompt)
    
    return InferenceResponse(response=response)

def get_app() -> FastAPI:
    return app