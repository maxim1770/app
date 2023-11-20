from .base import SchemaInDBToAssociationBase
from .date import Date


class MainInDB(SchemaInDBToAssociationBase):
    date: Date
