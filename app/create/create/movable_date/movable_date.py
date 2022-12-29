from sqlalchemy.orm import Session

from app import schemas, crud
from app.create.create.base_cls import CreateBase, FatalCreateError


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

        # FIXME попробовать убрать это и в функции create_movable_date не требовать movable_date
        # просто заглушка для вызовов функции create_movable_date()
        movable_date: schemas.MovableDateCreate = schemas.MovableDateCreate()

        for i, movable_day_id in enumerate(self.parents_id):

            if i % 7 == 0:
                # Создание вс Утрени
                if self.sundays_matins[i // 7]:

                    if crud.get_movable_date_by_id(
                            self.db,
                            movable_day_id=movable_day_id,
                            divine_service_title=schemas.DivineServiceEnum.matins
                    ):
                        raise FatalCreateError(self.get_except_text_created(movable_day_id, schemas.DivineServiceEnum.matins))
                    else:
                        movable_dates_id.append(
                            crud.create_movable_date(
                                self.db,
                                movable_day_id=movable_day_id,
                                divine_service_title=schemas.DivineServiceEnum.matins,
                                movable_date=movable_date
                            ).id
                        )

            # Создание Вс, пн, вт, ср, чт, пт, сб - Литургии
            if crud.get_movable_date_by_id(
                    self.db,
                    movable_day_id=movable_day_id,
                    divine_service_title=schemas.DivineServiceEnum.liturgy
            ):
                raise FatalCreateError(self.get_except_text_created(movable_day_id, schemas.DivineServiceEnum.liturgy))

            movable_dates_id.append(
                crud.create_movable_date(
                    self.db,
                    movable_day_id=movable_day_id,
                    divine_service_title=schemas.DivineServiceEnum.liturgy,
                    movable_date=movable_date
                ).id
            )

        self.check_num_creatures(movable_dates_id)

        return movable_dates_id
