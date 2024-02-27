from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.db import get_db
from pydantic_schemas.course import Course, CourseCreate
from pydantic_schemas.section import Section

from .utils.courses import (
    get_course,
    get_courses,
    create_course,
    update_course,
    delete_course,
    read_course_sections,
)


router = APIRouter()


@router.get("/courses", response_model=List[Course])
async def _get_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
async def _create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}", response_model=Course)
async def _get_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Course not found"
        )
    return db_course


@router.patch("/courses/{course_id}", response_model=Course)
async def _update_course(
    course_id: int, course: CourseCreate, db: Session = Depends(get_db)
):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    course_encoded = jsonable_encoder(course)
    db_course.title = course_encoded["title"]
    db_course.description = course_encoded["description"]
    db_course.user_id = course_encoded["user_id"]
    return update_course(db=db, course=db_course)


@router.delete("/courses/{course_id}")
async def _delete_course(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Course not found"
        )
    delete_course(db=db, course_id=course_id)
    return "success"


@router.get("/courses/{course_id}/sections", response_model=List[Section])
async def _read_course_sections(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=course_id)
    if db_course is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Course not found"
        )
    return read_course_sections(db=db, course_id=course_id)
