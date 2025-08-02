from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.database_name]
async def get_database():
    return client[settings.database_name]
