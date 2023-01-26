from typing import Final

from sqlalchemy.orm import Session

from app import crud
from .base_cls import CreateBase, FatalCreateError


#
# def create_readings(
#         db: Session,
#         movable_dates_id: list[int],
#         zachalos_id: list[int],
#         # sundays_matins: list[int | None],
#         number_readings: Final[int]
# ) -> bool:
#     num_creatures: int = 0
#
#     # Создание Вс, пн, вт, ср, чт, пт, сб - Литургии
#     for i, movable_date_id in enumerate(movable_dates_id):
#
#         # Создание Евангелие и Апостол для каждого дня
#         for zachalo_id in zachalos_id[2 * i: 2 * (i + 1)]:
#
#             if crud.get_reading_by_id(
#                     db,
#                     movable_date_id=movable_date_id,
#                     zachalo_id=zachalo_id
#             ):
#                 raise ValueError(f"""
#                     Reading: movable_date_id={movable_date_id}, zachalo_id={zachalo_id} уже была создана"""
#                                  )
#
#             crud.create_reading(
#                 db,
#                 movable_date_id=movable_date_id,
#                 zachalo_id=zachalo_id
#             )
#             num_creatures += 1
#
#     if number_readings != num_creatures:
#         raise ValueError(
#             f'Не создались {number_readings} записи о чтениях в таблице `readings`.')
#     return True


class CreateReading(CreateBase):

    def __init__(self, db: Session, parents_id: list[int], zachalos_id: list[int], num_creatures: int):
        super().__init__(db, items=None, parents_id=parents_id, num_creatures=num_creatures)
        self.zachalos_id = zachalos_id

    def create(self) -> list[int]:
        readings_id: list[int] = []

        # Создание Вс, пн, вт, ср, чт, пт, сб - Литургии
        for i, movable_date_id in enumerate(self.parents_id):

            # Создание Евангелие и Апостол для каждого дня
            for zachalo_id in self.zachalos_id[2 * i: 2 * (i + 1)]:

                if crud.get_reading_by_id(self.db, movable_date_id=movable_date_id, zachalo_id=zachalo_id):
                    raise FatalCreateError(self.get_except_text_created(movable_date_id, zachalo_id))

                readings_id.append(
                    crud.create_reading(self.db, movable_date_id=movable_date_id, zachalo_id=zachalo_id).id
                )

        self.check_num_creatures(readings_id)

        return readings_id
