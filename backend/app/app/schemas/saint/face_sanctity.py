from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __FaceSanctityBase(SchemaBase):
    title: enums.FaceSanctityTitle | None = None


class FaceSanctityCreate(__FaceSanctityBase):
    title: enums.FaceSanctityTitle


class FaceSanctityUpdate(__FaceSanctityBase):
    pass


class FaceSanctity(__FaceSanctityBase, SchemaInDBBase):
    pass
