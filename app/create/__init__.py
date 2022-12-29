from typing import Final

from app.create.prepare.base_classes import PrepareMethodsBase, PrepareParentBase, PrepareParentDataSliceBase


class PrepareC2MovableDayAbbr(PrepareMethodsBase):
    final_len: Final[int] = 4

    def __init__(self):
        super().__init__()

    def _fill_gaps(self):
        self.data = [1, 2, 3, 4]

    def _clean(self): pass

    def _convert(self): pass


class PrepareC1Sunday(PrepareParentBase):

    def __init__(self, parent_prepare: PrepareC2MovableDayAbbr):
        super().__init__(parent_prepare)

    def _fill_gaps(self):
        self.data = list(map(str, self.parent.data))

    def _clean(self): pass

    def _convert(self): pass


class PrepareC2Sunday(PrepareParentDataSliceBase):
    final_len: Final[int] = 2

    def __init__(self, parent_prepare: PrepareC2MovableDayAbbr):
        super().__init__(parent_prepare.data[:self.final_len])

    def _fill_gaps(self):
        self.data = [i ** 2 for i in self.data]

    def _clean(self): pass

    def _convert(self): pass


def my_test_base_classes():
    # p = PrepareBase_()
    # p.data = [1, 2]
    # print(p.__dict__)
    # print(p.data)

    # print(PrepareC2MovableDayAbbr.__dict__)
    # print(PrepareC2MovableDayAbbr.final_len)

    d = PrepareC2MovableDayAbbr()
    print(d.__dict__)
    print(d.data)

    da = PrepareC1Sunday(d)
    print(da.__dict__)
    print(da.data)

    da2 = PrepareC2Sunday(d)
    print(da2.__dict__)
    print(da2.data)


if __name__ == '__main__':
    my_test_base_classes()
