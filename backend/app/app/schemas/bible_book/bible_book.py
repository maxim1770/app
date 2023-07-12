from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

from pydantic import model_validator

from app import enums
from ..base import SchemaBase, SchemaInDBBase
from ..manuscript import ManuscriptInDB

if TYPE_CHECKING:
    from .zachalo import ZachaloInDBToBibleBook


class __BibleBookBase(SchemaBase):
    testament: enums.BibleBookTestament
    testament_ru: enums.BibleBookTestamentRu
    part: enums.BibleBookPart | None = None
    part_ru: enums.BibleBookPartRu | None = None
    title: str  # constr(strip_whitespace=True, strict=True, max_length=50)
    abbr: enums.BibleBookAbbr
    abbr_ru: enums.BibleBookAbbrRu


class BibleBookCreate(__BibleBookBase):

    @model_validator(mode='before')
    @classmethod
    def set_abbr_ru(cls, values: dict[str, Any]) -> dict[str, Any]:
        values['abbr_ru']: enums.BibleBookAbbrRu = enums.BibleBookAbbrRu[values['abbr'].name]
        return values


class __BibleBookNewTestamentCreateBase(BibleBookCreate):
    testament: enums.BibleBookTestament = enums.BibleBookTestament.new_testament
    testament_ru: enums.BibleBookTestamentRu = enums.BibleBookTestamentRu.new_testament


class BibleBookOldTestamentCreate(BibleBookCreate):
    testament: enums.BibleBookTestament = enums.BibleBookTestament.old_testament
    testament_ru: enums.BibleBookTestamentRu = enums.BibleBookTestamentRu.old_testament


class BibleBookEvangelCreate(__BibleBookNewTestamentCreateBase):
    part: enums.BibleBookPart = enums.BibleBookPart.evangel
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.evangel


class BibleBookApostleCreate(__BibleBookNewTestamentCreateBase):
    part: enums.BibleBookPart = enums.BibleBookPart.apostle
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.apostle


class BibleBookPsaltyrCreate(BibleBookOldTestamentCreate):
    part: enums.BibleBookPart = enums.BibleBookPart.psaltyr
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.psaltyr


class BibleBookPjatiknizhieMoisejaCreate(BibleBookOldTestamentCreate):
    part: enums.BibleBookPart = enums.BibleBookPart.pjatiknizhie_moiseja
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.pjatiknizhie_moiseja


class BibleBook(__BibleBookBase, SchemaInDBBase):
    manuscripts: list[ManuscriptInDB] = []
    zachalos: list[ZachaloInDBToBibleBook] = []
