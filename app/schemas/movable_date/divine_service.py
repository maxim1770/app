from enum import auto

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel


# from app.schemas.movable_date import MovableDate


class DivineServiceEnum(StrEnum):
    liturgy = auto()
    matins = auto()
    vespers = auto()


class DivineServiceBase(BaseModel):
    title: DivineServiceEnum


class DivineServiceCreate(DivineServiceBase):
    pass


class DivineService(DivineServiceBase):
    id: int

    # movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
