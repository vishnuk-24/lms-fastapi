from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.db import get_db
from pydantic_schemas.user import User, UserCreate
from pydantic_schemas.course import Course

from .utils.courses import get_user_courses
from .utils.users import get_user, get_user_by_email, get_users, create_user

router = APIRouter()


@router.get("/users", response_model=List[User])
async def _get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users(db=db, skip=skip, limit=limit)


@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def _create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
async def _get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
        )
    return db_user


@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_user_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(user_id=user_id, db=db)
    return courses
