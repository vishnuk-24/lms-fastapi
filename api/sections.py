from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.db import get_db
from pydantic_schemas.content_block import ContentBlock
from pydantic_schemas.section import Section
from .utils.sections import get_section, read_section_content_block
from .utils.content_blocks import get_content_block


router = APIRouter()


@router.get("/sections/{section_id}", response_model=Section)
async def _get_section(section_id: int, db: Session = Depends(get_db)):
    section = get_section(db=db, section_id=section_id)
    if section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return section


@router.get("/sections/{section_id}/content-blocks", response_model=ContentBlock)
async def _read_section_content_blocks(section_id, db: Session = Depends(get_db)):
    section = get_section(db=db, section_id=section_id)
    if section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return read_section_content_block(db=db, section_id=section_id)


@router.get("/content-blocks/{content_block_id}", response_model=ContentBlock)
async def _read_content_block(content_block_id: int, db: Session = Depends(get_db)):
    content_block = get_content_block(db=db, content_block_id=content_block_id)
    if content_block is None:
        raise HTTPException(status_code=404, detail="Content block not found")
    return content_block
