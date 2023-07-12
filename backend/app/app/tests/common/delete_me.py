import logging

from pydantic import BaseModel, model_validator

from app.create import create_any_holidays, create_all_great_holidays, create_all_tipikons, update_dates_posts_ids, \
    create_all_posts, create_dates_for_years
from app.create.create.holiday.before_after_holiday import create_all_before_after_holidays
from app.create.prepare.manuscript.bookmark.create_pdf_bookmark import create_lls_pdf_bookmarks
from app.schemas._calendar_attribute import CalendarAttribute

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

from sqlalchemy.orm import Session
from app.api import deps


class PydanticTestModel(BaseModel):
    text1: str
    text: str | None

    @model_validator(mode='before')
    @classmethod
    def prepare_text(cls, values):
        logging.error(values)
        logging.error(type(values))
        values['text'] = 'text'

        return values
        # handwriting_to_rating: float = round(info.data['handwriting'] / 2.4, 1)
        # info.data['handwriting_to_rating'] = handwriting_to_rating
        # return info


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    # session: requests.Session = next(deps.get_session())
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # p = PydanticTestModel(text1='text1')
    # print(p)

    # _create_all_pravicon_icons(db, session=session)
    # create_all_psaltyr_books(db)

    # create_all_cathedral_books(db)
    # create_kormchaya_pdf_bookmarks(db)
    # create_all_manuscripts_lls(db)
    # create_lls_pdf_bookmarks(db)
    # create_bible_books(db)
    # create_all_great_holidays(db)
    # create_any_holidays(db)
    # create_all_before_after_holidays(db)
    # create_all_tipikons(db)
    # create_all_posts(db)
    # update_dates_posts_ids(db)
    # create_dates_for_years(db)

    a = CalendarAttribute()
    print(a)