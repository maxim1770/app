from pydantic import BaseModel
from app.schemas.holiday.holiday import Holiday


class SaintBase(BaseModel):
    name: str | None = None
    name_en: str


class SaintCreate(SaintBase):
    pass


class Saint(SaintBase):
    id: int

    dignity_id: int | None
    face_sanctity_id: int | None

    holidays: list[Holiday] = []

    class Config:
        orm_mode = True
