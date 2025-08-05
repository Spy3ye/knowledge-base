from fastapi import APIRouter, HTTPException
from app.schemas.tag import TagCreate, TagBase
from app.services.tag import create_tag, list_tags

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.post("/", response_model=str)
async def create(tag: TagCreate):
    return await create_tag(tag)

@router.get("/", response_model=list[TagBase])
async def get_all():
    return await list_tags()
