from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.services.user import create_user, get_user_by_email
from app.db.mongo import get_database
from app.models.user import User
from app.utils.security import verify_password, create_access_token , hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
async def register(user_in: UserCreate , db= Depends(get_database)):
    if await get_user_by_email(user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await create_user(user_in)
    return user

@router.post("/login")
async def login(user_in: UserLogin , db= Depends(get_database)):
    user = await get_user_by_email(user_in.email)
    if not user or not verify_password(user_in.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(user["_id"])}, expires_minutes=60)
    return {"access_token": token, "token_type": "bearer"}
# @router.get("/me", response_model=UserOut)
# async def get_current_user(current_user: UserOut = Depends(get_current_user)):
#     if not current_user:
#         raise HTTPException(status_code=401, detail="Not authenticated")
#     return current_user