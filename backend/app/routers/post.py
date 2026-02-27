from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.deps import get_current_user
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["게시글"])
