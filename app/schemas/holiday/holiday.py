from pydantic import BaseModel


class HolidayBase(BaseModel):
    title: str | None = None
    title_en: str


class HolidayCreate(HolidayBase):
    pass


class Holiday(HolidayBase):
    id: int

    holiday_category_id: int | None
    year_id: int | None
    day_id: int | None

    saint_id: int | None

    class Config:
        orm_mode = True
