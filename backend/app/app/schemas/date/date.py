from pydantic import conint

from ..base import SchemaBase


class __DateBase(SchemaBase):
    year: conint(strict=True, ge=2_000, le=3_000) | None = None


class DateCreate(__DateBase):
    year: conint(strict=True, ge=2_000, le=3_000)


class DateUpdate(__DateBase):
    pass
