from pathlib import Path
from uuid import UUID

from pydantic import BaseModel, constr, conint, HttpUrl, root_validator, validator

from app import const, enums, utils
from .fund import Fund
from .page import PageCreate
from ..year import Year, YearCreate


class NotNumberedPage(BaseModel):
    page: PageCreate
    count: conint(strict=True, ge=1, le=30)


class NotNumberedPages(BaseModel):
    __root__: list[NotNumberedPage]

    @validator('__root__')
    def sort_not_numbered_pages(cls, not_numbered_pages: list[NotNumberedPage]):
        not_numbered_pages.sort(key=lambda not_numbered_page: not_numbered_page.page.num)
        return not_numbered_pages


class ManuscriptBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=150) | None = None
    neb_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG_STR) | None = None
    code_title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=20) | None = None
    code: UUID | constr(strip_whitespace=True, regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR) | None = None
    handwriting: conint(strict=True, ge=1, le=12) | None = None
    not_numbered_pages: NotNumberedPages = []
    first_page_position: enums.PagePosition | None = None


class ManuscriptCreateAny(ManuscriptBase):

    @root_validator
    def check_and_compute_year(cls, values):
        if not (values['code'] or values['neb_slug']):
            raise ValueError('Одно поле code или neb_slug точно должно быть задано')
        return values


class ManuscriptCreate(ManuscriptBase):
    title: constr(strip_whitespace=True, strict=True, max_length=150)
    code_title: constr(strip_whitespace=True, strict=True, max_length=20)
    code: UUID | constr(strip_whitespace=True, regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
    handwriting: conint(strict=True, ge=1, le=12)


class ManuscriptUpdate(ManuscriptBase):
    pass


class ManuscriptInDBBase(ManuscriptBase):
    id: int

    title: str
    code_title: str
    code: str
    handwriting: int
    path: Path = None

    url: HttpUrl = None
    neb_url: HttpUrl | None = None

    year: Year
    fund: Fund

    @validator('url', pre=True, always=True)
    def prepare_url(cls, url: None, values):
        url: str = utils.prepare_manuscript_url(values['code'])
        return url

    @validator('neb_url', pre=True, always=True)
    def prepare_neb_url(cls, neb_url: None, values):
        if not values['neb_slug']:
            return None
        neb_url: str = utils.prepare_manuscript_neb_url(values['neb_slug'])
        return neb_url

    # @validator('path', pre=True, always=True)
    # def prepare_path(cls, path: None, values):
    #     try:
    #         created_path: Path = utils.PrepareManuscriptPath(
    #             fund_title=values['fund'].title,
    #             library_title=values['fund'].library,
    #             code=values['code']
    #         ).created_path
    #     except FileNotFoundError:
    #         return None
    #     return created_path

    class Config:
        orm_mode = True


class Manuscript(ManuscriptInDBBase):
    # books: list[BookmarkInDB] = []
    pass


class ManuscriptInDB(ManuscriptInDBBase):
    pass


class ManuscriptDataBase(BaseModel):
    manuscript_in: ManuscriptUpdate | None = None
    fund_title: enums.FundTitle | None = None
    year_in: YearCreate | None = None


class ManuscriptDataCreateAny(ManuscriptDataBase):
    manuscript_in: ManuscriptCreateAny


class ManuscriptDataCreate(ManuscriptDataBase):
    manuscript_in: ManuscriptCreate
    fund_title: enums.FundTitle
    year_in: YearCreate


class ManuscriptDataUpdate(ManuscriptDataBase):
    pass
