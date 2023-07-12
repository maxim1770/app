from __future__ import annotations

from pydantic import BaseModel

from app import enums
from .base import SchemaInDBBase


class __PostBase(BaseModel):
    title: enums.PostTitle | None = None


class PostCreate(__PostBase):
    title: enums.PostTitle | None


class PostUpdate(__PostBase):
    pass


class Post(__PostBase, SchemaInDBBase):
    pass
