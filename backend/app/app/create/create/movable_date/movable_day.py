from sqlalchemy.orm import Session

from app import schemas, crud
from app.create import const
from ..base_cls import CreateBase, FatalCreateError


class CreateMovableDay(CreateBase):

    def __init__(self, db: Session, items: list[schemas.MovableDayCreate], parents_id: list[int], num_creatures: int):
        super().__init__(db, items, parents_id, num_creatures)

    def create(self) -> list[int]:
        days_id: list[int] = []

        for i, week_id in enumerate(self.parents_id):

            for day in self.items[i * const.NUM_DAYS_IN_WEEK: (i + 1) * const.NUM_DAYS_IN_WEEK]:

                if crud.get_movable_day_by_week_id(self.db, week_id=week_id, abbr=day.abbr):
                    raise FatalCreateError(self.get_except_text_created(week_id, day))

                days_id.append(crud.create_movable_day(self.db, week_id=week_id, movable_day=day).id)

        self.check_num_creatures(days_id)

        return days_id
