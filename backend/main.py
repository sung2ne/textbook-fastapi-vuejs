from fastapi import FastAPI

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/posts", tags=["게시글"], summary="게시글 목록")
def list_posts(page: int = 1):
    """
    게시글 목록을 반환합니다.

    - **page**: 페이지 번호 (기본값: 1)
    """
    return {"page": page, "posts": []}


@app.post("/posts", tags=["게시글"], summary="게시글 생성")
def create_post():
    return {"message": "게시글이 생성되었습니다."}


@app.get("/posts/{post_id}", tags=["게시글"], summary="게시글 상세")
def get_post(post_id: int):
    return {"post_id": post_id}
