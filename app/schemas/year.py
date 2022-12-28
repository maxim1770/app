from pydantic import BaseModel, Field


class YearBase(BaseModel):
    title: str
    year: int = Field(..., alias='_year')

    # class Config:
    #     fields = {'year': '_year'}


class YearCreate(YearBase):
    pass


class Year(YearBase):
    id: int

    class Config:
        orm_mode = True
