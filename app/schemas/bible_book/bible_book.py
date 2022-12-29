from pydantic import BaseModel, Field, root_validator

from app import enums
from app.schemas.bible_book.zachalo import Zachalo


class BibleBookBase(BaseModel):
    testament: enums.BibleBookTestament
    testament_ru: enums.BibleBookTestamentRu
    part: enums.BibleBookPart
    part_ru: enums.BibleBookPartRu = Field(description="Н: Евангелие/Апостол/Пятикнижие/...")
    title: str
    abbr: enums.BibleBookAbbr
    abbr_ru: enums.BibleBookAbbrRu


class BibleBookCreate(BibleBookBase):
    abbr_ru: enums.BibleBookAbbrRu | None

    # С этим не получилось создать записи из пакета create
    # @validator('abbr_ru')
    # def _set_abbr_ru(cls, field_value, values: dict, field, config):
    #     field = enums.BibleBookAbbrRu[values["abbr"]]
    #     return field

    @root_validator()
    def _set_abbr_ru(cls, values: dict) -> dict:
        values["abbr_ru"] = enums.BibleBookAbbrRu[values["abbr"].name]
        return values


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

    class Config:
        orm_mode = True
