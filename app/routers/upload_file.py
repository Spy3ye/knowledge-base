from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import os
from app.services.qdrant import insert_vector

from app.services.extract_file import extract_text_from_pdf, extract_text_from_csv , extract_text_from_txt
# from app.services.embedding_service import embed_and_store
from app.db.mongo import get_database
from bson import ObjectId

router = APIRouter()

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "csv" , "txt"]:
        raise HTTPException(status_code=400, detail="Only PDF, CSV, and TXT files are supported.")

    file_id = str(uuid4())
    temp_path = f"/tmp/{file_id}.{ext}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    if ext == "pdf":
        content = extract_text_from_pdf(temp_path)
    elif ext == "txt":
        content = extract_text_from_txt(temp_path)
    else:
        content = extract_text_from_csv(temp_path)

    os.remove(temp_path)

    db = await get_database()
    doc = {"filename": file.filename, "content": content}
    result = await db["documents"].insert_one(doc)
    mongo_id = str(result.inserted_id)
    text = file.filename + " " + content
    insert_vector("documents",mongo_id,text)
    return str(result.inserted_id)

    # Embed and store in Qdrant
    # await embed_and_store(
    #     collection_name="documents",
    #     mongo_id=str(result.inserted_id),
    #     content=content
    # )

    return {"id": str(result.inserted_id), "filename": file.filename, "preview": content[:300]}
