from app.models.user import User
from app.schemas.user import UserCreate
from app.db.mongo import db
from app.utils.security import hash_password


async def create_user(user_in: UserCreate ) -> User:
    user = User(email=user_in.email, hashed_password=hash_password(user_in.password) , first_name=user_in.first_name, last_name=user_in.last_name, username=user_in.username)
    await db["users"].insert_one(user.dict())
    return user

async def get_user_by_email(email: str) -> User | None:
    return await db["users"].find_one({"email": email})
# async def get_current_user(user_id: str) -> User | None:
#     return await engine.find_one(User, User.user_Id == user_id)
async def get_user_by_id(user_id: str) -> User | None:
    return await db["users"].find_one({"_id": user_id})