from odmantic import Model
from odmantic import Field
from typing import Optional
from enum import Enum
from uuid import uuid4,UUID

class UserRole(str, Enum):
    admin = "admin"
    user = "user"

class User(Model):
    # user_Id: UUID = Field(default_factory=uuid4)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: str
    hashed_password: str
    is_active: bool = True
    role: UserRole = UserRole.user
