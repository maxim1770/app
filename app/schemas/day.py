from pydantic import BaseModel, conint


class DayBase(BaseModel):
    month: conint(strict=True, ge=1, le=12)
    day: conint(strict=True, ge=1, le=31)


class DayCreate(DayBase):
    pass


class Day(DayBase):
    id: int

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True
