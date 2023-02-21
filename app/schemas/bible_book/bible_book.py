from pydantic import BaseModel, constr, validator

from app import enums
from .zachalo import Zachalo


class BibleBookBase(BaseModel):
    testament: enums.BibleBookTestament
    testament_ru: enums.BibleBookTestamentRu
    part: enums.BibleBookPart
    part_ru: enums.BibleBookPartRu
    title: constr(strip_whitespace=True, strict=True, max_length=50)
    abbr: enums.BibleBookAbbr
    abbr_ru: enums.BibleBookAbbrRu | None = None


class BibleBookCreate(BibleBookBase):

    @validator('abbr_ru', pre=True, always=True)
    def set_abbr_ru(cls, abbr_ru: None, values):
        abbr_ru: enums.BibleBookAbbrRu = enums.BibleBookAbbrRu[values['abbr'].name]
        return abbr_ru


class BibleBookNewTestamentCreate(BibleBookCreate):
    testament: enums.BibleBookTestament = enums.BibleBookTestament.new_testament
    testament_ru: enums.BibleBookTestamentRu = enums.BibleBookTestamentRu.new_testament


class BibleBookEvangelCreate(BibleBookNewTestamentCreate):
    part: enums.BibleBookPart = enums.BibleBookPart.evangel
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.evangel


class BibleBookApostleCreate(BibleBookNewTestamentCreate):
    part: enums.BibleBookPart = enums.BibleBookPart.apostle
    part_ru: enums.BibleBookPartRu = enums.BibleBookPartRu.apostle


class BibleBook(BibleBookBase):
    zachalos: list[Zachalo] = []

    abbr_ru: enums.BibleBookAbbrRu

    class Config:
        orm_mode = True
