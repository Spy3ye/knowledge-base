from fastapi import FastAPI
from app.routers import auth

app = FastAPI()


app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Knowledge Base API is running 🚀"}
