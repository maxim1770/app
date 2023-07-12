from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pydantic import model_validator

from app import models, enums
from .holiday import __HolidayBase
from ..holiday_category import HolidayCategory
from ..tipikon import Tipikon
from ...base import SchemaInDBBase, SchemaInDBToAssociationBase
from ...book import HolidayBook, MolitvaBook
from ...icon import IconInDB
from ...saint import SaintInDBToHoliday
from ...year import Year

if TYPE_CHECKING:
    from ...movable_date import MovableDayInDB
    from ...day import DayInDB
    from ..before_after_holiday import BeforeAfterHoliday


class __HolidayInDBBase(__HolidayBase, SchemaInDBBase):
    title: str
    slug: str

    holiday_category: HolidayCategory
    tipikon: Tipikon | None

    year: Year | None


class __HolidayInDBWithDayBase(__HolidayInDBBase):
    day: DayInDB | None


class __HolidayInDBWithMovableDayBase(__HolidayInDBBase):
    movable_day: MovableDayInDB | None


class __HolidayInDBWithSaintsBase(__HolidayInDBBase):
    saints: list[SaintInDBToHoliday] = []

    title_in_dative: str | None

    @model_validator(mode='before')
    @classmethod
    def prepare_title_in_dative(cls, values: models.Holiday) -> models.Holiday:
        names_in_dative: set[str] = {saint.name_in_dative for saint in values.saints if saint.name_in_dative}
        if len(names_in_dative) == 1:
            values.title_in_dative = names_in_dative.pop()
        elif names_in_dative:
            values.title_in_dative = ' и '.join(names_in_dative)
        else:
            values.title_in_dative = None
        return values


class __HolidayInDBWithIconsBase(__HolidayInDBBase):
    icons: list[IconInDB] = []

    @model_validator(mode='before')
    @classmethod
    def prepare_icons_paths(cls, values: models.Holiday) -> models.Holiday:
        holiday_slug: str = values.slug
        for icon in values.icons:
            if isinstance(icon, dict):
                if not icon['path']:
                    if pravicon_id := icon.get('pravicon_id'):
                        icon_library_str_id = f'pravicon-{pravicon_id}'
                    elif gallerix_id := icon.get('gallerix_id'):
                        icon_library_str_id = f'gallerix-{gallerix_id}'
                    elif shm_id := icon.get('shm_id'):
                        icon_library_str_id = f'shm-{shm_id}'
                    icon['path']: Path = Path(f'img/icons/{holiday_slug}/{icon_library_str_id}.webp')
            else:
                if pravicon_id := icon.pravicon_id:
                    icon_library_str_id = f'pravicon-{pravicon_id}'
                elif gallerix_id := icon.gallerix_id:
                    icon_library_str_id = f'gallerix-{gallerix_id}'
                elif shm_id := icon.shm_id:
                    icon_library_str_id = f'shm-{shm_id}'
                icon.path: Path = Path(f'img/icons/{holiday_slug}/{icon_library_str_id}.webp')
        return values


class HolidayInDBToDay(__HolidayInDBWithSaintsBase):
    pass


class HolidayInDBToMovableDay(__HolidayInDBWithSaintsBase):
    pass


class HolidayInDBToSaint(__HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithIconsBase):
    pass


class HolidayInDBToIcon(__HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithSaintsBase):
    pass


class Holiday(
    __HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithSaintsBase, __HolidayInDBWithIconsBase
):
    holiday_books: list[HolidayBook] = []
    molitva_books_: dict[str, list[MolitvaBook]] | None
    before_after_holiday: BeforeAfterHoliday | None
    before_after_holidays: list[BeforeAfterHoliday] = []

    @model_validator(mode='before')
    @classmethod
    def structure_molitva_books_by_manuscript(cls, values: models.Holiday) -> models.Holiday:
        manuscript_molitva_books: dict[str, list[MolitvaBook]] = {}
        for molitva_book in values.molitva_books:
            try:
                manuscript_molitva_books[molitva_book.book.bookmarks[0].manuscript.code].append(molitva_book)
            except KeyError:
                manuscript_molitva_books[molitva_book.book.bookmarks[0].manuscript.code] = [molitva_book]
        values.molitva_books_ = manuscript_molitva_books if manuscript_molitva_books else None
        return values


class HolidayInDB(__HolidayInDBWithDayBase, __HolidayInDBWithMovableDayBase, __HolidayInDBWithIconsBase):
    pass


class HolidayWithData(SchemaInDBToAssociationBase):
    holiday: Holiday
    tipikon_titles: list[enums.TipikonTitle] = list(enums.TipikonTitle)
