from enum import StrEnum, auto


class BibleBookTestament(StrEnum):
    """OT - Old Testament, NT - New Testament"""
    new_testament = auto()
    old_testament = auto()


class BibleBookTestamentRu(StrEnum):
    """OT - Old Testament, NT - New Testament"""
    new_testament = 'Новый завет'
    old_testament = 'Ветхий завет'


class BibleBookPart(StrEnum):
    evangel = auto()
    apostle = auto()


class BibleBookPartRu(StrEnum):
    evangel = 'Евангелие'
    apostle = 'Апостол'


class BibleBookAbbr(StrEnum):
    # Евангелие
    Mk = auto()
    Mt = auto()
    Lk = auto()
    Jn = auto()

    # Деяния святых Апостолов
    Act = auto()

    # Соборные Послания
    Jac = auto()
    _1Pet = '1Pet'
    _2Pet = '2Pet'
    _1Jn = '1Jn'
    _2Jn = '2Jn'
    _3Jn = '3Jn'
    Juda = auto()

    # Послания Апостола Павла
    Rom = auto()
    _1Cor = '1Cor'
    _2Cor = '2Cor'
    Gal = auto()
    Eph = auto()
    Phil = auto()
    Col = auto()
    _1Thes = '1Thes'
    _2Thes = '2Thes'
    _1Tim = '1Tim'
    _2Tim = '2Tim'
    Tit = auto()
    Phlm = auto()
    Hebr = auto()

    # Апокалипсис
    Apok = auto()


class BibleBookAbbrRu(StrEnum):
    # Евангелие
    Jn = 'Ин'
    Lk = 'Лк'
    Mk = 'Мк'
    Mt = 'Мф'

    # Деяния святых Апостолов
    Act = 'Деян'

    # Соборные Послания
    Jac = 'Иак'
    _1Pet = '1 Пет'
    _2Pet = '2 Пет'
    _1Jn = '1 Ин'
    _2Jn = '2 Ин'
    _3Jn = '3 Ин'
    Juda = 'Иуд'

    # Послания Апостола Павла
    Rom = 'Рим'
    _1Cor = '1 Кор'
    _2Cor = '2 Кор'
    Gal = 'Гал'
    Eph = 'Еф'
    Phil = 'Флп'
    Col = 'Кол'
    # А тут https://azbyka.ru/biblia/?1Thes.1&r написано не '1 Сол', a '1 Фес' (написано, вверху в меню)
    _1Thes = '1 Сол'
    # Так же, написано не '2 Сол', а '2 Фес'
    _2Thes = '2 Сол'
    _1Tim = '1 Тим'
    _2Tim = '2 Тим'
    Tit = 'Тит'
    # НЕ ЧИТАЕТСЯ ПО ДНЯМ
    Phlm = 'Флм'
    Hebr = 'Евр'

    # Апокалипсис
    # НЕ ЧИТАЕТСЯ ПО ДНЯМ
    Apok = 'Откр'
