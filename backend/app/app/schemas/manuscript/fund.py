from pydantic import BaseModel

from app import enums


class FundBase(BaseModel):
    title: enums.FundTitle
    library: enums.LibraryTitle


class FundCreate(FundBase):
    pass


class Fund(FundBase):
    id: int

    class Config:
        orm_mode = True
