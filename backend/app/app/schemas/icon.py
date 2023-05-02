from pydantic import BaseModel, constr

from app import enums
from .city import City
from .year import Year, YearCreate


class IconBase(BaseModel):
    desс: constr(strip_whitespace=True, strict=True, max_length=350) | None = None


class IconCreate(IconBase):
    pass


class IconUpdate(IconBase):
    pass


class IconInDBBase(IconBase):
    id: int

    desс: str

    city: City | None
    year: Year

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


class IconDataCreate(IconDataBase):
    icon_in: IconCreate


class IconDataUpdate(IconDataBase):
    pass
