from sqlalchemy.orm import Session

from app import crud, enums
from ..base_cls import CreateBase, FatalCreateError


# TODO Тут возможно стоит разделить создания записей и создания pydantic моделей, для того чтобы в разы уменьшить кол. кода
#  Но тогда возможно потеряться логика с различием данных, в создании записей, по идее, все будет в одном цикле for
#  ТУТ И ПОВТОРОВ МНОГО, ТАК ЧТО ДУМАЮ ТОЧНО СТОИТ РАЗДЕЛИТЬ НА ДВЕ ЧАСТИ


# TODO если что про утреню в четверг и комментарий можно посмотреть в Local History

class CreateMovableDate(CreateBase):

    def __init__(self, db: Session, parents_id: list[int], sundays_matins: list[int | None], num_creatures: int):
        super().__init__(db, items=None, parents_id=parents_id, num_creatures=num_creatures)
        self.sundays_matins = sundays_matins

    def create(self) -> list[int]:
        movable_dates_id: list[int] = []

        for i, movable_day_id in enumerate(self.parents_id):

            if i % 7 == 0:
                # Создание вс Утрени
                if self.sundays_matins[i // 7]:

                    if crud.get_movable_date_by_id(
                            self.db,
                            movable_day_id=movable_day_id,
                            divine_service_title=enums.DivineServiceTitle.matins
                    ):
                        raise FatalCreateError(
                            self.get_except_text_created(movable_day_id, enums.DivineServiceTitle.matins))
                    else:
                        movable_dates_id.append(
                            crud.create_movable_date(
                                self.db,
                                movable_day_id=movable_day_id,
                                divine_service_title=enums.DivineServiceTitle.matins
                            ).id
                        )

            # Создание Вс, пн, вт, ср, чт, пт, сб - Литургии
            if crud.get_movable_date_by_id(
                    self.db,
                    movable_day_id=movable_day_id,
                    divine_service_title=enums.DivineServiceTitle.liturgy
            ):
                raise FatalCreateError(self.get_except_text_created(movable_day_id, enums.DivineServiceTitle.liturgy))

            movable_dates_id.append(
                crud.create_movable_date(
                    self.db,
                    movable_day_id=movable_day_id,
                    divine_service_title=enums.DivineServiceTitle.liturgy
                ).id
            )

        self.check_num_creatures(movable_dates_id)

        return movable_dates_id
