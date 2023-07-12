from pydantic import BaseModel

from app.models import Post
from app.schemas import PostCreate, PostUpdate
from .base import CRUDBase


class PostFilter(BaseModel):
    pass


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate, PostFilter]):
    pass


post = CRUDPost(Post)
