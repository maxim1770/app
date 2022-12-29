from pydantic import BaseModel

from app.schemas.movable_date.movable_day import MovableDay


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

    movable_days: list[MovableDay] = []

    class Config:
        orm_mode = True
