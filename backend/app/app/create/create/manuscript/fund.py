from sqlalchemy.orm import Session

from app import schemas, crud, enums, utils
from ..base_cls import FatalCreateError


def create_all_funds(db: Session) -> None:
    if crud.fund.get_all(db):
        raise FatalCreateError(f'Fund: funds already created')
    funds_in: list[schemas.FundCreate] = []
    for fund_title in enums.FundTitle:
        if utils.is_rsl_library(fund_title):
            library = enums.LibraryTitle.rsl
        else:
            library = enums.LibraryTitle.nlr
        funds_in.append(schemas.FundCreate(title=fund_title, library=library))
    for fund_in in funds_in:
        crud.fund.create(db, obj_in=fund_in)
