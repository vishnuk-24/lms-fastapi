import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from ..db import Base
from .mixins import TimeStamp


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(TimeStamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    role = Column(Enum(Role))
    is_active = Column(Boolean, default=False)

    profile = relationship("Profile", back_populates="owner", uselist=False)
    student_courses = relationship("StudentCourse", back_populates="student")
    student_content_blocks = relationship(
        "CompletedContentBlock", back_populates="student"
    )


class Profile(TimeStamp, Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
