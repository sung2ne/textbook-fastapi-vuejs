from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}


@app.get("/posts")
def list_posts():
    return {"posts": [{"id": 1, "title": "첫 번째 글"}]}


@app.post("/posts")
def create_post():
    return {"message": "게시글이 생성되었습니다"}


@app.put("/posts/{post_id}")
def update_post(post_id: int):
    return {"message": f"{post_id}번 게시글이 수정되었습니다"}


@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    return {"message": f"{post_id}번 게시글이 삭제되었습니다"}
