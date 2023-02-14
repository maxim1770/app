from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import FatalCreateError


def create_all_funds(db: Session) -> None:
    if crud.get_funds(db):
        raise FatalCreateError(f'Fund: funds уже были созданы')

    funds_in = [schemas.FundCreate(title=fund_title, library=enums.LibraryTitle.nlr)
                for fund_title in enums.FundTitle]

    for fund_in in funds_in:
        crud.create_fund(db, fund_in=fund_in)
