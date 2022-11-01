from abc import ABC, abstractmethod

from bs4.element import Tag


class PrepareBase(ABC):

    def __init__(self, data: list | None, *, table: Tag | None = None):
        self.data = data

        self.collect(table)
        self.fill_gaps()
        self.clean()
        self.convert()
        self.process()

        if len(self.data) != self.final_len:
            raise ValueError(f"После prepare массив должен быть длинной: {self.final_len}")

    @property
    @abstractmethod
    def final_len(self):
        pass

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @abstractmethod
    def collect(self, table: Tag | None):
        pass

    @abstractmethod
    def fill_gaps(self):
        pass

    @abstractmethod
    def clean(self):
        pass

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def process(self):
        pass
