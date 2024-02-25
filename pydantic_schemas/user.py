from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # convert orm objects to dict
    # Allow SQLAlchemy and pydantic to work together
    class Config:
        orm_mode = True
