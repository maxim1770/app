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
    Mt = auto()
    Mk = auto()
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
    Mt = 'Мф'
    Mk = 'Мк'
    Lk = 'Лк'
    Jn = 'Ин'

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


class BibleBookAuthorSlug(StrEnum):
    # Евангелие
    Mt = 'matfej-levij'
    Mk = 'mark-evangelist'
    Lk = 'luka-evangelist'
    Jn = 'ioann-bogoslov'

    # Деяния святых Апостолов
    Act = 'luka-evangelist'

    # Соборные Послания
    Jac = 'iakov-zevedeev'
    _1Pet = 'petr-do-prizvanija-simon'
    _2Pet = 'petr-do-prizvanija-simon'
    _1Jn = 'ioann-bogoslov'
    _2Jn = 'ioann-bogoslov'
    _3Jn = 'ioann-bogoslov'
    Juda = 'iuda-iakovlev-levvej'

    # Послания Апостола Павла
    Rom = 'pavel-pervoverhovnyj-apostol'
    _1Cor = 'pavel-pervoverhovnyj-apostol'
    _2Cor = 'pavel-pervoverhovnyj-apostol'
    Gal = 'pavel-pervoverhovnyj-apostol'
    Eph = 'pavel-pervoverhovnyj-apostol'
    Phil = 'pavel-pervoverhovnyj-apostol'
    Col = 'pavel-pervoverhovnyj-apostol'
    _1Thes = 'pavel-pervoverhovnyj-apostol'
    _2Thes = 'pavel-pervoverhovnyj-apostol'
    _1Tim = 'pavel-pervoverhovnyj-apostol'
    _2Tim = 'pavel-pervoverhovnyj-apostol'
    Tit = 'pavel-pervoverhovnyj-apostol'
    Phlm = 'pavel-pervoverhovnyj-apostol'
    Hebr = 'pavel-pervoverhovnyj-apostol'

    # Апокалипсис
    Apok = 'ioann-bogoslov'
