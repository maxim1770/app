from pydantic import BaseModel, constr

from app.create import const
from app.schemas.holiday.holiday import Holiday


class SaintCreate(BaseModel):
    slug: constr(strip_whitespace=True, strict=True, max_length=70, regex=const.REGEX_SLUG)


class SaintBase(SaintCreate):
    name: constr(strip_whitespace=True, strict=True, max_length=100)


class Saint(SaintBase):
    id: int

    dignity_id: int | None
    face_sanctity_id: int | None

    holidays: list[Holiday] = []

    class Config:
        orm_mode = True
