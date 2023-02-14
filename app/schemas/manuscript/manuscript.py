from uuid import UUID

from pydantic import BaseModel, constr, conint, HttpUrl, root_validator, validator

from app import const, enums, utils
from .fund import Fund
from ..year import Year, YearCreate


class ManuscriptBase(BaseModel):
    title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=150) | None = None
    neb_slug: constr(strip_whitespace=True, strict=True, max_length=150, regex=const.REGEX_SLUG) | None = None
    code_title: constr(strip_whitespace=True, strict=True, min_length=1, max_length=15) | None = None
    code: UUID | constr(strip_whitespace=True, regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR) | None = None
    handwriting: conint(strict=True, ge=1, le=12) | None = None


class ManuscriptCreateAny(ManuscriptBase):

    @root_validator
    def check_and_compute_year(cls, values):
        if not (values['code'] or values['neb_slug']):
            raise ValueError('Одно поле code или neb_slug точно должно быть задано')
        return values


class ManuscriptCreate(ManuscriptBase):
    title: constr(strip_whitespace=True, strict=True, max_length=150)
    code_title: constr(strip_whitespace=True, strict=True, max_length=15)
    code: UUID | constr(strip_whitespace=True, regex=const.REGEX_RSL_MANUSCRIPT_CODE_STR)
    handwriting: conint(strict=True, ge=1, le=12)


class ManuscriptUpdate(ManuscriptBase):
    pass


class ManuscriptInDBBase(ManuscriptBase):
    id: int

    year: Year
    fund: Fund

    url: HttpUrl
    neb_url: HttpUrl | None = None

    @validator('url')
    def prepare_url(cls, url: None, values):
        if (code := values['code'])[0] == 'f':
            url: str = f'{const.RslUrl.GET_MANUSCRIPT}/{utils.combine_fund_with_manuscript_code(code)}'
        else:
            url: str = f'{const.NlrUrl.GET_MANUSCRIPT}?ab={code}'
        return url

    @validator('neb_slug')
    def prepare_neb_slug(cls, neb_slug: None, values):
        if neb_slug := values['neb_slug']:
            neb_url: str = f'{const.NebUrl.GET_MANUSCRIPT_DATA}/{neb_slug}'
            values['neb_url'] = neb_url
        return neb_slug

    class Config:
        orm_mode = True


class Manuscript(ManuscriptInDBBase):
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
