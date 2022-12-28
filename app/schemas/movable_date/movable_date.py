from pydantic import BaseModel

from app.schemas.movable_date.divine_service import DivineService
from app.schemas.reading import Reading


class MovableDateBase(BaseModel):
    pass


class MovableDateCreate(MovableDateBase):
    pass


class MovableDate(MovableDateBase):
    id: int

    movable_day_id: int
    # divine_service_id: int
    divine_service: DivineService

    readings: list[Reading] = []

    class Config:
        orm_mode = True
