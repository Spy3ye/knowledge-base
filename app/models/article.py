from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List, Optional

class ArticleModel(BaseModel):
    # id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    title: str
    body: str
    tags: List[ObjectId] = []        # Many-to-many relationship
    category_id: Optional[ObjectId] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    embedding: Optional[List[float]] = None  # For vector search
    author_id: Optional[ObjectId] = None  # Reference to User model
    