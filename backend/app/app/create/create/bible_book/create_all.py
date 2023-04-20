import logging

import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import models, enums, crud, schemas
from .bible_book import create_bible_books
from .zachalos_movable_dates import CreateZachaloMovableDateAssociationFactory
from ..movable_date.delete_any_cycle_2 import delete_any_movable_dates_in_cycle_2


def create_all_zachalos_movable_dates_associations(db: Session):
    create_bible_books(db)
    logging.info('Created Bible Books')
    _create_c1_zachalos_movable_dates_associations(db)
    _create_c2_zachalos_movable_dates_associations(db)
    _create_c1_and_c2_zachalos_movable_dates_associations_matins_on_sun(db)
    _create_c3_zachalos_movable_dates_associations(db)


def _create_c1_zachalos_movable_dates_associations(db: Session):
    create_zachalo_movable_date_association = CreateZachaloMovableDateAssociationFactory.get_c1(db)
    zachalos_id: list[int] = create_zachalo_movable_date_association.create()
    logging.info('Created c1 zachalos movable dates associations')


def _create_c2_zachalos_movable_dates_associations(db: Session):
    create_zachalo_movable_date_association = CreateZachaloMovableDateAssociationFactory.get_c2(db)
    zachalos_id: list[int] = create_zachalo_movable_date_association.create()
    logging.info('Created c2 zachalos movable dates associations')
    zachalos = db.execute(sa.select(models.Zachalo).join(models.BibleBook).filter(
        models.BibleBook.abbr == enums.BibleBookAbbr.Apok)).scalars().all()
    for zachalo in zachalos:
        zachalos_movable_dates = db.execute(
            sa.select(models.ZachalosMovableDates).filter_by(zachalo_id=zachalo.id)
        ).scalar_one_or_none()
        db.delete(zachalos_movable_dates)
        db.delete(zachalo)
        db.commit()
    delete_any_movable_dates_in_cycle_2(db)
    logging.info(
        'Deleted default (BibleBookAbbr = Apok) c2 zachalos and zachalos movable dates associations and any movable dates'
    )


def _create_c1_and_c2_zachalos_movable_dates_associations_matins_on_sun(db: Session):
    zachalos_evangels_id: list[int] = []
    for i, zachalo_data in enumerate([
        (enums.BibleBookAbbr.Mt, 116),
        (enums.BibleBookAbbr.Mk, 70),
        (enums.BibleBookAbbr.Mk, 71),
        (enums.BibleBookAbbr.Lk, 112),
        (enums.BibleBookAbbr.Lk, 113),
        (enums.BibleBookAbbr.Lk, 114),
        (enums.BibleBookAbbr.Jn, 63),
        (enums.BibleBookAbbr.Jn, 64),
        (enums.BibleBookAbbr.Jn, 65),
        (enums.BibleBookAbbr.Jn, 66),
        (enums.BibleBookAbbr.Jn, 67)
    ]):
        zachalos_evangels_id.append(
            crud.create_zachalo(
                db,
                bible_book_abbr=zachalo_data[0],
                zachalo=schemas.ZachaloCreate(
                    num=zachalo_data[1],
                    title=f'Евангелие Воскресное {i + 1}'
                ),
            ).id
        )
    evangels_matins_suns_nums: list[int] = [
        1, 3, 4, 7, 8, 10, 9,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
        1, 2
    ]
    movable_dates_suns = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle)
        .filter(
            (models.Cycle.num != enums.CycleNum.cycle_3) &
            ((models.Week.num != 1) | (models.Week.sunday_num != 1)) &
            (models.Week.sunday_num != 36) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.sun) &
            (models.DivineService.title == enums.DivineServiceTitle.matins)
        )).scalars().all()
    for movable_date_sun, evangel_matins_sun_num in zip(
            movable_dates_suns,
            evangels_matins_suns_nums
    ):
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalos_evangels_id[evangel_matins_sun_num - 1],
            movable_date_id=movable_date_sun.id
        )

    movable_date_vespers_PASKHA_id = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle)
        .filter(
            (models.Cycle.num == enums.CycleNum.cycle_1) &
            ((models.Week.num == 1) | (models.Week.sunday_num == 1)) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.sun) &
            (models.DivineService.title == enums.DivineServiceTitle.vespers)
        )).scalar_one_or_none().id
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalos_evangels_id[9 - 1],
        movable_date_id=movable_date_vespers_PASKHA_id
    )


def _create_c3_zachalos_movable_dates_associations(db: Session):
    __create_c3_zachalos_movable_dates_associations_liturgies_on_sat_and_sun(db)
    __create_c3_zachalos_movable_dates_associations_matins_on_sun_6(db)
    __create_zachalos_movable_dates_associations_on_strastnaja_sedmitsa(db)
    logging.info('Created c3 zachalos movable dates associations')


