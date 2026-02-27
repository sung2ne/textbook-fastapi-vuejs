from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.get("/posts")
def get_posts():
    return [
        {"id": 1, "title": "첫 번째 게시글"},
        {"id": 2, "title": "두 번째 게시글"},
    ]


@app.get("/posts/{post_id}")
def get_post(post_id: int = Path(ge=1, description="게시글 ID")):
    return {"post_id": post_id, "title": f"게시글 {post_id}"}
