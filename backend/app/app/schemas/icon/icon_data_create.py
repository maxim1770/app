from pydantic import BaseModel, constr

from app import enums, const
from .icon import IconUpdate, IconCreate
from ..year import YearCreate


class __IconDataBase(BaseModel):
    icon_in: IconUpdate | None = None
    year_in: YearCreate | None = None
    city_title: enums.CityTitle | None = None
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR) | None = None


class IconDataCreate(__IconDataBase):
    icon_in: IconCreate
    year_in: YearCreate
    holiday_slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR)
