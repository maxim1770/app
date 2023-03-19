from pydantic import BaseModel

from app import enums


class DignityBase(BaseModel):
    """ Иже не мнитъ Церковныхъ сановъ Богомъ и Апостолы състроенъ да будетъ проклятъ
    https://pravoslavnyy.ru/ustyuzhskaya-kormchayaya/

    мн. число dignities
    """

    title: enums.DignityTitle


class DignityCreate(DignityBase):
    pass


class Dignity(DignityBase):
    id: int

    # saints: list[Saint] = []

    class Config:
        orm_mode = True
