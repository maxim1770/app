from app.filters import FundFilter
from app.models import Fund
from app.schemas import FundCreate, FundUpdate
from ..base import CRUDBase


class CRUDFund(CRUDBase[Fund, FundCreate, FundUpdate, FundFilter]):
    pass


fund = CRUDFund(Fund)
