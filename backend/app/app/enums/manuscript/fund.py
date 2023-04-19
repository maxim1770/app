from enum import StrEnum


class FundTitle(StrEnum):
    # Так же иногда записано как: 'Q.п.I.', то таких Рукописей меньше, чем по запросу 'F.I' :  # https://nlr.ru/manuscripts/RA1527/elektronnyiy-katalog?ab=BF5DE157-EB98-464E-B118-B65E04885253
    # Иногда записано так: 'O.I' : https://nlr.ru/manuscripts/RA1527/elektronnyiy-katalog?ab=BADB534A-3512-419F-AA6B-016F5F240FAF
    f_i = 'F.I'
    sol = 'Сол'
    sof = 'Соф'
    gilf = 'Гильф'
    pogod = 'Погод'
    kir_bel = 'Кир.-Бел'
    georgij = 'Георгий'

    f_7 = 'Ф.7'
    f_37 = 'Ф.37'
    f_87 = 'Ф.87'
    f_98 = 'Ф.98'
    f_113 = 'Ф.113'
    f_173i = 'Ф.173/I'
    f_256 = 'Ф.256'
    f_304i = 'Ф.304/I'
    f_304iii = 'Ф.304/III'
    f_556 = 'Ф.556'


class LibraryTitle(StrEnum):
    nlr = 'РНБ'
    rsl = 'РГБ'
