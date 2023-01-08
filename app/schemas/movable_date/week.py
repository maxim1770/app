from pydantic import BaseModel, conint

from app.schemas.movable_date.movable_day import MovableDay


class WeekBase(BaseModel):
    title: str | None
    num: conint(strict=True, ge=1, le=36) | None
    sunday_title: str | None
    sunday_num: conint(strict=True, ge=1, le=36)


class WeekCreate(WeekBase):
    pass


class Week(WeekBase):
    id: int

    cycle_id: int

    movable_days: list[MovableDay] = []

    class Config:
        orm_mode = True
