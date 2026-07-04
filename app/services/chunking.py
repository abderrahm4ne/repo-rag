"""
naive file chunking
"""

import tiktoken
from app.core.config import settings

encoding = tiktoken.get_encoding("cl100k_base")

def chunk_text(content: str) -> list[str]:
    tokens = encoding.encode(content)
    if not tokens:
        return []
    
    chunks = []
    step = settings.chunk_size_tokens - settings.chunk_overlap_tokens
    for i in range(0, len(tokens), step):
        chunk_tokens = tokens[i:i + settings.chunk_size_tokens]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)
        if i + settings.chunk_size_tokens >= len(tokens):
            break

    return chunks