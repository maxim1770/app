# import logging
#
# from bs4 import Tag
# from sqlalchemy.orm import Session
#
# from app import crud
# from app.api import deps
# from app.create_data.create_data.saint.saint import update_saint
# from app.create_data.prepare.base_collect import collect_saint_data, get_session
# from app.create_data.prepare.saint.saint import SaintDataUpdateFactory
#
# if __name__ == '__main__':
#     db: Session = next(deps.get_db())
#     session = next(get_session())
#     for saint in crud.saint.get_multi(db, skip=200, limit=2000):
#         saint_slug = saint.slug
#         saint_data_collect: Tag = collect_saint_data(session, saint_slug=saint_slug)
#         try:
#             saint_data_in = SaintDataUpdateFactory(saint_data_collect).get()
#         except AttributeError as e:
#             logging.error(e)
#             logging.info(saint_slug)
#         saint = update_saint(db, saint_slug=saint_slug, saint_data_in=saint_data_in)
from sqlalchemy.orm import Session

from app.api import deps
from app.create.create.saint.create_all import update_saints

if __name__ == '__main__':
    db: Session = next(deps.get_db())
    update_saints(db)
