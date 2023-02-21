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
        if not const.REGEX_YEAR_TITLE_.match(year_title):
            raise ValueError(f'{year_title} not valid year')
        self.__year_title = year_title

    @classmethod
    def _offset_years(cls, year_title: str) -> str:
        for year in map(int, re.findall(r'\d+', year_title)):
            year_title = year_title.replace(f'{year}', f'{year + const.NUM_OFFSET_YEARS}')
        return year_title

    @classmethod
    def _prepare_сlarification_year(cls, year_title: str) -> str:
        year_title = year_title[0].upper() + year_title[1:]
        year_title = cls.__replace_to_one_text(year_title, ['Ок.'], const.YearСlarification.okolo)
        year_title = cls.__replace_to_one_text(year_title, ['Нач.'], const.YearСlarification.nachalo)
        year_title = cls.__replace_to_one_text(year_title, ['Кон.'], const.YearСlarification.konets)
        year_title = cls.__replace_to_one_text(year_title, ['Серед.', 'Серед', 'Сер'], const.YearСlarification.seredina)
        year_title = cls.__replace_to_one_text(year_title, ['Пер'], 'Первая')
        year_title = cls.__replace_to_one_text(year_title, ['Посл.'], 'Последняя')
        year_title = cls.__replace_to_one_text(year_title, ['Перв', 'Пер'], 'Первая')
        year_title = cls.__replace_to_one_text(year_title, ['Втор.'], 'Вторая')
        year_title = cls.__replace_to_one_text(year_title, ['пол.', 'пол'], 'половина')
        return year_title

    @classmethod
    def _remove_abbrs_from_end(cls, year_title: str) -> str:
        for abbr in [
            'года',
            'гг.', 'гг', 'г.', ' ' + 'г',
            'вв.', 'вв', 'в.', ' ' + 'в',
        ]:
            if abbr in year_title and year_title[-len(abbr):] == abbr:
                year_title = year_title.replace(abbr, '')
        year_title = year_title.strip()
        return year_title

    @classmethod
    def _clean_spaces(cls, year_title: str) -> str:
        year_title = year_title.replace('  ', '')
        year_title = year_title.strip()
        return year_title

    @staticmethod
    def __replace_to_one_text(year_title: str, texts: list[str], prepare_text: const.YearСlarification | str) -> str:
        if prepare_text in year_title:
            return year_title
        for clarification in texts:
            if clarification in year_title:
                year_title = year_title.replace(clarification, prepare_text)
                break
        return year_title
