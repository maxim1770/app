from pydantic import BaseModel, conint, constr

from .movable_day import MovableDay


class WeekBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=100) | None = None
    num: conint(strict=True, ge=1, le=36) | None = None
    sunday_title: constr(strip_whitespace=True, strict=True, max_length=50) | None = None
    sunday_num: conint(strict=True, ge=1, le=36) | None = None


class WeekCreate(WeekBase):
    pass


class Week(WeekBase):
    id: int

    cycle_id: int

    movable_days: list[MovableDay] = []

    class Config:
        orm_mode = True