def __create_c3_zachalos_movable_dates_associations_liturgies_on_sat_and_sun(db: Session):
    zachalos_evangels_id: list[int] = []
    for zachalo_num in [10, -5, 6, 7, 8, 37, 31, 40, 35, 47, -39, -41]:
        if zachalo_num < 0:
            zachalos_evangels_id.append(
                crud.create_zachalo(db, bible_book_abbr=enums.BibleBookAbbr.Jn,
                                    zachalo=schemas.ZachaloCreate(num=abs(zachalo_num))).id
            )
        else:
            zachalos_evangels_id.append(
                crud.create_zachalo(db, bible_book_abbr=enums.BibleBookAbbr.Mt,
                                    zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
            )
    zachalos_apostles_id: list[int] = []
    for zachalo_num in [303, 329, 309, 304, 325, 311, 313, 314, 322, 321, 333, -247]:
        if zachalo_num < 0:
            zachalos_apostles_id.append(
                crud.create_zachalo(db, bible_book_abbr=enums.BibleBookAbbr.Phil,
                                    zachalo=schemas.ZachaloCreate(num=abs(zachalo_num))).id
            )
        else:
            zachalos_apostles_id.append(
                crud.create_zachalo(db, bible_book_abbr=enums.BibleBookAbbr.Hebr,
                                    zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
            )
    movable_dates = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.not_like('%Страстная%')) &
            (
                    (models.MovableDay.abbr == enums.MovableDayAbbr.sat) |
                    (models.MovableDay.abbr == enums.MovableDayAbbr.sun)
            ) &
            (models.DivineService.title == enums.DivineServiceTitle.liturgy)
        )).scalars().all()
    for movable_date, zachalo_evangel_id, zachalo_apostle_id in zip(
            movable_dates,
            zachalos_evangels_id,
            zachalos_apostles_id
    ):
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_evangel_id,
            movable_date_id=movable_date.id
        )
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_apostle_id,
            movable_date_id=movable_date.id
        )


def __create_c3_zachalos_movable_dates_associations_matins_on_sun_6(db: Session):
    zachalo_sun_6_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Mt,
        zachalo=schemas.ZachaloCreate(num=83)).id
    movable_date_sun_6_id: int = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.sunday_num == 6) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.sun) &
            (models.DivineService.title == enums.DivineServiceTitle.matins)
        )).scalar_one_or_none().id

    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_sun_6_id,
        movable_date_id=movable_date_sun_6_id
    )


def __create_zachalos_movable_dates_associations_on_strastnaja_sedmitsa(db: Session):
    zachalos_evangels_id: list[int] = []
    for zachalo_num in [98, 102, 108, 107, 115]:
        zachalos_evangels_id.append(
            crud.create_zachalo(db, bible_book_abbr=enums.BibleBookAbbr.Mt,
                                zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
        )
    zachalo_apostle_sat_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Rom,
        zachalo=schemas.ZachaloCreate(num=91)).id
    movable_dates = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr != enums.MovableDayAbbr.fri) &
            (models.DivineService.title == enums.DivineServiceTitle.liturgy)
        )).scalars().all()
    for movable_date, zachalo_evangel_id in zip(movable_dates, zachalos_evangels_id):
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_evangel_id,
            movable_date_id=movable_date.id
        )
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_apostle_sat_id,
        movable_date_id=movable_dates[-1].id
    )

    zachalo_apostle_vespers_thu_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr._1Cor,
        zachalo=schemas.ZachaloCreate(num=149)).id
    movable_date_vespers_thu_id: int = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.thu) &
            (models.DivineService.title == enums.DivineServiceTitle.vespers)
        )).scalar_one_or_none().id
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_apostle_vespers_thu_id,
        movable_date_id=movable_date_vespers_thu_id
    )

    zachalo_evangel_1_umyveniye_thu_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Jn,
        zachalo=schemas.ZachaloCreate(num=44)).id
    zachalo_evangel_2_umyveniye_thu_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Jn,
        zachalo=schemas.ZachaloCreate(num=45)).id
    movable_date_umyveniye_thu_id: int = db.execute(
        sa.select(models.MovableDate).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.thu) &
            (models.MovableDate.divine_service_id == None)
        )).scalar_one_or_none().id
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_evangel_1_umyveniye_thu_id,
        movable_date_id=movable_date_umyveniye_thu_id
    )
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_evangel_2_umyveniye_thu_id,
        movable_date_id=movable_date_umyveniye_thu_id
    )

    zachalo_evangel_matins_sat_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Mt,
        zachalo=schemas.ZachaloCreate(num=114)).id
    zachalo_apostle_matins_sat_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr._1Cor,
        zachalo=schemas.ZachaloCreate(num=133)).id
    movable_date_matins_sat_id: int = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.sat) &
            (models.DivineService.title == enums.DivineServiceTitle.matins)
        )).scalar_one_or_none().id
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_evangel_matins_sat_id,
        movable_date_id=movable_date_matins_sat_id
    )
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_apostle_matins_sat_id,
        movable_date_id=movable_date_matins_sat_id
    )

    ___create_zachalos_movable_dates_associations_on_fri_strastnaja_sedmitsa(db)


