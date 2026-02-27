import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.database import engine, Base
from app.models.post import Post  # noqa: F401
from app.models.user import User  # noqa: F401
from app.routers import post as post_router
from app.routers import upload as upload_router
from app.routers import auth as auth_router
from app.middleware import log_requests

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)

cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        origin.strip() for origin in cors_origins.split(",")
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.middleware("http")(log_requests)

app.include_router(post_router.router)
app.include_router(upload_router.router)
app.include_router(auth_router.router)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


@app.get("/")
def health_check():
    return {"status": "ok"}
