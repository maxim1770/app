from pydantic import BaseModel, Field

from app.schemas.book.zachalo import Zachalo


class BookBase(BaseModel):
    new_or_old_testament: str
    section: str = Field(description="Н: Евангелие/Апостолы/Пятикнижие")
    title: str | None
    title_short_en: str


class BookCreate(BookBase):
    pass


class BookGospelCreate(BookCreate):
    new_or_old_testament: str = 'НЗ'
    section: str = 'Евангелие'


class BookApostleCreate(BookCreate):
    new_or_old_testament: str = 'НЗ'
    section: str = 'Апостол'


class Book(BookBase):
    zachalos: list[Zachalo] = []

    class Config:
        orm_mode = True
