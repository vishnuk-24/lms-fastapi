from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int
    bio: Optional[str]


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # convert orm objects to dict
    # Allow sqlalchemy and pydantic to work together
    class Config:
        orm_mode = True
