from pydantic import BaseModel

from app import enums
from .manuscript import ManuscriptUpdate, ManuscriptCreateAny, ManuscriptCreate
from ..page import PageCreate
from ...year import YearCreate


class __ManuscriptDataBase(BaseModel):
    manuscript_in: ManuscriptUpdate | None = None
    fund_title: enums.FundTitle | None = None
    year_in: YearCreate | None = None
    preview_page_in: PageCreate | None = None


class ManuscriptDataCreateAny(__ManuscriptDataBase):
    manuscript_in: ManuscriptCreateAny


class ManuscriptDataCreate(__ManuscriptDataBase):
    manuscript_in: ManuscriptCreate
    fund_title: enums.FundTitle
    year_in: YearCreate


class ManuscriptDataUpdate(__ManuscriptDataBase):
    pass
