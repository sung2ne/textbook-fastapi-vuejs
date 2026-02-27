from fastapi import FastAPI
from datetime import datetime
from app.schemas.post import PostCreate, PostResponse
from app.database import engine, Base
from app.models.post import Post  # noqa: F401

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)

# 테이블 생성
Base.metadata.create_all(bind=engine)

# 임시 데이터 저장소
posts_db = []
next_id = 1
