from sqlalchemy.orm import Session

from db.models.course import Section, ContentBlock
from pydantic_schemas.section import SectionCreate


def get_sections(db: Session):
    return db.query(Section).all()


def get_section(db: Session, section_id: int):
    return db.query(Section).filter(Section.id == section_id).first()


def create_section(db: Session, section: SectionCreate):
    db_section = Section(
        title=section.title,
        description=section.description,
        course_id=section.course_id,
    )
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def read_section_content_block(db: Session, section_id: int):
    return db.query(ContentBlock).filter(ContentBlock.section_id == section_id).all()


def update_section(db: Session, section: SectionCreate):
    section = db.merge(section)
    db.commit()
    return section
