from pydantic import BaseModel, Field


class ReadingBase(BaseModel):
    pass


class ReadingCreate(ReadingBase):
    pass


class Reading(ReadingBase):
    id: int
    date_id: int
    bible_zachalo_id: int

    class Config:
        orm_mode = True


class BibleZachaloBase(BaseModel):
    title: str
    zachalo: int


class BibleZachaloCreate(BibleZachaloBase):
    pass


class BibleZachalo(BibleZachaloBase):
    id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True


class DateBase(BaseModel):
    week: int
    day: str
    period: int = Field(description="Один из трех периодов")


class DateCreate(DateBase):
    pass


class Date(DateBase):
    id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True
