import sqlalchemy as sa
from sqlalchemy.orm import Session

from app import enums
from app import models


def delete_any_movable_dates_in_cycle_2(db: Session):
    liturgies_on_wed_and_fri_sun_35 = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle)
        .filter(
            (models.Cycle.num == enums.CycleNum.cycle_2) &
            (models.Week.sunday_num == 35) &
            ((models.MovableDay.abbr == enums.MovableDayAbbr.wed) | (
                    models.MovableDay.abbr == enums.MovableDayAbbr.fri)) &
            (models.DivineService.title == enums.DivineServiceTitle.liturgy)
        )).scalars().all()
    for movable_day in liturgies_on_wed_and_fri_sun_35:
        db.delete(movable_day)
        db.commit()

    matins_on_sun_36 = db.execute(
        sa.select(models.MovableDate).join(models.DivineService).join(models.MovableDay).join(models.Week).join(
            models.Cycle)
        .filter(
            (models.Cycle.num == enums.CycleNum.cycle_2) &
            (models.Week.sunday_num == 36) &
            (models.MovableDay.abbr == enums.MovableDayAbbr.sun) &
            (models.DivineService.title == enums.DivineServiceTitle.matins)
        )).scalar_one_or_none()
    db.delete(matins_on_sun_36)
    db.commit()
