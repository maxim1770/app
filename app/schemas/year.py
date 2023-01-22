from pydantic import BaseModel, Field, conint, constr

from app.const import REGEX_YEAR_TITLE_STR


class YearBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, regex=REGEX_YEAR_TITLE_STR)
    year: conint(strict=True, ge=1, le=7100) = Field(..., alias='_year')


class YearCreate(YearBase):
    pass


class Year(YearBase):
    id: int

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True
