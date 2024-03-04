import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import users, courses, sections
from db.db import engine
from db.models import user, course


user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Learning management system")

origins = ["*"]  # TODO: adjust for production

app.add_middleware(
    CORSMiddleware(
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
