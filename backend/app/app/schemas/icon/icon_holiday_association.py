from __future__ import annotations

from typing import TYPE_CHECKING

from ..base import SchemaBase, SchemaInDBToAssociationBase

if TYPE_CHECKING:
    from .icon import IconInDB
    from ..holiday import HolidayInDB


class __IconHolidayAssociationBase(SchemaBase):
    is_use_slug: bool | None = None


class IconHolidayAssociationCreate(__IconHolidayAssociationBase):
    pass


class __IconHolidayAssociationInDBBase(__IconHolidayAssociationBase, SchemaInDBToAssociationBase):
    pass


class IconHolidayAssociation(__IconHolidayAssociationInDBBase):
    holiday: HolidayInDB


class IconHolidayAssociationInDB(__IconHolidayAssociationInDBBase):
    icon: IconInDB
