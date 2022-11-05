from pydantic import BaseModel

from app.schemas.movable_date.day import Day


class WeekBase(BaseModel):
    title: str | None
    num: int | None
    sunday_title: str | None
    sunday_num: int


class WeekCreate(WeekBase):
    pass


class Week(WeekBase):
    id: int

    cycle_id: int

    days: list[Day] = []

    class Config:
        orm_mode = True
