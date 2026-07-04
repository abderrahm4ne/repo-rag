import uuid
from pydantic import BaseModel

class IngestRequest(BaseModel):
    repo_url: str

class IngestResponse(BaseModel):
    repo_id: uuid.UUID
    files_ingested: int
    chunks_created: int

class QueryRequest(BaseModel):
    repo_id: uuid.UUID
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    cached: bool