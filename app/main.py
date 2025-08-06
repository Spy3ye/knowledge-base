from fastapi import FastAPI
from app.routers import auth , tag , category , article , semantic_search
from app.db.mongo import get_database
from app.services.qdrant import init_qdrant_collection , create_text_index
# from app.routers import tag

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    db = await get_database()
    init_qdrant_collection("articles")
    init_qdrant_collection("categories")
    init_qdrant_collection("tags")
    await create_text_index(db, "articles")
    await create_text_index(db, "categories")
    await create_text_index(db, "tags")

app.include_router(auth.router)
app.include_router(tag.router)
app.include_router(category.router)
app.include_router(article.router)
app.include_router(semantic_search.router, prefix="/semantic", tags=["Semantic Search"])



@app.get("/")
async def root():
    return {"message": "Knowledge Base API is running 🚀"}
