from pydantic import BaseModel

from app import enums


class HolidayCategoryBase(BaseModel):
    title: enums.HolidayCategoryTitle


class HolidayCategoryCreate(HolidayCategoryBase):
    pass


class HolidayCategory(HolidayCategoryBase):
    id: int

    class Config:
        orm_mode = True
