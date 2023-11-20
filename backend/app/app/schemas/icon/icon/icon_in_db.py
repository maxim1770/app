from pathlib import Path

from pydantic import computed_field, model_validator

from app import const, models
from .icon import __IconBase
from ..icon_holiday_association import IconHolidayAssociation
from ...base import SchemaInDBBase
from ...city import City
from ...year import Year


class __IconInDBBase(SchemaInDBBase):
    path: Path

    @model_validator(mode='before')
    @classmethod
    def prepare_path(cls, values: models.Icon) -> models.Icon:
        __holiday_slug: str = next((
            icon_holiday_association.holiday.slug for icon_holiday_association in values.holidays
            if icon_holiday_association.is_use_slug
        ))
        if pravicon_id := values.pravicon_id:
            icon_library_str_id = f'pravicon-{pravicon_id}'
        elif gallerix_id := values.gallerix_id:
            icon_library_str_id = f'gallerix-{gallerix_id}'
        elif shm_id := values.shm_id:
            icon_library_str_id = f'shm-{shm_id}'
        values.path = Path(f'img/icons/{__holiday_slug}/{icon_library_str_id}.webp')
        return values


class Icon(__IconInDBBase, __IconBase):
    desc: str

    year: Year
    city: City | None

    holidays: list[IconHolidayAssociation] = []

    @computed_field
    @property
    def url(self) -> str:
        if pravicon_id := self.pravicon_id:
            return const.PraviconUrl.GET_ICON_DATA.replace(
                const.PraviconUrl.SOME_ICON_ID, str(pravicon_id)
            )
        elif gallerix_id := self.gallerix_id:
            return const.GallerixUrl.GET_ICON_DATA.replace(
                const.GallerixUrl.SOME_ICON_ID, str(gallerix_id)
            )
        elif shm_id := self.shm_id:
            return const.ShmUrl.GET_ITEM_DATA.replace(
                const.ShmUrl.SOME_ITEM_ID, str(shm_id)
            )


class IconInDB(__IconInDBBase):
    pass
