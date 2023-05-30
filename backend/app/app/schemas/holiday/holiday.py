from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import BaseModel, constr, validator, root_validator

from app import const, enums
from .holiday_category import HolidayCategory
from ..book import HolidayBook, MolitvaBook
from ..icon import Icon
from ..saint import SaintInDBToHoliday, SaintCreate
from ..year import Year, YearCreate

if TYPE_CHECKING:
    from ..movable_date import MovableDayInDB, MovableDayGet
    from ..day import DayCreate, DayInDB


class __HolidayBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=200) | None = None
    slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR) | None = None


class HolidayCreate(__HolidayBase):
    title: constr(strip_whitespace=True, strict=True, max_length=200)
    slug: constr(strip_whitespace=True, strict=True, max_length=200, regex=const.REGEX_SLUG_STR)


class HolidayUpdate(__HolidayBase):
    pass


class __HolidayInDBBase(__HolidayBase):
    id: int

    title: str
    slug: str

    holiday_category: HolidayCategory

    year: Year | None
    icons: list[Icon] = []

    @validator('icons', pre=True, always=True)
    def prepare_icons(cls, icons: list[Icon], values):
        try:
            holiday_slug: str = values['slug']
            for icon in icons:
                icon_id = f'pravicon-{icon.pravicon_id}' if icon.pravicon_id else None
                if not icon_id:
                    icon_id = f'gallerix-{icon.gallerix_id}' if icon.gallerix_id else None
                if not icon_id:
                    icon_id = f'shm-{icon.shm_id}' if icon.shm_id else None
                icon.path = Path(f'img/icons/{holiday_slug}/{icon_id}.webp')
        except FileNotFoundError:
            return []
        else:
            return icons

    class Config:
        orm_mode = True


class __HolidayInDBWithDayBase(__HolidayInDBBase):
    day: DayInDB | None


class __HolidayInDBWithSaintsBase(__HolidayInDBBase):
    saints: list[SaintInDBToHoliday] = []

    title_in_dative: str | None = None

    @root_validator
    def prepare_title_in_dative(cls, values):
        names_in_dative: set[str] = {saint.name_in_dative for saint in values['saints'] if saint.name_in_dative}
        if len(names_in_dative) == 1:
            values['title_in_dative'] = names_in_dative.pop()
            return values
        elif names_in_dative:
            values['title_in_dative'] = ' и '.join(names_in_dative)
            return values
        return values


class HolidayInDBToDay(__HolidayInDBWithSaintsBase):
    pass


class HolidayInDBToSaint(__HolidayInDBWithDayBase):
    pass


class Holiday(__HolidayInDBWithDayBase, __HolidayInDBWithSaintsBase):
    movable_day: MovableDayInDB | None
    holiday_books: list[HolidayBook] = []
    molitva_books: list[MolitvaBook] = []


class HolidayInDB(__HolidayInDBWithDayBase, __HolidayInDBWithSaintsBase):
    pass


class HolidayCreateBase(BaseModel):
    holiday_in: HolidayCreate
    holiday_category_title: enums.HolidayCategoryTitle
    year_in: YearCreate


class HolidayDataCreate(HolidayCreateBase):
    day_in: DayCreate


class SaintsHolidayCreateBase(HolidayCreateBase):
    saints_in: list[SaintCreate]


class SaintHolidayCreateBase(HolidayCreateBase):
    saint_in: SaintCreate


class SaintHolidayCreate(SaintHolidayCreateBase):
    day_in: DayCreate


class SaintHolidayCreateWithoutYear(SaintHolidayCreateBase):
    year_in: YearCreate | None = None
    day_in: DayCreate


class SaintsHolidayCreate(SaintsHolidayCreateBase):
    day_in: DayCreate
    year_in: YearCreate | None = None


class MovableSaintHolidayCreate(SaintHolidayCreateBase):
    movable_day_get: MovableDayGet


class MovableSaintHolidayCreateWithoutData(BaseModel):
    movable_day_get: MovableDayGet
    saint_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR)
