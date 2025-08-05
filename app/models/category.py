from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional

class CategoryModel(BaseModel):
    # id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    