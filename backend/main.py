from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: int, page: int = 1, size: int = 10
):
    return {
        "user_id": user_id,
        "page": page,
        "size": size,
    }
