from pydantic import BaseModel, Field
from datetime import datetime


class PostCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100, description="게시글 제목")
    content: str = Field(min_length=1, description="게시글 내용")


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
