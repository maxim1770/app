from pydantic import BaseModel

from app import enums


class CityBase(BaseModel):
    title: enums.CityTitle


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        orm_mode = True
