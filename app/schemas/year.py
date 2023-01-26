from math import ceil
from statistics import mean

from pydantic import BaseModel, Field, root_validator
from roman import fromRoman

from app import const
from app.create import const as create_const


class YearBase(BaseModel):
    title: str
    year: int = Field(None, alias='_year')


class YearCreate(YearBase):

    @root_validator
    def compute_year(cls, values):
        title: str = values['title']
        if const.REGEX_YEAR_TITLE.match(title) is None:
            raise ValueError(f'year_title >16: {title}')

        years: list[int] = list(map(lambda groups: int(groups[0]), const.REGEX_YEAR_BEFORE_1600.findall(title)))
        if years:
            _year = ceil(mean(years))
            _year_max = max(years)

            if 'до' in title:
                _year -= 15
            if 'ок.' in title:
                _year_max += 15
            if 'после' in title:
                _year_max += 25
                _year += 15

            if _year_max >= create_const.YEAR_HERESY:
                raise ValueError(f'year > {create_const.YEAR_HERESY}')
        else:
            roman_centuries: list[int] = list(map(fromRoman, const.REGEX_ROMAN_CENTURY_BEFORE_16.findall(title)))
            _year = int(mean(roman_centuries) * create_const.NUM_YEARS_IN_CENTURY) - 50

            if 'до' in title:
                _year -= 50
            if 'после' in title:
                _year += 50

            _year += create_const.NUM_OFFSET_YEARS

            if _year >= create_const.YEAR_HERESY:
                raise ValueError(f'year > {create_const.YEAR_HERESY}')

        _year += create_const.YEAR_CHRISTMAS

        values['year'] = _year
        return values


class Year(YearBase):
    id: int

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True
