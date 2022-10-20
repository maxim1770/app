from pydantic import BaseModel, Field


class ReadingBase(BaseModel):
    pass


class ReadingCreate(ReadingBase):
    pass


class Reading(ReadingBase):
    id: int
    date_id: int
    num_id: int

    class Config:
        orm_mode = True


class ZachaloBase(BaseModel):
    num: int


class ZachaloCreate(ZachaloBase):
    pass


class Zachalo(ZachaloBase):
    id: int
    book_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    new_or_old_testament: str
    section: str = Field(description="Н: Евангелие/Апостолы/Пятикнижие")
    title: str | None
    title_short_en: str


class BookCreate(BookBase):
    pass


class BookGospelCreate(BookCreate):
    new_or_old_testament: str = 'НЗ'
    section: str = 'Евангелие'


class BookApostleCreate(BookCreate):
    new_or_old_testament: str = 'НЗ'
    section: str = 'Апостол'


class Book(BookBase):
    zachalos: list[Zachalo] = []

    class Config:
        orm_mode = True


class DateBase(BaseModel):
    day: str
    day_title: str | None
    divine_service: str | None


class DateCreate(DateBase):
    pass


class Date(DateBase):
    id: int
    week_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True


class WeekBase(BaseModel):
    title: str
    num: int
    sunday_title: str
    sunday_num: int


class WeekCreate(WeekBase):
    pass


class Week(WeekBase):
    id: int
    dates: list[Date] = []
    period_id: int

    class Config:
        orm_mode = True


class PeriodBase(BaseModel):
    title: str | None
    num: int


class PeriodCreate(PeriodBase):
    pass


class Period(PeriodBase):
    id: int
    weeks: list[Week] = []

    class Config:
        orm_mode = True
