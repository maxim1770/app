from pydantic import BaseModel, validator, constr

from app import enums
from app.schemas.movable_date.movable_date import MovableDate


class MovableDayBase(BaseModel):
    abbr: enums.MovableDayAbbr
    abbr_ru: enums.MovableDayAbbrRu
    title: constr(strip_whitespace=True, strict=True, max_length=30) | None


class MovableDayCreate(MovableDayBase):
    abbr_ru: enums.MovableDayAbbrRu = None

    @validator('abbr_ru', pre=True, always=True)
    def set_abbr_ru(cls, v, values):
        v: enums.MovableDayAbbrRu = enums.MovableDayAbbrRu[values['abbr'].name]
        return v


class MovableDay(MovableDayBase):
    id: int

    week_id: int

    movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
