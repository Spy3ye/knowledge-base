from fastapi import APIRouter
from app.schemas.category import CategoryCreate, CategoryBase
from app.services.category import create_category, list_categories

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=str)
async def create(cat: CategoryCreate):
    return await create_category(cat)

@router.get("/", response_model=list[CategoryBase])
async def get_all():
    return await list_categories()
