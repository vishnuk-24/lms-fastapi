import uvicorn

from fastapi import FastAPI
from api import users, courses, sections
from db.db import engine
from db.models import user, course


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Learning management system")


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
