from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Student Management API",
    description="Simple CRUD API using FastAPI",
    version="1.0.0"
)

app.include_router(router)