def ___create_zachalos_movable_dates_associations_on_fri_strastnaja_sedmitsa(db: Session):
    zachalos_evangels_id: list[int] = []
    for bible_book_abbr, zachalo_num in [
        (enums.BibleBookAbbr.Jn, 46),
        (enums.BibleBookAbbr.Jn, 58),
        (enums.BibleBookAbbr.Mt, 109),
        (enums.BibleBookAbbr.Jn, 59),
        (enums.BibleBookAbbr.Mt, 111),
        (enums.BibleBookAbbr.Mk, 67),
        (enums.BibleBookAbbr.Mt, 113),
        (enums.BibleBookAbbr.Lk, 111),
        (enums.BibleBookAbbr.Jn, 61),
        (enums.BibleBookAbbr.Mk, 69),
        (enums.BibleBookAbbr.Jn, 62),
        (enums.BibleBookAbbr.Mt, 114)
    ]:
        zachalos_evangels_id.append(
            crud.create_zachalo(db, bible_book_abbr=bible_book_abbr,
                                zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
        )
    movable_date_common_fri_id: int = db.execute(
        sa.select(models.MovableDate).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.fri) &
            (models.MovableDate.divine_service_id == None)
        )).scalar_one_or_none().id
    for zachalo_evangel_id in zachalos_evangels_id:
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_evangel_id,
            movable_date_id=movable_date_common_fri_id
        )

    zachalos_evangels_na_chasakh_id: list[int] = []
    for bible_book_abbr, zachalo_num in [
        (enums.BibleBookAbbr.Mt, 111),  # В Рукописи bibliya_n_z_evangelie_revangelie_tetr_evangelie_isaaka_bireva 110
        (enums.BibleBookAbbr.Mk, 66),  # В ... 67
        (enums.BibleBookAbbr.Lk, 110),  # В ... 111
        (enums.BibleBookAbbr.Jn, 59)
    ]:
        zachalos_evangels_na_chasakh_id.append(
            crud.create_zachalo(db, bible_book_abbr=bible_book_abbr,
                                zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
        )
    zachalos_apostles_na_chasakh_id: list[int] = []
    for bible_book_abbr, zachalo_num in [
        (enums.BibleBookAbbr.Gal, 216),
        (enums.BibleBookAbbr.Rom, 88),
        (enums.BibleBookAbbr.Hebr, 306),
        (enums.BibleBookAbbr.Hebr, 324)
    ]:
        zachalos_apostles_na_chasakh_id.append(
            crud.create_zachalo(db, bible_book_abbr=bible_book_abbr,
                                zachalo=schemas.ZachaloCreate(num=zachalo_num)).id
        )
    for zachalo_evangel_na_chas_id, zachalo_apostle_na_chas_id in zip(
            zachalos_evangels_na_chasakh_id, zachalos_apostles_na_chasakh_id
    ):
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_evangel_na_chas_id,
            movable_date_id=movable_date_common_fri_id
        )
        crud.create_zachalo_movable_date_association(
            db,
            zachalo_id=zachalo_apostle_na_chas_id,
            movable_date_id=movable_date_common_fri_id
        )

    zachalo_evangel_vespers_fri_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr.Mt,
        zachalo=schemas.ZachaloCreate(num=110)).id
    zachalo_apostle_vespers_fri_id: int = crud.create_zachalo(
        db, bible_book_abbr=enums.BibleBookAbbr._1Cor,
        zachalo=schemas.ZachaloCreate(num=125)).id
    movable_date_vespers_fri_id: int = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle
        ).filter(
            (models.Cycle.num == enums.CycleNum.cycle_3) &
            (models.Week.title.like('%Страстная%')) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.fri) &
            (models.DivineService.title == enums.DivineServiceTitle.vespers)
        )).scalar_one_or_none().id
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_evangel_vespers_fri_id,
        movable_date_id=movable_date_vespers_fri_id
    )
    crud.create_zachalo_movable_date_association(
        db,
        zachalo_id=zachalo_apostle_vespers_fri_id,
        movable_date_id=movable_date_vespers_fri_id
    )
