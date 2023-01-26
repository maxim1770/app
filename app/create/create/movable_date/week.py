from sqlalchemy.orm import Session

from app import schemas, crud
from ..base_cls import CreateBase, FatalCreateError


class CreateWeek(CreateBase):

    def __init__(self, db: Session, items: list[schemas.WeekCreate], parents_id: int, num_creatures: int):
        super().__init__(db, items, parents_id, num_creatures)

    def create(self) -> list[int]:
        weeks_id: list[int] = []

        for week in self.items:

            if crud.get_week_by_id(self.db, cycle_id=self.parents_id, sunday_num=week.sunday_num):
                raise FatalCreateError(self.get_except_text_created(self.parents_id, week))

            weeks_id.append(crud.create_week(self.db, cycle_id=self.parents_id, week=week).id)

        self.check_num_creatures(weeks_id)

        return weeks_id
