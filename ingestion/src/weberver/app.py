from fastapi import FastAPI
from src.config import Config
from src.vector_db.qdrant.qdrant import QdrantVectorDb
from src.embedding.ollama.ollama_embedding import EmbeddingOllama
from fastapi import FastAPI, UploadFile, HTTPException, status
import pathlib
from src.weberver.dto.response.inference_response import UploadFileResponse


app = FastAPI()
config = Config()
vector_db = QdrantVectorDb(config)
embedding = EmbeddingOllama(config)



@app.get("/health")
async def health() -> str:
    return "ingestion"


@app.post("/uploadfile", status_code=status.HTTP_201_CREATED)
async def create_upload_file(file: UploadFile) -> UploadFileResponse:
    contents = await file.read()
    contents = contents.decode("utf-8")
    if file.content_type != "text/plain":
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="content must be text/plain")
    
    file_extension = pathlib.Path(file.filename).suffix

    if file_extension != ".txt":
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="file must be a .txt")

    query_embedding = embedding.create_embeddings(contents)
    vector_db.upsert_vectors(contents, query_embedding)
    await file.close()
    return UploadFileResponse(detail="ingestion successful")

def get_app() -> FastAPI:
    return app
