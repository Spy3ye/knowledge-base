

def chunk_text(text: str, max_chunk_size: int = 1000, overlap: int = 100) -> list[str]:
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = min(start + max_chunk_size , length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap

    return chunks
