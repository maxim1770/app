from pydantic import BaseModel, Field, conint


class YearBase(BaseModel):
    title: str
    year: conint(strict=True, ge=1, le=7100) = Field(..., alias='_year')


class YearCreate(YearBase):
    pass


class Year(YearBase):
    id: int

    class Config:
        orm_mode = True
