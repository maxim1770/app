from pydantic import constr

from app import const
from ...base import SchemaBase


class __SaintBase(SchemaBase):
    name: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    name_in_dative: constr(strip_whitespace=True, strict=True, max_length=150) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=150, pattern=const.REGEX_SLUG_STR) | None = None


class SaintCreate(__SaintBase):
    slug: constr(strip_whitespace=True, strict=True, max_length=150, pattern=const.REGEX_SLUG_STR)


class SaintUpdate(__SaintBase):
    pass
