from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import os
from app.services.qdrant import insert_vector

from app.services.extract_file import extract_text_from_pdf, extract_text_from_csv , extract_text_from_txt
# from app.services.embedding_service import embed_and_store
from app.db.mongo import get_database
from bson import ObjectId
from app.utils.chunck import chunk_text
from app.services.file import upload_file, get_document

router = APIRouter()

@router.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    return await upload_file(file)

@router.get("/document/{file_name}")
async def get_document_endpoint(file_name: str):
    return await get_document(file_name)