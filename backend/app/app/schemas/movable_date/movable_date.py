from pydantic import BaseModel

from .divine_service import DivineService
from ..bible_book import Zachalo


class MovableDateBase(BaseModel):
    pass


class MovableDateCreate(MovableDateBase):
    pass


class MovableDate(MovableDateBase):
    id: int

    movable_day_id: int
    # divine_service_id: int
    divine_service: DivineService

    zachalos: list[Zachalo] = []

    class Config:
        orm_mode = True
