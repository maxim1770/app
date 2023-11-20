from __future__ import annotations

from typing import Any

from pydantic import field_validator, BaseModel, conint, constr, model_validator
from pydantic_extra_types.color import Color

from app import const


class FitSchema(BaseModel):
    left: float
    top: float
    zoom: float

    @field_validator('zoom')
    @classmethod
    def round_zoom(cls, zoom: float) -> float:
        return round(zoom, 3)


class __PdfBookmarkBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=620)
    page_num: conint(strict=True, ge=0, le=3000)
    color: Color | None = None


class PdfBookmark(__PdfBookmarkBase):
    fit: FitSchema | None = None
    children: list[PdfBookmark] = []
    parent: PdfBookmark | None = None
    start_on_new_page: bool | None = None


class __LlsYearBookmark(PdfBookmark):
    year: int

    @model_validator(mode='before')
    @classmethod
    def prepare_title(cls, values: dict[str | Any]) -> dict[str | Any]:
        year: int = values['year']
        values['title']: str = f'В лето {year} ({year - const.YEAR_CHRISTMAS})'
        return values
