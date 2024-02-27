from typing import Optional

from pydantic import BaseModel, AnyUrl


class ContentBlockBase(BaseModel):
    title: str
    description: Optional[str]
    type: int
    url: AnyUrl
    content: str
    section_id: int


class ContentBlockCreate(ContentBlockBase):
    ...


class ContentBlock(ContentBlockCreate):
    id: int
