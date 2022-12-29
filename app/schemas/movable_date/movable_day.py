from pydantic import BaseModel, root_validator

from app import enums
from app.schemas.movable_date.movable_date import MovableDate


class MovableDayBase(BaseModel):
    abbr: enums.MovableDayAbbr
    abbr_ru: enums.MovableDayAbbrRu
    title: str | None


class MovableDayCreate(MovableDayBase):
    abbr_ru: enums.MovableDayAbbrRu | None

    @root_validator()
    def _set_abbr_ru(cls, values: dict) -> dict:
        values["abbr_ru"] = enums.MovableDayAbbrRu[values["abbr"].name]
        return values


class MovableDay(MovableDayBase):
    id: int

    week_id: int

    movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
