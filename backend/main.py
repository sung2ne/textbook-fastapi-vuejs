from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import os
from dotenv import load_dotenv

from app.database import engine, Base
from app.models.post import Post  # noqa: F401
from app.models.user import User  # noqa: F401
from app.routers import post as post_router
from app.routers import upload as upload_router
from app.routers import auth as auth_router
from app.routers import ws as ws_router
from app.middleware import log_requests

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="게시판 API", version="0.1.0")

app.middleware("http")(log_requests)

origins = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "서버 내부 오류가 발생했습니다"})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({"field": " → ".join(str(loc) for loc in error["loc"]), "message": error["msg"]})
    return JSONResponse(status_code=422, content={"detail": "입력값 검증 실패", "errors": errors})

app.include_router(post_router.router)
app.include_router(upload_router.router)
app.include_router(auth_router.router)
app.include_router(ws_router.router)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
