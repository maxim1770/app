from app import enums
from .base import SchemaBase, SchemaInDBBase


class __CityBase(SchemaBase):
    title: enums.CityTitle | None = None


class CityCreate(__CityBase):
    title: enums.CityTitle


class CityUpdate(__CityBase):
    pass


class City(__CityBase, SchemaInDBBase):
    pass
