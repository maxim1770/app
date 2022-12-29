from datetime import date
from pydantic import BaseModel

from app.schemas.saint.cathedral_saints import CathedralSaints
from app.schemas.saint.saint import Saint


class DateBase(BaseModel):
    date: date


class DateCreate(DateBase):
    pass


class Date(DateBase):
    id: int

    cathedrals_saints: list[CathedralSaints] = []

    saints: list[Saint] = []

    class Config:
        orm_mode = True
