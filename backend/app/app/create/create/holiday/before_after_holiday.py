from datetime import timedelta, date

from sqlalchemy.orm import Session

from app import crud, schemas, enums, const, models


def create_all_before_after_holidays(db: Session) -> None:
    great_holidays_num_before_after_days = [
        (
            'uspenie-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii',
            'Успения Пресвятой Богородицы',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 8),
        ),
        (
            'rozhdestvo-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii',
            'Рождества Пресвятой Богородицы',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 4),
        ),
        (
            'vvedenie-v-tserkov-presvjatuju-vladychitsu-nashu-bogoroditsu',
            'Введения во Храм Пресвятой Богородицы',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 4),
        ),
        (
            'vozdvizhenie-chestnogo-i-zhivotvorjashchego-kresta-gospodnja',
            'Воздвижения Честно́го и Животворящего Креста Господня',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 7),
        ),
        (
            'izhe-po-ploti-rozhdestvo-gospoda-boga-i-spasa-nashego-isusa-hrista',
            'Рождества Христова',
            (enums.HolidayCategoryTitle.predprazdnstvo, 5),
            (enums.HolidayCategoryTitle.poprazdnstvo, 6),
        ),
        (
            'svjatoe-bogojavlenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
            'Богоявления',
            (enums.HolidayCategoryTitle.predprazdnstvo, 4),
            (enums.HolidayCategoryTitle.poprazdnstvo, 8),
        ),
        (
            'sretenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
            'Сретения Господня',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 1),
        ),
        (
            'blagoveschenie-presvjatoj-vladychitsy-nashej-bogoroditsy-i-prisnodevy-marii',
            'Благовещения Пресвятой Богородицы',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 1),
        ),
        (
            'svjatoe-preobrazhenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
            'Преображения Господня',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 7),
        ),
        (
            'voznesenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
            'Вознесения Господня',
            (enums.HolidayCategoryTitle.predprazdnstvo, 1),
            (enums.HolidayCategoryTitle.poprazdnstvo, 8),
        ),
        (
            'svjataja-pjatidesjatnitsa',
            'Пятидесятницы',
            (enums.HolidayCategoryTitle.predprazdnstvo, 0),
            (enums.HolidayCategoryTitle.poprazdnstvo, 6),
        ),
    ]
    for great_holiday_slug, great_holiday_title_in_genitive, before_data, after_data in great_holidays_num_before_after_days:
        __great_holiday = crud.holiday.get_by_slug(db, slug=great_holiday_slug)
        if __great_holiday.day:
            __great_holiday_date = date(const.BASE_YEAR_FOR_DAY, month=__great_holiday.day.month,
                                        day=__great_holiday.day.day)
            for _holiday_category_title, _num_days in [before_data, after_data]:
                before_after_holiday: models.BeforeAfterHoliday = __create_before_after_holiday(
                    db,
                    holiday_category_title=_holiday_category_title,
                    great_holiday_slug=great_holiday_slug,
                    great_holiday_title_in_genitive=great_holiday_title_in_genitive,
                    great_holiday_id=__great_holiday.id
                )
                for day_num in range(1, _num_days + 1):
                    __days = timedelta(days=day_num)
                    if _holiday_category_title == enums.HolidayCategoryTitle.predprazdnstvo:
                        _date = __great_holiday_date - timedelta(days=_num_days + 1) + __days
                        is_last_day = None
                    else:
                        _date = __great_holiday_date + __days
                        is_last_day: bool | None = True if day_num == _num_days else None
                    day = crud.day.get_by_month_and_day(db, month=_date.month, day=_date.day)
                    before_after_holiday_day_association_in = schemas.BeforeAfterHolidayDayAssociationCreate(
                        is_last_day=is_last_day
                    )
                    crud.create_before_after_holiday_day_association(
                        db,
                        before_after_holiday=before_after_holiday,
                        day=day,
                        before_after_holiday_day_association_in=before_after_holiday_day_association_in
                    )
        else:
            __great_holiday_movable_day_id: int = __great_holiday.movable_day_id
            for _holiday_category_title, _num_days in [before_data, after_data]:
                before_after_holiday: models.BeforeAfterHoliday = __create_before_after_holiday(
                    db,
                    holiday_category_title=_holiday_category_title,
                    great_holiday_slug=great_holiday_slug,
                    great_holiday_title_in_genitive=great_holiday_title_in_genitive,
                    great_holiday_id=__great_holiday.id
                )
                for day_num in range(1, _num_days + 1):
                    if _holiday_category_title == enums.HolidayCategoryTitle.predprazdnstvo:
                        _movable_day_id = __great_holiday_movable_day_id - day_num
                        is_last_day = None
                    else:
                        _movable_day_id = __great_holiday_movable_day_id + day_num
                        is_last_day: bool | None = True if day_num == _num_days else None
                    movable_day = crud.get_movable_day_by_id(db, id=_movable_day_id)
                    before_after_holiday_movable_day_association_in = schemas.BeforeAfterHolidayMovableDayAssociationCreate(
                        is_last_day=is_last_day
                    )
                    crud.create_before_after_holiday_movable_day_association(
                        db,
                        before_after_holiday=before_after_holiday,
                        movable_day=movable_day,
                        before_after_holiday_movable_day_association_in=before_after_holiday_movable_day_association_in
                    )


def __create_before_after_holiday(
        db: Session,
        *,
        holiday_category_title: enums.HolidayCategoryTitle,
        great_holiday_slug: str,
        great_holiday_title_in_genitive: str,
        great_holiday_id: int
) -> models.BeforeAfterHoliday:
    __holiday_in = schemas.HolidayCreate(
        slug=f'{holiday_category_title.name}-{great_holiday_slug}',
        title=f'{holiday_category_title} {great_holiday_title_in_genitive}'
    )
    _holiday = crud.holiday.create_with_category(
        db,
        obj_in=__holiday_in,
        holiday_category_id=crud.holiday_category.get_by_title(db, title=holiday_category_title).id
    )
    _before_after_holiday_in = schemas.BeforeAfterHolidayCreate()
    before_after_holiday = crud.create_before_after_holiday(
        db,
        id=_holiday.id,
        before_after_holiday_in=_before_after_holiday_in,
        great_holiday_id=great_holiday_id
    )
    return before_after_holiday
