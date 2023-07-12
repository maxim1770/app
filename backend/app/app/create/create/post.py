from sqlalchemy.orm import Session

from app import schemas, crud, enums
from .base_cls import FatalCreateError


def create_all_posts(db: Session) -> None:
    if crud.post.get_all(db):
        raise FatalCreateError(f'Post: posts already created')
    posts_in = [
        schemas.PostCreate(title=post_title)
        for post_title in enums.PostTitle
    ]
    for post_in in posts_in:
        crud.post.create(db, obj_in=post_in)
