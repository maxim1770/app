from pydantic import BaseModel, Field, conint, constr


class YearBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, max_length=30)
    year: conint(strict=True, ge=1, le=7100) = Field(..., alias='_year')


class YearCreate(YearBase):
    pass


class Year(YearBase):
    id: int

    class Config:
        orm_mode = True
