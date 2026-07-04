import cohere
from app.core.config import settings

co = cohere.AsyncClient(settings.cohere_api_key)
response = await co.embed(texts=[text], model=settings.embedding_model, input_type=input_type, embedding_types=["float"])
print(type(response.embeddings))
print(response.embeddings)
"""
async def embed_text(text: str, input_type: str = "search_query") -> list[float]:
    response = await co.embed(texts=[text], model=settings.embedding_model, input_type=input_type, embedding_types=["float"])
    return response.embeddings.float[0]

    """"""
async def embed_batch(texts: list[str], input_type: str = "search_document") -> list[list[float]]:
    response = await co.embed(texts=texts, model=settings.embedding_model, input_type=input_type, embedding_types=["float"])
    return response.embeddings.float[0]
"""