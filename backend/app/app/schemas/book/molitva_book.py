from pydantic import BaseModel, conint, validator

from app import enums
from .book import BookInDB


class MolitvaBookBase(BaseModel):
    type: enums.MolitvaBookType | None = None
    glas_num: conint(strict=True, ge=1, le=8) | None = None


class MolitvaBookCreate(MolitvaBookBase):
    type: enums.MolitvaBookType


class MolitvaBookInDBBase(MolitvaBookBase):
    id: int

    title: str | None = None

    @validator('title', pre=True, always=True)
    def prepare_title(cls, title: None, values):
        title: str = f"{values['type']} глас {values['glas_num']}" if values['glas_num'] else f"{values['type']}"
        return title

    class Config:
        orm_mode = True


class MolitvaBook(MolitvaBookInDBBase):
    book: BookInDB


class MolitvaBookInDB(MolitvaBookInDBBase):
    pass
