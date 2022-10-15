from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str
    zachalo: int


class Date(BaseModel):
    week: int
    day: str
    period: int = Field(description="Один из трех периодов")


class Reading(BaseModel):
    date: Date
    book: Book
