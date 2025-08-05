from fastapi import APIRouter , HTTPException
from app.schemas.article import ArticleCreate, ArticleBase
from app.services.article import create_article, list_articles , get_article_by_title , get_article_by_id , get_articles_by_tag , get_articles_by_category

router = APIRouter(prefix="/articles", tags=["Articles"])

@router.post("/", response_model=str)
async def create(article: ArticleCreate):
    return await create_article(article)

@router.get("/", response_model=list[ArticleBase])
async def get_all():
    return await list_articles()

@router.get("/{title}", response_model=ArticleBase)
async def get_by_title(title: str):
    article = await get_article_by_title(title)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/id/{article_id}", response_model=ArticleBase)
async def get_by_id(article_id: str):
    article = await get_article_by_id(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/tag/{tag}", response_model=list[ArticleBase])
async def get_by_tag(tag: str):
    articles = await get_articles_by_tag(tag)
    return articles