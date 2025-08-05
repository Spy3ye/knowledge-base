from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    body: str
    tags: Optional[List[str]] = []
    category_id: Optional[str] = None

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(ArticleBase):
    title: Optional[str]
    body: Optional[str]

class ArticleResponse(ArticleBase):
    id: str
    title: str
    created_at: datetime
    updated_at: Optional[datetime]
    embedding: Optional[List[float]] = None  # For vector search
    author_id: Optional[str] = None  # Reference to User model