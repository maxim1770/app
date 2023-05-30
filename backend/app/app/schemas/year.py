from math import ceil
from statistics import mean

from pydantic import BaseModel, root_validator
from roman import fromRoman

from app import const


class YearBase(BaseModel):
    title: str
    year: int = None


class YearCreate(YearBase):

    @root_validator
    def check_and_compute_year(cls, values):
        title: str = values['title']

        if 'от Адама' in title:
            values['year'] = int(const.YearRegex.YEAR.search(title)[0])
            return values

        if not const.YearRegex.YEAR_TITLE.match(title):
            raise ValueError(f'{title} not valid year')

        years: list[int] = list(map(lambda groups: int(groups[0]), const.YearRegex.YEAR_BEFORE_1600.findall(title)))
        if years:
            year = ceil(mean(years))
            year_max = max(years)

            if title.isdigit():
                pass
            elif title.endswith('-е'):
                year += 5
                year_max += 9
            elif title.startswith(const.YearCorrection.do):
                year += const.NumYearCorrection.do
            elif title.startswith(const.YearCorrection.okolo):
                year_max += const.NumYearCorrection.okolo
            elif title.startswith(const.YearCorrection.posle):
                year_max += const.NumYearCorrection.posle
                year += const.NumYearCorrection.posle - 10

            if year_max >= const.YEAR_HERESY:
                raise ValueError(f'year > {const.YEAR_HERESY}')
        else:
            centuries: list[int] = list(map(fromRoman, const.YearRegex.CENTURY_BEFORE_XVI.findall(title)))
            year = int(mean(centuries) * const.NUM_YEARS_IN_CENTURY) - 50

            for century_correction in const.CenturyCorrection:
                if title.startswith(century_correction + ' '):
                    year += const.NumCenturyCorrection[century_correction.name]
                    break

            year += const.NUM_OFFSET_YEARS

            if year >= const.YEAR_HERESY:
                raise ValueError(f'year > {const.YEAR_HERESY}')

        year += const.YEAR_CHRISTMAS

        values['year'] = year
        return values


class Year(YearBase):
    id: int

    class Config:
        orm_mode = True
