from sqlalchemy.orm import Session

from app import schemas, crud, enums
from ..base_cls import CreateBase, FatalCreateError


class CreateZachalo(CreateBase):

    def __init__(self,
                 db: Session,
                 items: list[schemas.ZachaloCreate],
                 parents_id: list[enums.BibleBookAbbr],
                 num_creatures: int):
        super().__init__(db, items, parents_id, num_creatures)

    def create(self) -> list[int]:
        zachalos_id: list[int] = []

        for bible_book_abbr, zachalo in zip(self.parents_id, self.items):

            if crud.get_zachalo(self.db, bible_book_abbr=bible_book_abbr, num=zachalo.num):
                raise FatalCreateError(self.get_except_text_created(bible_book_abbr, zachalo))

            zachalos_id.append(crud.create_zachalo(self.db, bible_book_abbr=bible_book_abbr, zachalo=zachalo).id)

        self.check_num_creatures(zachalos_id)

        return zachalos_id
