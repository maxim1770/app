from pydantic import BaseModel

from app import enums


# from .movable_date import MovableDate


class DivineServiceBase(BaseModel):
    title: enums.DivineServiceTitle


class DivineServiceCreate(DivineServiceBase):
    pass


class DivineService(DivineServiceBase):
    id: int

    # movable_dates: list[MovableDate] = []

    class Config:
        orm_mode = True
