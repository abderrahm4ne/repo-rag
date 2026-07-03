from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # optional while .env not provided
    github_token: Optional[str] = None
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    database_url: Optional[str] = None
    redis_url: Optional[str] = None
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536
    chunk_size_tokens: int = 500
    chunk_overlap_tokens: int = 50
    top_k_retrieval: int = 5

    class Config:
        env_file = ".env"

settings = Settings()
