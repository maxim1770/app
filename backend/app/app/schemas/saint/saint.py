from pydantic import BaseModel, constr, HttpUrl, validator

from app import const, enums
from .face_sanctity import FaceSanctity
from ..saint import Dignity


class SaintBase(BaseModel):
    name: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR) | None = None


class SaintCreate(SaintBase):
    slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR)


class SaintUpdate(SaintBase):
    pass


class SaintInDBBase(SaintBase):
    id: int

    slug: str

    dignity: Dignity | None
    face_sanctity: FaceSanctity | None
    url: HttpUrl = None

    # holidays: list[Holiday] = []

    @validator('url', pre=True, always=True)
    def prepare_url(cls, url: None, values):
        return 'https://azbyka.ru/days/sv-' + values['slug']

    class Config:
        orm_mode = True


class Saint(SaintInDBBase):
    pass


class SaintInDB(SaintInDBBase):
    pass


class SaintDataBase(BaseModel):
    saint_in: SaintUpdate | None = None
    face_sanctity_title: enums.FaceSanctityTitle | None = None
    dignity_title: enums.DignityTitle | None = None


class SaintDataCreate(SaintDataBase):
    saint_in: SaintCreate


class SaintDataUpdate(SaintDataBase):
    pass
