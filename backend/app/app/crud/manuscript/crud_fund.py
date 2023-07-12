from pydantic import BaseModel

from app.models import Fund
from app.schemas import FundCreate, FundUpdate
from ..base import CRUDBase


class FundFilter(BaseModel):
    pass


class CRUDFund(CRUDBase[Fund, FundCreate, FundUpdate, FundFilter]):
    pass


fund = CRUDFund(Fund)
