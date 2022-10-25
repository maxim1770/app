from pydantic import BaseModel

from app.schemas.reading import Reading


class MovableDateBase(BaseModel):
    pass


class MovableDateCreate(MovableDateBase):
    pass


class MovableDate(MovableDateBase):
    id: int

    day_id: int
    divine_service_id: int

    readings: list[Reading] = []

    class Config:
        orm_mode = True
