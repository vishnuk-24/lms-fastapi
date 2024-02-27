from sqlalchemy.orm import Session
from db.models.course import ContentBlock
from pydantic_schemas.content_block import ContentBlockCreate


def get_content_block(db: Session, content_block_id: int):
    return db.query(ContentBlock).filter(ContentBlock.id == content_block_id).first()


def create_content_block(db: Session, content_block: ContentBlockCreate):
    db_content_block = ContentBlock(
        title=content_block.title,
        description=content_block.description,
        type=content_block.type,
        url=content_block.url,
        content=content_block.content,
        section_id=content_block.section_id,
    )
    db.add(db_content_block)
    db.commit()
    db.refresh(db_content_block)
    return db_content_block
