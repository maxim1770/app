from pydantic import BaseModel

from app.schemas.movable_date.week import Week


class CycleBase(BaseModel):
    title: str | None
    num: int


class CycleCreate(CycleBase):
    pass



class Cycle(CycleBase):
    id: int
    weeks: list[Week] = []

    class Config:
        orm_mode = True

# Cycle
#
# movable_date
#
# cycle
