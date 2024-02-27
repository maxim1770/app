import logging

from pydantic import BaseModel, model_validator

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
import logging

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

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # s = Service(r"C:\Users\MaxDroN\Desktop\chromedriver-win64\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)

    # boto_session: boto3.session.Session = next(deps.get_boto())

    # create_all_shm_icons_imgs(db, driver=driver, boto_session=boto_session)

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
    # update_dates_is_solid_weeks(db)

    # create_dates_for_years(db)

    # create_any_holidays(db)
    # create_all_movable_saints_holidays(db)

    # create_all_gallerix_icons_imgs(db, session=session, driver=driver, boto_session=boto_session)
