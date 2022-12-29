from pydantic import BaseModel

from app import enums

from app.schemas.movable_date.week import Week


class CycleBase(BaseModel):
    num: enums.CycleNum
    title: str | None


class CycleCreate(CycleBase):
    pass


class Cycle(CycleBase):
    id: int

    weeks: list[Week] = []

    class Config:
        orm_mode = True
