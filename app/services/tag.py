# from app.models.tag import tag_collection
from app.schemas.tag import TagCreate
from bson import ObjectId
from fastapi import HTTPException, status , Depends
from app.db.mongo import get_database , db

async def create_tag(tag: TagCreate ):
    result = await db["tags"].insert_one(tag.dict())
    return str(result.inserted_id)

async def list_tags():
    tags = db["tags"].find()
    return [dict(tag, _id=str(tag["_id"])) async for tag in tags]
