# from app.models.category import category_collection
from app.schemas.category import CategoryCreate
from app.db.mongo import db
from app.services.qdrant import insert_vector

async def create_category(cat: CategoryCreate):
    result = await db["categories"].insert_one(cat.dict())
    mongo_id = str(result.inserted_id)
    text = cat.name + " " + cat.description
    insert_vector("categories",mongo_id,text)
    return str(result.inserted_id)

async def list_categories():
    cats = db["categories"].find()
    return [dict(c, _id=str(c["_id"])) async for c in cats]
