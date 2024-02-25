from typing import Optional
from pydantic import BaseModel


class SectionBase(BaseModel):
    title: str
    description: Optional[str] = None
    course_id: int


class SectionCreate(SectionBase):
    ...


class Section(SectionCreate):
    id: int

    class Config:
        orm_mode = True
