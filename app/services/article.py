# from app.models.article import article_collection
from app.schemas.article import ArticleCreate
from app.db.mongo import db
from app.services.qdrant import insert_vector

async def create_article(article: ArticleCreate):
    result = await db["articles"].insert_one(article.dict())
    mongo_id = str(result.inserted_id)
    text = article.title + " " + article.body
    insert_vector("articles",mongo_id,text)
    return str(result.inserted_id)

async def list_articles():
    articles = db["articles"].find()
    return [dict(a, _id=str(a["_id"])) async for a in articles]

async def get_article_by_title(title: str):
    article = await db["articles"].find_one({"title": title})
    if article:
        return dict(article, _id=str(article["_id"]))
    return None

async def get_article_by_id(article_id: str):
    article = await db["articles"].find_one({"_id": article_id})
    if article:
        return dict(article, _id=str(article["_id"]))
    return None

async def get_articles_by_tag(tag: str):
    articles = db["articles"].find({"tags": tag})
    if articles :
        return [dict(a, _id=str(a["_id"])) async for a in articles]
    return None

async def get_articles_by_category(category: str):
    articles = db["articles"].find({"category": category})
    return [dict(a, _id=str(a["_id"])) async for a in articles]
