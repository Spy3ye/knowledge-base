from fastapi import APIRouter, Depends
from bson import ObjectId
from app.db.mongo import get_database
from app.services.qdrant import semantic_search

router = APIRouter()

@router.get("/semantic-search")
async def search_semantically(collection: str, query: str, db=Depends(get_database)):
    results = semantic_search(collection, query)

    ids = []
    for res in results:
        mongo_id = res.payload.get("mongo_id")
        if mongo_id:
            try:
                ids.append(ObjectId(mongo_id))
            except Exception:
                pass

    if ids:
        documents = await db[collection].find({"_id": {"$in": ids}}).to_list(length=len(ids))
    else:
        documents = []

    # 🔁 Convert ObjectId to str to make it JSON serializable
    for doc in documents:
        doc["_id"] = str(doc["_id"])

    return documents
