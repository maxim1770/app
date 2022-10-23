from pydantic import BaseModel

from app.schemas.reading import Reading


class DivineServiceBase(BaseModel):
    title: str


class DivineServiceCreate(DivineServiceBase):
    title: str | None


class DivineService(DivineServiceBase):
    id: int
    day_id: int
    readings: list[Reading] = []

    class Config:
        orm_mode = True

