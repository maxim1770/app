import logging
from datetime import date

import requests
from bs4 import Tag
from sqlalchemy.orm import Session

from app import create
from app import crud
from app.api import deps
from app.create.const import AzbykaUrl
from app.create.prepare.base_collect import get_saints_holidays_new_in_day, get_saints_groups_holidays_new_in_day

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(db: Session):
    holidays = crud.holiday.get_multi(db, limit=2000)
    day = date(2031, 10, 12)
    saints_holidays: list[Tag] = get_saints_holidays_new_in_day(day)
    new_saints_holidays: list[Tag] = []
    print(len(saints_holidays))
    for saint_holiday in saints_holidays:
        saint_slug: str = saint_holiday['href'].replace('http:', 'https:').replace(AzbykaUrl.GET_SAINT_BY_SLUG,
                                                                                   '').lower().strip()
        has_in_holidays: bool = False
        for holiday in holidays:
            if saint_slug in holiday.slug:
                has_in_holidays: bool = True
                print(saint_slug)
                break
        if has_in_holidays:
            continue
        new_saints_holidays.append(saint_holiday)
    print(new_saints_holidays)


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    session: requests.Session = next(deps.get_session())
    # create.create_all_saints_holidays_new(db)
    # create.create_all_saints_groups_holidays_new(db, session=session)
    create.create_all_saints_groups_holidays_new_method_2(db, session=session)


    # a = get_saints_groups_holidays_new_in_day(date(2031, 11, 24))
    # print(a)