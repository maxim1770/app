from typing import Any

from pydantic import model_validator

from app import enums
from ...base import SchemaBase


class __MovableDayBase(SchemaBase):
    abbr: enums.MovableDayAbbr
    abbr_ru: enums.MovableDayAbbrRu
    title: str | None = None  # constr(strip_whitespace=True, strict=True, max_length=30) | None = None


class MovableDayCreate(__MovableDayBase):

    @model_validator(mode='before')
    def set_abbr_ru(cls, values: dict[str, Any]) -> dict[str, Any]:
        values['abbr_ru']: enums.MovableDayAbbrRu = enums.MovableDayAbbrRu[values['abbr'].name]
        return values
