from pydantic import conint, model_validator

from app import models
from .book import BookInDB
from ..base import SchemaBase, SchemaInDBBase


class __MolitvaBookBase(SchemaBase):
    glas_num: conint(strict=True, ge=1, le=8) | None = None


class MolitvaBookCreate(__MolitvaBookBase):
    pass


class __MolitvaBookInDBBase(__MolitvaBookBase, SchemaInDBBase):
    title: str

    @model_validator(mode='before')
    @classmethod
    def prepare_title(cls, values: models.MolitvaBook) -> models.MolitvaBook:
        values.title: str = f'{values.book.type} глас {values.glas_num}' if values.glas_num else f'{values.book.type}'
        return values


class MolitvaBook(__MolitvaBookInDBBase):
    book: BookInDB


class MolitvaBookInDB(__MolitvaBookInDBBase):
    pass
