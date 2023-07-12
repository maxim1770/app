from app import enums
from ..base import SchemaBase, SchemaInDBBase


class __DignityBase(SchemaBase):
    """ Иже не мнитъ Церковныхъ сановъ Богомъ и Апостолы състроенъ да будетъ проклятъ
    https://pravoslavnyy.ru/ustyuzhskaya-kormchayaya/

    мн. число dignities
    """
    title: enums.DignityTitle | None = None


class DignityCreate(__DignityBase):
    title: enums.DignityTitle


class DignityUpdate(__DignityBase):
    pass


class Dignity(__DignityBase, SchemaInDBBase):
    pass
