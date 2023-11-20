from pydantic import computed_field

from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __TipikonBase(SchemaBase):
    title: enums.TipikonTitle | None = None
    priority: enums.TipikonPriority | None = None


class TipikonCreate(__TipikonBase):
    title: enums.TipikonTitle
    priority: enums.TipikonPriority


class TipikonUpdate(__TipikonBase):
    pass


class Tipikon(__TipikonBase, SchemaInDBBase):

    @computed_field
    @property
    def title_en(self) -> str:
        return self.title.name
