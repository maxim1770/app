import re
import urllib.parse
from typing import Pattern
from uuid import UUID

import requests
from bs4 import BeautifulSoup, Tag
from roman import fromRoman

from app import const
from .collect_manuscript_data import CollectManuscriptDataFromRsl


class SearchManuscriptInNeb(object):

    def __init__(self, session: requests.Session, *, manuscript_code_title: str):
        self._session = session
        self._manuscript_code_title = manuscript_code_title

    @property
    def manuscript_neb_slug(self) -> str | None:
        return self._search_manuscript_neb_slug()

    def _search_manuscript_neb_slug(self) -> str | None:
        url: str = self.prepare_neb_search_manuscript_api_url(self._manuscript_code_title)
        r = self._session.get(url)
        if not r.json()['data']:
            return None
        manuscript_neb_slug: str = r.json()['data'][0]['_source']['slug']
        return manuscript_neb_slug

    @classmethod
    def prepare_neb_search_manuscript_api_url(cls, manuscript_code_title) -> str:
        if manuscript_code_title[0] == 'Ф':
            manuscript_code_title = cls.prepare_rsl_manuscript_code_title(manuscript_code_title)
        url: str = cls.get_base_neb_search_manuscript_api_url(manuscript_code_title)
        return url

    @staticmethod
    def get_base_neb_search_manuscript_api_url(manuscript_code_title: str) -> str:
        NEB_SEARCH_THEMATIC_SECTIONS: str = '5dd3ea5274d5af0dd456867d'
        NEB_SEARCH_PLACES: str = '5fcf8d4b991f3b9142349d94,618b838a703aa2232fcf7913,5dd530820b10f174bc4c8b09,5dd530840b10f174bc4c8b64,5dd5302a0b10f174bc4c7d25,5dd5302c0b10f174bc4c7d88,5fcf8aa3991f3b9142341612,5dd802773809b788051e3925,5fcf8b96991f3b9142342699,5de79d7fdaf4fec5e4e69ebd,5dd530820b10f174bc4c8b1a,5dd5306b0b10f174bc4c8733,5dd530020b10f174bc4c76df,5fcf8ca9991f3b9142347606,5dd5305d0b10f174bc4c8500,5dd530630b10f174bc4c85f8,5dd530810b10f174bc4c8ada,5fcf8bba991f3b9142343df3,618b839d703aa2232fcf7d0f,5ddad4cdf9982d%20661bc35864'
        NEB_SEARCH_PUBLISHED_YEAR_END: int = 1700
        NEB_SEARCH_LENGTH: int = 1
        NEB_SEARCH_PLACES = ''
        manuscript_code_title_utf: str = urllib.parse.quote(manuscript_code_title)
        url: str = f'{const.NebUrl.SEARCH_MANUSCRIPT_API}?search={manuscript_code_title_utf}&thematicSections={NEB_SEARCH_THEMATIC_SECTIONS}&places={NEB_SEARCH_PLACES}&publishedYearEnd={NEB_SEARCH_PUBLISHED_YEAR_END}&length={NEB_SEARCH_LENGTH}'
        return url

    @staticmethod
    def prepare_rsl_manuscript_code_title(manuscript_code_title: str) -> str:
        if match := const.REGEX_ROMAN_CENTURY_BEFORE_16.search(manuscript_code_title):
            sub_roman_num: str = match[0]
            sub_num: int = fromRoman(sub_roman_num)
            manuscript_code_title = manuscript_code_title.replace(f'/{sub_roman_num}', f'.{sub_num}')
        if manuscript_code_title[-1] == '.':
            manuscript_code_title = manuscript_code_title[:-1]
        manuscript_code_title = manuscript_code_title.strip()
        return manuscript_code_title


class SearchManuscriptInNlr(object):

    def __init__(self, session: requests.Session, *, manuscript_code_title: str):
        self._session = session
        self._manuscript_code_title = manuscript_code_title
        self.manuscript_code = self._search_manuscript_code()

    @property
    def manuscript_code(self) -> UUID:
        return self.__manuscript_code

    @manuscript_code.setter
    def manuscript_code(self, manuscript_code: UUID):
        self.__manuscript_code = manuscript_code

    def _search_manuscript_code(self) -> UUID:
        search_data: dict[str, str] = {
            'doc_Shifr': self._manuscript_code_title,
            'doc_IsYesDigital': 'on'
        }
        r = self._session.post(const.NlrUrl.SEARCH_MANUSCRIPT_API, data=search_data)
        data: str = r.json()['result']
        if 'Данные не найдены' in data:
            raise ValueError(f'The Manuscript with code_title: {self._manuscript_code_title} not found in nlr search')
        soup = BeautifulSoup(data, 'lxml')
        link: list[Tag] = soup.find_all('a')
        if len(link) > 1:
            raise ValueError(f'Meny Manuscripts found on search = code_title: {self._manuscript_code_title}')
        link: Tag = link[0]
        manuscript_code_title_from_nlr: str = link.text
        if manuscript_code_title_from_nlr != self._manuscript_code_title:
            raise ValueError('Manuscript_code_title in libs !=')
        manuscript_code: UUID = UUID(link['data-ab'])
        return manuscript_code


class SearchManuscriptInRsl(object):

    def __init__(self, session: requests.Session, *, manuscript_code_title: str):
        self._session = session
        self._manuscript_code_title = manuscript_code_title
        self.manuscript_code = self.convert_code_title_to_code(manuscript_code_title)

    @property
    def manuscript_code(self) -> str:
        return self.__manuscript_code

    @manuscript_code.setter
    def manuscript_code(self, manuscript_code: str):
        collect_manuscript_data_from_rsl = CollectManuscriptDataFromRsl(self._session, manuscript_code=manuscript_code)
        manuscript_code_title_from_rsl = collect_manuscript_data_from_rsl.manuscript_code_title
        if manuscript_code_title_from_rsl != self._manuscript_code_title:
            raise ValueError('Manuscript_code_title in libs !=')
        self.__manuscript_code = manuscript_code

    @staticmethod
    def convert_code_title_to_code(manuscript_code_title: str) -> str:
        REGEX_FIND_FOND_NUM: Pattern[str] = re.compile(r'(?<=Ф\.)\d*(?=.|\s)')
        fond_num: int = int(REGEX_FIND_FOND_NUM.search(manuscript_code_title)[0])
        num: int = int(manuscript_code_title[manuscript_code_title.find('№') + 1:])
        if '/' in manuscript_code_title:
            fond_sub_roman_num: str = const.REGEX_ROMAN_CENTURY_BEFORE_16.search(
                manuscript_code_title
            )[0].lower()
            return f'f-{fond_num}{fond_sub_roman_num}-{num}'
        return f'f-{fond_num}-{num}'


class SearchManuscriptFactory(object):

    @classmethod
    def get(
            cls,
            session: requests.Session,
            *,
            manuscript_code_title: str
    ) -> SearchManuscriptInRsl | SearchManuscriptInNlr:
        if manuscript_code_title[0] == 'Ф':
            return SearchManuscriptInRsl(session, manuscript_code_title=manuscript_code_title)
        return SearchManuscriptInNlr(session, manuscript_code_title=manuscript_code_title)
