from pydantic import model_validator

from app import enums, models
from ..base import SchemaBase, SchemaInDBBase


class __TipikonBase(SchemaBase):
    title: enums.TipikonTitle | None = None


class TipikonCreate(__TipikonBase):
    title: enums.TipikonTitle


class TipikonUpdate(__TipikonBase):
    pass


class Tipikon(__TipikonBase, SchemaInDBBase):
    title_en: str

    @model_validator(mode='before')
    @classmethod
    def prepare_title_en(cls, values: models.Tipikon) -> models.Tipikon:
        values.title_en = values.title.name
        return values
