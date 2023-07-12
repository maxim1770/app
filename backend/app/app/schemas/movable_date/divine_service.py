from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __DivineServiceBase(SchemaBase):
    title: enums.DivineServiceTitle


class DivineServiceCreate(__DivineServiceBase):
    pass


class DivineService(__DivineServiceBase, SchemaInDBBase):
    pass
