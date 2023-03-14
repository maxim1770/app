from pydantic import BaseModel, constr

from app import enums
from .week import Week


class CycleBase(BaseModel):
    num: enums.CycleNum
    title: constr(strip_whitespace=True, strict=True, max_length=30)


class CycleCreate(CycleBase):
    pass


class Cycle(CycleBase):
    id: int

    weeks: list[Week] = []

    class Config:
        orm_mode = True
