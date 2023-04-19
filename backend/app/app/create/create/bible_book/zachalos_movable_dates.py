import logging

from sqlalchemy.orm import Session

from app import crud, enums
from app.create import const, prepare
from .zachalo import CreateZachalo
from ..base_cls import CreateBase


class CreateZachaloMovableDateAssociation(CreateBase):

    def __init__(self, db: Session, parents_id: list[int], zachalos_id: list[int], num_creatures: int):
        super().__init__(db, items=None, parents_id=parents_id, num_creatures=num_creatures)
        self._zachalos_id = zachalos_id

    def create(self) -> list[int]:
        zachalos_id: list[int] = []
        # Создание Вс, пн, вт, ср, чт, пт, сб - Литургии
        for i, movable_date_id in enumerate(self.parents_id):
            # Создание Евангелие и Апостол для каждого дня
            for zachalo_id in self._zachalos_id[2 * i: 2 * (i + 1)]:
                # if crud.get_reading_by_id(self.db, movable_date_id=movable_date_id, zachalo_id=zachalo_id):
                #     raise FatalCreateError(self.get_except_text_created(movable_date_id, zachalo_id))

                zachalos_id.append(
                    crud.create_zachalo_movable_date_association(
                        self.db,
                        zachalo_id=zachalo_id,
                        movable_date_id=movable_date_id
                    ).id
                )
        self.check_num_creatures(zachalos_id)
        return zachalos_id


class CreateZachaloMovableDateAssociationFactory(object):

    @staticmethod
    def get_c1(db: Session) -> CreateZachaloMovableDateAssociation:
        create_zachalo: CreateZachalo = prepare.CreateZachaloFactory.get_c1_zachalo(db)
        zachalos_id: list[int] = create_zachalo.create()
        logging.info("Created c1 zachalos")

        cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_1).id
        divine_service_id: int = crud.get_divine_service(db, title=enums.DivineServiceTitle.liturgy).id
        movable_dates_id: list[int] = [movable_date.id for movable_date in
                                       crud.get_movable_dates(
                                           db,
                                           cycle_id=cycle_id,
                                           divine_service_id=divine_service_id
                                       )
                                       ]
        return CreateZachaloMovableDateAssociation(
            db,
            parents_id=movable_dates_id,
            zachalos_id=zachalos_id,
            num_creatures=const.NumMovableDay.IN_CYCLE_1 * 2
        )

    @staticmethod
    def get_c2(db: Session) -> CreateZachaloMovableDateAssociation:
        create_zachalo: CreateZachalo = prepare.CreateZachaloFactory.get_c2_zachalo(db)
        zachalos_id: list[int] = create_zachalo.create()
        logging.info("Created c2 zachalos")

        cycle_id: int = crud.get_cycle(db, num=enums.CycleNum.cycle_2).id
        divine_service_id: int = crud.get_divine_service(db, title=enums.DivineServiceTitle.liturgy).id
        movable_dates_id: list[int] = [movable_date.id for movable_date in
                                       crud.get_movable_dates(
                                           db,
                                           cycle_id=cycle_id,
                                           divine_service_id=divine_service_id
                                       )
                                       ]
        return CreateZachaloMovableDateAssociation(
            db,
            parents_id=movable_dates_id,
            zachalos_id=zachalos_id,
            num_creatures=const.NumMovableDay.IN_CYCLE_2 * 2
        )
