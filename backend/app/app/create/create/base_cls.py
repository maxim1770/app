from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class CreateBase(ABC):

    def __init__(self, db: Session, items: list | None, parents_id: list | int, num_creatures: int):
        self.db = db
        self.items = items
        self.parents_id = parents_id
        self.num_creatures: int = num_creatures

    @abstractmethod
    def create(self) -> list[int]:
        pass

    @classmethod
    def get_except_text_created(cls, *args) -> str:
        return f'{cls}: {" | ".join(map(str, args))} уже была создана'

    def __get_except_text_num_creatures(self, len_items_id: int) -> str:
        return f'Не создались {self.num_creatures} записи из {self}. Было создано {len_items_id} записей'

    def check_num_creatures(self, items_id: list[int]):
        if len(items_id) != self.num_creatures:
            raise FatalCreateError(self.__get_except_text_num_creatures(len(items_id)))


class FatalCreateError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return self.message
