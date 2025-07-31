from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Knowledge Base API is running 🚀"}
