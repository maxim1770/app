from datetime import date
from enum import StrEnum, auto
from typing import Annotated
from uuid import UUID, uuid4

from pydantic import conint, field_validator, Field

from .base import SchemaBase


class HighlightColor(StrEnum):
    indigo = auto()
    purple = auto()
    blue = auto()
    red = auto()


class Highlight(SchemaBase):
    fillMode: str = 'light'
    color: HighlightColor


class Highlights(SchemaBase):
    start: Highlight
    base: Highlight
    end: Highlight


class Popover(SchemaBase):
    label: str
    visibility: str = 'hover'
    hideIndicator: bool = False


class CalendarAttributeDates(SchemaBase):
    start: date
    end: date | None = None


class CalendarAttribute(SchemaBase):
    key: Annotated[int | UUID | str | None, Field(validate_default=True)] = None
    dates: CalendarAttributeDates | None = None
    highlight: Highlights | Highlight | HighlightColor | None = None
    dot: HighlightColor | None = None
    popover: Popover | None = None
    order: conint(strict=True, ge=0, le=5) | None = None

    @field_validator('key')
    @classmethod
    def set_not_defined_key_to_uuid(cls, v: int | UUID | str | None) -> int | UUID | str | None:
        if not v:
            v: UUID = uuid4()
        return v
