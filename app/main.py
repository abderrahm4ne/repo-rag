from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup task
    print("Initializing database...")
    yield 

app = FastAPI(title="repo-rag", version="0.1.0", lifespan=lifespan)

app.get("/health")
async def health_check():
    return {"status": "ok"}