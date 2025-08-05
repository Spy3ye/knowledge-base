from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str
    description: Optional[str] = None

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
