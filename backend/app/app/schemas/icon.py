from pathlib import Path

from pydantic import BaseModel, constr

from app import enums, const
from .city import City
from .year import Year, YearCreate


class IconBase(BaseModel):
    desc: constr(strip_whitespace=True, strict=True, max_length=450) | None = None
    pravicon_id: int | None = None
    gallerix_id: int | None = None
    shm_id: int | None = None


class IconCreate(IconBase):
    pass


class IconUpdate(IconBase):
    pass


class IconInDBBase(IconBase):
    id: int

    desc: str

    path: Path | None = None

    city: City | None
    year: Year | None

    class Config:
        orm_mode = True


class Icon(IconInDBBase):
    pass


class IconInDB(IconInDBBase):
    pass


class IconDataBase(BaseModel):
    icon_in: IconUpdate | None = None
    year_in: YearCreate
    city_title: enums.CityTitle | None = None
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)


class IconDataCreate(IconDataBase):
    icon_in: IconCreate


class IconDataUpdate(IconDataBase):
    pass
