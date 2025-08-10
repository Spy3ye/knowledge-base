from odmantic import Model
from odmantic import Field
from typing import Optional
from enum import Enum
from uuid import uuid4,UUID


class documents(Model):
    # user_Id: UUID = Field(default_factory=uuid4)
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None