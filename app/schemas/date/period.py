from pydantic import BaseModel

from app.schemas.date.week import Week


class PeriodBase(BaseModel):
    title: str | None
    num: int


class PeriodCreate(PeriodBase):
    pass


class Period(PeriodBase):
    id: int
    weeks: list[Week] = []

    class Config:
        orm_mode = True
