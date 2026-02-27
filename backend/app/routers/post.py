@router.get("/", summary="게시글 목록")
def list_posts(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
):
    offset = (page - 1) * size
    total = db.query(Post).count()
    posts = (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(size)
        .all()
    )
    return {"items": posts, "total": total}
