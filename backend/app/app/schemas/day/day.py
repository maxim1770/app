from pydantic import conint

from ..base import SchemaBase


class __DayBase(SchemaBase):
    month: conint(strict=True, ge=1, le=12) | None = None
    day: conint(strict=True, ge=1, le=31) | None = None


class DayCreate(__DayBase):
    month: conint(strict=True, ge=1, le=12)
    day: conint(strict=True, ge=1, le=31)


class DayUpdate(__DayBase):
    pass
