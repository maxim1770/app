from pydantic import BaseModel


class DayBase(BaseModel):
    month: int
    day: int


class DayCreate(DayBase):
    pass


class Day(DayBase):
    id: int

    class Config:
        orm_mode = True
