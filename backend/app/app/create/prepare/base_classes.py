from abc import ABC, abstractmethod
from copy import deepcopy
from functools import wraps
from typing import Final, Any

from bs4 import Tag
from pydantic import BaseModel, parse_obj_as

# FIXME: баги с data, т.к у класса PrepareParentNoCopyBase остается инфо о дате, нужно это сделать как то
#  только для объектов, а не для классов
from app.create.create.base_cls import FatalCreateError


class PrepareBase(ABC):
    # _final_len = None

    def __init__(self, data: list | None = None):
        self.data = data if data else [None] * self.final_len
        self._prepare()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: list):
        self.__data = data

    @property
    def final_len(self):
        return self._final_len

    @final_len.setter
    def final_len(self, final_len: int):
        self._final_len = final_len

    def _prepare(self):
        if len(self.data) != self.final_len:
            raise FatalCreateError(f"После prepare массив должен быть длинной: {self.final_len}, a не {len(self.data)}")


class PrepareMethodsBase(PrepareBase):

    def __init__(self, data: list | None = None):
        super().__init__(data=data)

    def _prepare(self):
        self._fill_gaps()
        self._clean()
        self._convert()
        super()._prepare()

    @abstractmethod
    def _fill_gaps(self): pass

    @abstractmethod
    def _clean(self): pass

    @abstractmethod
    def _convert(self): pass


class PrepareTableBase(PrepareMethodsBase):

    def __init__(self, table: Tag):
        # FIXME: подумать над тем, чтобы self.table сделать приватным атрибутом self._table или даже self.__table
        self.table: Tag = table
        super().__init__()

    def _prepare(self):
        self._collect()
        super()._prepare()

    @abstractmethod
    def _collect(self): pass


class PrepareParentDataSliceBase(PrepareMethodsBase):

    def __init__(self, data: list):
        # FIXME: подумать над тем почему мы не используем list.copy(), вроде как нужно использовать
        #  НАВЕРНЕО НЕ НУЖНО, Т,К В КЛАССАХ МЫ ДЕЛАЕМ СРЕЗ [:...], а он вроде как копирует часть списка, и создает новый
        super().__init__(data=data)


class PrepareParentBase(PrepareMethodsBase):

    def __init__(self, parent: PrepareMethodsBase):
        self.parent = deepcopy(parent)
        self.final_len: Final[int] = parent.final_len
        super().__init__()

    # @PrepareMethodsBase.final_len.setter
    # def final_len(self, final_len):
    #     self._final_len = final_len


class PrepareParentNoCopyBase(PrepareMethodsBase):

    def __init__(self, parent: PrepareMethodsBase):
        self.parent = parent
        self.final_len: Final[int] = parent.final_len
        super().__init__()

    # @PrepareMethodsBase.final_len.setter
    # def final_len(self, final_len):
    #     self._final_len = final_len


def convert_to_schemas(schema: [BaseModel]):
    def _check_lens_lists(data: dict[str, list]):
        if len(set(map(len, data.values()))) != 1:
            raise FatalCreateError(f"Списки data для создания схем {schema} разной длинны")

    def convert(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> list[schema]:
            data: dict[str, list] = func(*args, **kwargs)

            _check_lens_lists(data)

            items: list[dict[str, Any]] = []

            for i in range(len(list(data.values())[0])):
                item: dict[str, Any] = {}
                for name, value in data.items():
                    item[name] = value[i]

                items.append(item)

            return parse_obj_as(list[schema], items)

        return wrapper

    return convert


class PrepareError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return self.message
