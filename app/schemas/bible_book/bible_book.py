from enum import Enum, auto

from fastapi_utils.enums import StrEnum
from pydantic import BaseModel, Field, root_validator, validator

from app.schemas.bible_book.zachalo import Zachalo


class TestamentEnum(StrEnum):
    """OT - Old Testament, NT - New Testament"""
    new_testament = auto()
    old_testament = auto()


class TestamentRuEnum(str, Enum):
    """OT - Old Testament, NT - New Testament"""
    new_testament = 'Новый завет'
    old_testament = 'Ветхий завет'


class PartEnum(StrEnum):
    evangel = auto()
    apostle = auto()


class PartRuEnum(str, Enum):
    evangel = 'Евангелие'
    apostle = 'Апостол'


class AbbrEnum(StrEnum):
    # Евангелие
    Mk = auto()
    Mt = auto()
    Lk = auto()
    Jn = auto()

    # Деяния святых Апостолов
    Act = auto()

    # Соборные Послания
    Jac = auto()
    _1Pet = '1Pet'
    _2Pet = '2Pet'
    _1Jn = '1Jn'
    _2Jn = '2Jn'
    _3Jn = '3Jn'
    Juda = auto()

    # Послания Апостола Павла
    Rom = auto()
    _1Cor = '1Cor'
    _2Cor = '2Cor'
    Gal = auto()
    Eph = auto()
    Phil = auto()
    Col = auto()
    _1Thes = '1Thes'
    _2Thes = '2Thes'
    _1Tim = '1Tim'
    _2Tim = '2Tim'
    Tit = auto()
    Phlm = auto()
    Hebr = auto()

    # Апокалипсис
    Apok = auto()


class AbbrRuEnum(str, Enum):
    # Евангелие
    Jn = 'Ин'
    Lk = 'Лк'
    Mk = 'Мк'
    Mt = 'Мф'

    # Деяния святых Апостолов
    Act = 'Деян'

    # Соборные Послания
    Jac = 'Иак'
    _1Pet = '1 Пет'
    _2Pet = '2 Пет'
    _1Jn = '1 Ин'
    _2Jn = '2 Ин'
    _3Jn = '3 Ин'
    Juda = 'Иуд'

    # Послания Апостола Павла
    Rom = 'Рим'
    _1Cor = '1 Кор'
    _2Cor = '2 Кор'
    Gal = 'Гал'
    Eph = 'Еф'
    Phil = 'Флп'
    Col = 'Кол'
    # А тут https://azbyka.ru/biblia/?1Thes.1&r написано не '1 Сол', a '1 Фес' (написано, вверху в меню)
    _1Thes = '1 Сол'
    # Так же, написано не '2 Сол', а '2 Фес'
    _2Thes = '2 Сол'
    _1Tim = '1 Тим'
    _2Tim = '2 Тим'
    Tit = 'Тит'
    # НЕ ЧИТАЕТСЯ ПО ДНЯМ
    Phlm = 'Флм'
    Hebr = 'Евр'

    # Апокалипсис
    # НЕ ЧИТАЕТСЯ ПО ДНЯМ
    Apok = 'Откр'


class BibleBookBase(BaseModel):
    testament: TestamentEnum
    testament_ru: TestamentRuEnum
    part: PartEnum
    part_ru: PartRuEnum = Field(description="Н: Евангелие/Апостол/Пятикнижие/...")
    title: str
    abbr: AbbrEnum
    abbr_ru: AbbrRuEnum


class BibleBookCreate(BibleBookBase):
    abbr_ru: AbbrRuEnum | None

    # С этим не получилось создать записи из пакета pars
    # @validator('abbr_ru')
    # def _set_abbr_ru(cls, field_value, values: dict, field, config):
    #     field = AbbrRuEnum[values["abbr"]]
    #     return field

    @root_validator()
    def _set_abbr_ru(cls, values: dict) -> dict:
        values["abbr_ru"] = AbbrRuEnum[values["abbr"].name]
        return values


class BibleBookNewTestamentCreate(BibleBookCreate):
    testament: TestamentEnum = TestamentEnum.new_testament
    testament_ru: TestamentRuEnum = TestamentRuEnum.new_testament


class BibleBookEvangelCreate(BibleBookNewTestamentCreate):
    part: PartEnum = PartEnum.evangel
    part_ru: PartRuEnum = PartRuEnum.evangel


class BibleBookApostleCreate(BibleBookNewTestamentCreate):
    part: PartEnum = PartEnum.apostle
    part_ru: PartRuEnum = PartRuEnum.apostle


class BibleBook(BibleBookBase):
    zachalos: list[Zachalo] = []

    class Config:
        orm_mode = True
