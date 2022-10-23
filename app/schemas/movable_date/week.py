from pydantic import BaseModel

from app.schemas.movable_date.day import Day


class WeekBase(BaseModel):
    title: str
    num: int
    sunday_title: str
    sunday_num: int


class WeekCreate(WeekBase):
    title: str | None
    num: int | None
    sunday_title: str | None
    sunday_num: int | None


class Week(WeekBase):
    id: int
    days: list[Day] = []
    cycle_id: int

    class Config:
        orm_mode = True
