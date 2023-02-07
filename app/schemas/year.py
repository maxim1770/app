from math import ceil
from statistics import mean

from pydantic import BaseModel, Field, root_validator
from roman import fromRoman

from app import const


class YearBase(BaseModel):
    title: str
    year: int = Field(None, alias='_year')


class YearCreate(YearBase):

    @root_validator
    def check_and_compute_year(cls, values):
        title: str = values['title']

        if 'от Адама' in title:
            values['year'] = int(const.REGEX_YEAR.search(title)[0])
            return values

        if not const.REGEX_YEAR_TITLE.match(title):
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

            if _year_max >= const.YEAR_HERESY:
                raise ValueError(f'year > {const.YEAR_HERESY}')
        else:
            roman_centuries: list[int] = list(map(fromRoman, const.REGEX_ROMAN_CENTURY_BEFORE_16.findall(title)))
            _year = int(mean(roman_centuries) * const.NUM_YEARS_IN_CENTURY) - 50

            if 'до' in title:
                _year -= 50
            if 'после' in title:
                _year += 50

            _year += const.NUM_OFFSET_YEARS

            if _year >= const.YEAR_HERESY:
                raise ValueError(f'year > {const.YEAR_HERESY}')

        _year += const.YEAR_CHRISTMAS

        values['year'] = _year
        return values


class Year(YearBase):
    id: int

    # holidays: list[Holiday] = []

    class Config:
        orm_mode = True
