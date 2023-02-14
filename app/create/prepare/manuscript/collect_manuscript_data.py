import re
from abc import ABC, abstractmethod
from uuid import UUID

import requests
from bs4 import BeautifulSoup
from roman import toRoman

from app import const, enums, utils
from app.schemas import YearCreate


class CollectManuscriptDataBase(ABC):

    def __init__(self, session: requests.Session, *, manuscript_code: UUID | str):
        self._session = session
        self._manuscript_code = manuscript_code
        self._soup: BeautifulSoup = self._collect_manuscript()

    @abstractmethod
    def _collect_manuscript(self) -> BeautifulSoup: ...

    @property
    @abstractmethod
    def manuscript_code_title(self) -> str: ...

    @property
    @abstractmethod
    def manuscript_title(self) -> str: ...

    @property
    @abstractmethod
    def year_in(self) -> YearCreate: ...

    @property
    @abstractmethod
    def fund_title(self) -> enums.FundTitle: ...


class CollectManuscriptDataFromRsl(CollectManuscriptDataBase):

    def __init__(self, session: requests.Session, *, manuscript_code: str):
        super().__init__(session, manuscript_code=manuscript_code)

    def _collect_manuscript(self) -> BeautifulSoup:
        r = self._session.get(
            f'{const.RslUrl.GET_MANUSCRIPT}/{utils.combine_fund_with_manuscript_code(self._manuscript_code)}'
        )
        _soup = BeautifulSoup(r.text, 'lxml')
        return _soup

    @property
    def manuscript_title(self) -> str:
        manuscript_title: str = self._soup.find('h1', class_='item-h1').text.replace(
            f'{self.manuscript_code_title}. ', ''
        ).strip()
        if manuscript_title[-1] == '.':
            manuscript_title = manuscript_title[:-1]
        return manuscript_title

    @property
    def manuscript_code_title(self) -> str:
        manuscript_code_title: str = self._soup.find('li', {'class': 'breadcrumb-item', 'aria-current': 'page'}).text
        return manuscript_code_title

    @property
    def year_in(self) -> YearCreate:
        year_title: str = self._soup.find(
            lambda tag: tag.name == 'span' and 'Дата:' in tag.text
        ).next_element.next_element.strip()
        return YearCreate(title=year_title)

    @property
    def fund_title(self) -> enums.FundTitle:
        fund_title: enums.FundTitle = self.prepare_fund_title(self.manuscript_code_title)
        return fund_title

    @staticmethod
    def prepare_fund_title(manuscript_code_title: str) -> enums.FundTitle:
        fund_title = enums.FundTitle(manuscript_code_title[:manuscript_code_title.find('№') - 1])
        return fund_title


class CollectManuscriptDataFromNlr(CollectManuscriptDataBase):

    def __init__(self, session: requests.Session, *, manuscript_code: UUID):
        super().__init__(session, manuscript_code=manuscript_code)

    def _collect_manuscript(self) -> BeautifulSoup:
        r = self._session.post(const.NlrUrl.GET_MANUSCRIPT_DATA_API, data={'ab': self._manuscript_code})
        _soup = BeautifulSoup(r.json()['result'], 'lxml')
        return _soup

    @property
    def manuscript_title(self) -> str:
        manuscript_title: str = self._soup.find_all('b')[1].text.strip()
        if manuscript_title[-1] == '.':
            manuscript_title = manuscript_title[:-1]
        return manuscript_title

    @property
    def manuscript_code_title(self) -> str:
        _code_title: str = self._soup.find('b').text.replace('ОР ', '').strip()
        return _code_title

    @property
    def year_in(self) -> YearCreate:
        year_title: str = self._soup.find_all('br')[2].next_element.next_element.strip()
        return YearCreate(title=year_title)

    @property
    def fund_title(self) -> enums.FundTitle:
        fund_title: enums.FundTitle = self.prepare_fund_title(self.manuscript_code_title)
        return fund_title

    @staticmethod
    def prepare_fund_title(manuscript_code_title: str) -> enums.FundTitle:
        fond_title_text: str = manuscript_code_title[:manuscript_code_title.rfind('.')]
        if fond_title_text in ['F.IV', 'O.I', 'Q.п.I']:
            fond_title_text: str = 'F.I'
        fund_title = enums.FundTitle(fond_title_text)
        return fund_title


class CollectManuscriptDataFromNeb(CollectManuscriptDataBase):

    def __init__(self, session: requests.Session, *, manuscript_code: str):
        super().__init__(session, manuscript_code=manuscript_code)

    def _collect_manuscript(self) -> BeautifulSoup:
        r = self._session.get(f'{const.NebUrl.GET_MANUSCRIPT_DATA}/{self._manuscript_code}')
        _soup = BeautifulSoup(r.text, 'lxml')
        return _soup

    @property
    def manuscript_title(self) -> str:
        manuscript_title: str = self._soup.find(
            'div', class_='book-info'
        ).find(lambda tag: tag.name == 'div' and 'Заглавие' == tag.text).next_sibling.text.strip()
        manuscript_title = manuscript_title.replace(' :', ':')
        return manuscript_title

    @staticmethod
    def _prepare_rsl_manuscript_code_title_from_neb(manuscript_code_title: str) -> str:
        if match := re.search(r'(?<=\d\.)\d(?=\s№)', manuscript_code_title):
            sub_num: int = int(match[0])
            sub_roman_num: str = toRoman(sub_num)
            manuscript_code_title = manuscript_code_title.replace(f'.{sub_num} №', f'/{sub_roman_num} №')
        return manuscript_code_title

    @property
    def manuscript_code_title(self) -> str:
        manuscript_code_title: str = self._soup.find(
            'div', class_='book-info'
        ).find_all('div', class_='book-info-table')[-1].text.replace('Шифр хранения', '').strip()
        if manuscript_code_title[0] == 'Ф':
            manuscript_code_title: str = self._prepare_rsl_manuscript_code_title_from_neb(manuscript_code_title)
        return manuscript_code_title

    @property
    def year_in(self) -> YearCreate:
        year_title: str = self._soup.find('div', class_='annotation-sections-date').find('h4').text.strip()
        return YearCreate(title=year_title)

    @property
    def fund_title(self) -> enums.FundTitle:
        if self.manuscript_code_title[0] == 'Ф':
            return CollectManuscriptDataFromRsl.prepare_fund_title(self.manuscript_code_title)
        return CollectManuscriptDataFromNlr.prepare_fund_title(self.manuscript_code_title)
