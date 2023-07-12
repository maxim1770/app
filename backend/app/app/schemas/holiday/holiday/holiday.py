from pydantic import constr

from app import const
from ...base import SchemaBase


class __HolidayBase(SchemaBase):
    title: constr(strip_whitespace=True, strict=True, max_length=200) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR) | None = None


class HolidayCreate(__HolidayBase):
    title: constr(strip_whitespace=True, strict=True, max_length=200)
    slug: constr(strip_whitespace=True, strict=True, max_length=200, pattern=const.REGEX_SLUG_STR)


class HolidayUpdate(__HolidayBase):
    pass
