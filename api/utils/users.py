from typing import List

from sqlalchemy.orm import Session

from db.models.user import User
from pydantic_schemas import user


def get_user(db: Session, user_id: int) -> user.User:
    db_user = db.query(User).filter(User.id == user_id).first()
    return user.User(**db_user.__dict__)


def get_user_by_email(db: Session, email: str) -> user.User:
    db_user = db.query(User).filter(User.email == email).first()
    return user.User(**db_user.__dict__)


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[user.User]:
    db_users = db.query(User).offset(skip).limit(limit).all()
    return [user.User(**db_user.__dict__) for db_user in db_users]


def create_user(db: Session, user: user.UserCreate) -> user.User:
    # fake_hashed_password = user.password + "notreallyhashed"
    # db_user = user.User(email=user.email, hashed_password=fake_hashed_password)
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
