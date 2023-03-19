import re

from app import const


class PrepareYearTitle(object):

    def __init__(self, year_title: str):
        year_title = self._clean_spaces(year_title)
        year_title = self._remove_abbrs_from_end(year_title)
        year_title = self._prepare_сlarification_year(year_title)
        year_title = self._offset_years(year_title)
        self.year_title = year_title

    @property
    def year_title(self) -> str:
        return self.__year_title

    @year_title.setter
    def year_title(self, year_title: str):
        if not const.YearRegex.YEAR_TITLE.match(year_title):
            raise ValueError(f'{year_title} not valid year')
        self.__year_title = year_title

    @classmethod
    def _offset_years(cls, year_title: str) -> str:
        to_ten: int = 2 if year_title.endswith('-е') else 0
        for year in map(int, re.findall(r'\d+', year_title)):
            year_title = year_title.replace(f'{year}', f'{year + const.NUM_OFFSET_YEARS + to_ten}')
        return year_title

    @classmethod
    def _prepare_сlarification_year(cls, year_title: str) -> str:
        year_title = year_title[0].upper() + year_title[1:]
        year_title = cls.__replace_to_one_text(year_title, ['Ок.'], const.CenturyCorrection.okolo)
        year_title = cls.__replace_to_one_text(year_title, ['Нач.'], const.CenturyCorrection.nachalo)
        year_title = cls.__replace_to_one_text(year_title, ['Кон.'], const.CenturyCorrection.konets)
        year_title = cls.__replace_to_one_text(year_title, ['Серед.', 'Серед', 'Сер'],
                                               const.CenturyCorrection.seredina
                                               )
        year_title = cls.__replace_to_one_text(year_title, ['Посл.'], 'Последняя')
        year_title = cls.__replace_to_one_text(year_title, ['Перв.', 'Перв', 'Пер'], 'Первая')
        year_title = cls.__replace_to_one_text(year_title, ['Втор.'], 'Вторая')
        year_title = cls.__replace_to_one_text(year_title, ['пол.', 'пол'], 'половина')
        year_title = cls.__replace_to_one_text(year_title, ['четв.'], 'четверть')
        return year_title

    @classmethod
    def _remove_abbrs_from_end(cls, year_title: str) -> str:
        for abbr in [
            'года',
            'гг.', 'гг', 'г.', 'г',
            'вв.', 'вв', 'в.', 'в',
        ]:
            if year_title.endswith(abbr):
                year_title = year_title.replace(' ' + abbr, '')
                year_title = year_title.strip()
                break
        return year_title

    @classmethod
    def _clean_spaces(cls, year_title: str) -> str:
        year_title = year_title.replace('  ', '')
        year_title = year_title.replace('–', '-').replace(' -', '-').replace('- ', '-')
        year_title = year_title.strip()
        return year_title

    @staticmethod
    def __replace_to_one_text(year_title: str, texts: list[str], prepared_text: const.CenturyCorrection | str) -> str:
        if prepared_text in year_title:
            return year_title
        for correction in texts:
            if correction + ' ' in year_title:
                year_title = year_title.replace(correction, prepared_text)
                break
        return year_title
