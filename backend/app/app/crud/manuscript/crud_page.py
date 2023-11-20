from pydantic import BaseModel

from app.models import Page
from app.schemas import PageCreate, PageUpdate
from ..base import CRUDBase


class PageFilter(BaseModel):
    pass


class CRUDPage(CRUDBase[Page, PageCreate, PageUpdate, PageFilter]):
    pass


page = CRUDPage(Page)
