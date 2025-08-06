from app.db.qdrant import qdrant_client
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance,
    Filter,
    FieldCondition,
    MatchValue
)
from qdrant_client import QdrantClient
from app.utils.embedding import get_embedding

# qdrant = QdrantClient(host="localhost", port=6333)

def init_qdrant_collection(name: str, vector_size: int = 384):
    if not qdrant_client.collection_exists(name):
        qdrant_client.recreate_collection(
            collection_name=name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )



def insert_vector(collection: str, doc_id: str, text: str):
    vector = get_embedding(text)
    qdrant_client.upsert(
        collection_name=collection,
        points=[
            PointStruct(
                id=int.from_bytes(doc_id.encode(), "big") % 2**63,
                vector=vector,
                payload={"mongo_id": doc_id}
            )
        ]
    )



def semantic_search(collection: str, query: str, limit: int = 2):
    vector = get_embedding(query)
    results = qdrant_client.search(
        collection_name=collection,
        query_vector=vector,
        limit=limit
    )
    return results

async def create_text_index(db, collection: str):
    if "text_index" not in db[collection].index_information():
        db[collection].create_index(
            [("title", "text"), ("content", "text")],
            name="text_index"
        )
        print(f"Text index created for {collection} collection.")
    else:
        print(f"Text index already exists for {collection} collection.")
    return True