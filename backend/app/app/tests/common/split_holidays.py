import logging

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api import deps
from app.create import create_saint_holiday
from app.create.create.holiday.create_all import _check_holiday_for_existence_and_to_slug
from app.create.prepare.year import PrepareYearTitle
from app.schemas import YearCreate, HolidayCreate, SaintCreate, DayCreate

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def main(db):
    """
    Если год не указан в азбука, то ставим XVI и потом в бд вручную убираем
    """
    for holiday_slug, year_data, titles in [
        ('den-pamjati-onufrij-velikij-i-petr-afonskij', ('734', 2), ('Прп. Ону́фрия Великого', 'Прп. Петра Афонского')),
        ('den-pamjati-foma-malein-i-akakij-sinajskij', ('VI', 2), ('Прп. Фомы́, иже в Малеи', 'Прп. Ака́кия Синайского, о котором повествуется в Лествице')),
        ('den-pamjati-amfilohij-ikonijskij-i-grigorij-akragantijskij', ('VI-VII', 2), ('Свт. Амфило́хия Иконийского', 'Свт. Григо́рия Акрагантийского')),
        ('den-pamjati-sisinij-kizicheskij-i-feodor-antiohijskij', ('IV', 2), ('Мч. Сиси́ния, епископа Кизического', 'Мч. Фео́дора Антиохийского')),
        ('den-pamjati-kliment-rimskij-i-petr-i-aleksandrijskij', ('311', 2), ('Сщмч. Кли́мента, папы Римского', 'Сщмч. Петра I Александрийского, архиепископа')),
        ('den-pamjati-pavel-fivejskij-i-ioann-kushchnik', ('V', 2), ('Прп. Павла Фивейского', 'Прп. Иоа́нна Кущника')),
        ('den-pamjati-parfenij-lampsakijskij-i-luka-elladskij', ('ок. 946', 2), ('Прп. Парфе́ния, епископа Лампсакийского', 'Прп. Луки́ Елладского')),
        ('den-pamjati-feodotija-nikejskaja-muchenica-i-agafoklija', ('XVI', 2), ('Мц. Феодо́тии', 'Мц. Агафо́кли')),
    ]:
        holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
        day_in = DayCreate(month=holiday.day.month, day=holiday.day.day)
        saint_in_1 = SaintCreate(slug=holiday.saints[0].slug)
        saint_in_2 = SaintCreate(slug=holiday.saints[1].slug)
        year_title: str = PrepareYearTitle(year_data[0]).year_title
        some_year_in = YearCreate(title=year_title)
        has_year_2: bool = True if year_data[1] == 2 else False
        if has_year_2:
            year_in_1 = YearCreate(title=holiday.year.title)
            year_in_2 = some_year_in
        else:
            year_in_1 = some_year_in
            year_in_2 = YearCreate(title=holiday.year.title)
        holiday_in_1 = HolidayCreate(title=titles[0],
                                     slug=holiday.holiday_category.title.name.replace('_', '-') + '-' + saint_in_1.slug)
        holiday_in_2 = HolidayCreate(title=titles[1],
                                     slug=holiday.holiday_category.title.name.replace('_', '-') + '-' + saint_in_2.slug)
        saint_holiday_in_1 = schemas.SaintHolidayCreate(
            day_in=day_in,
            saint_in=saint_in_1,
            holiday_in=holiday_in_1,
            holiday_category_title=holiday.holiday_category.title,
            year_in=year_in_1,
        )
        saint_holiday_in_2 = schemas.SaintHolidayCreate(
            day_in=day_in,
            saint_in=saint_in_1,
            holiday_in=holiday_in_2,
            holiday_category_title=holiday.holiday_category.title,
            year_in=year_in_2
        )
        for holiday_data_in in [saint_holiday_in_1, saint_holiday_in_2]:
            holiday_data_in = _check_holiday_for_existence_and_to_slug(
                db,
                holiday_data_in=holiday_data_in
            )
            create_saint_holiday(db, holiday_data_in)
        for saint in holiday.saints:
            saint_holiday = db.execute(sa.select(models.SaintHolidayAssociation).filter_by(saint_id=saint.id,
                                                                                           holiday_id=holiday.id)).scalar_one_or_none()
            db.delete(saint_holiday)
            db.commit()
        crud.holiday.remove_by_slug(db, slug=holiday.slug)


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    main(db)


