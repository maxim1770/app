from typing import Any

from pydantic import model_validator

from app import enums
from app.schemas.base import SchemaBase


class __BibleBookBase(SchemaBase):
    testament: enums.BibleBookTestament | None = None
    testament_ru: enums.BibleBookTestamentRu | None = None
    part: enums.BibleBookPart | None = None
    part_ru: enums.BibleBookPartRu | None = None
    title: str | None = None  # constr(strip_whitespace=True, strict=True, max_length=50)
    abbr: enums.BibleBookAbbr | None = None
    abbr_ru: enums.BibleBookAbbrRu | None = None


class BibleBookCreate(__BibleBookBase):
    testament: enums.BibleBookTestament
    testament_ru: enums.BibleBookTestamentRu
    title: str
    abbr: enums.BibleBookAbbr
    abbr_ru: enums.BibleBookAbbrRu

    @model_validator(mode='before')
    @classmethod
    def set_abbr_ru(cls, values: dict[str, Any]) -> dict[str, Any]:
        values['abbr_ru']: enums.BibleBookAbbrRu = enums.BibleBookAbbrRu[values['abbr'].name]
        return values


class BibleBookUpdate(__BibleBookBase):
    pass


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
