from app.models.user import User
from app.schemas.user import UserCreate
from app.db.mongo import db
from app.utils.security import hash_password
from app.utils.email_utils import send_email


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

def send_verification_email(user_email: str, token: str):
    verify_link = f"http://localhost:8000/auth/verify-email?token={token}"
    subject = "Verify your email"
    body = f"""
    <h2>Email Verification</h2>
    <p>Please click the link below to verify your email:</p>
    <a href="{verify_link}">{verify_link}</a>
    """
    send_email(subject, user_email, body)



def send_password_reset_email(user_email: str, token: str):
    reset_link = f"http://localhost:8000/auth/reset-password?token={token}"
    subject = "Reset your password"
    body = f"""
    <h2>Password Reset</h2>
    <p>Click below to reset your password:</p>
    <a href="{reset_link}">{reset_link}</a>
    """
    send_email(subject, user_email, body)