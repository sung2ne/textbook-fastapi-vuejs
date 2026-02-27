from fastapi import FastAPI
from datetime import datetime
from app.schemas.post import PostCreate, PostResponse

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)

# 임시 데이터 저장소
posts_db = []
next_id = 1


@app.get("/")
def health_check():
    return {"status": "ok"}
