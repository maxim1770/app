from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __HolidayCategoryBase(SchemaBase):
    title: enums.HolidayCategoryTitle | None = None


class HolidayCategoryCreate(__HolidayCategoryBase):
    title: enums.HolidayCategoryTitle


class HolidayCategoryUpdate(__HolidayCategoryBase):
    pass


class HolidayCategory(__HolidayCategoryBase, SchemaInDBBase):
    pass
