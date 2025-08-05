from fastapi import FastAPI
from app.routers import auth , tag , category , article
# from app.routers import tag

app = FastAPI()


app.include_router(auth.router)
app.include_router(tag.router)
app.include_router(category.router)
app.include_router(article.router)



@app.get("/")
async def root():
    return {"message": "Knowledge Base API is running 🚀"}
