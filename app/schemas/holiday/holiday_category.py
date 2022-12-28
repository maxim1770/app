from enum import Enum

from pydantic import BaseModel

from app.schemas.holiday.holiday import Holiday


class HolidayCategoryTitle(str, Enum):
    pass


class HolidayCategoryBase(BaseModel):
    title: HolidayCategoryTitle


class HolidayCategoryCreate(HolidayCategoryBase):
    pass


class HolidayCategory(HolidayCategoryBase):
    id: int

    holidays: list[Holiday] = []

    class Config:
        orm_mode = True
