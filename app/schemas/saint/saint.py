from pydantic import BaseModel, constr

from app import const
from app.schemas.saint.dignity import Dignity
from app.schemas.saint.face_sanctity import FaceSanctity


class SaintBase(BaseModel):
    name: constr(strip_whitespace=True, strict=True, max_length=100) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=70, regex=const.REGEX_SLUG) | None = None


class SaintCreate(SaintBase):
    slug: constr(strip_whitespace=True, strict=True, max_length=70, regex=const.REGEX_SLUG)


class SaintUpdate(SaintBase):
    pass


class SaintInDBBase(SaintBase):
    id: int

    slug: str

    dignity: Dignity | None
    face_sanctity: FaceSanctity | None

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True


class Saint(SaintInDBBase):
    pass


class SaintInDB(SaintInDBBase):
    pass
