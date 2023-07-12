from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __FundBase(SchemaBase):
    title: enums.FundTitle | None = None
    library: enums.LibraryTitle | None = None


class FundCreate(__FundBase):
    title: enums.FundTitle
    library: enums.LibraryTitle


class FundUpdate(__FundBase):
    pass


class Fund(__FundBase, SchemaInDBBase):
    pass
