from enum import StrEnum


class BookTitle(StrEnum):
    Prolog = 'Пролог'
    Zhitija_Svjatyh = 'Жития Святых'


class BookType(StrEnum):
    Slovo = 'Слово'
    Pouchenie = 'Поучение'
    Pritcha = 'Притча'
    Povest = 'Повесть'
    Nakazanie = 'Наказание'
    _istorija = 'история'
    slovo_istorija = f'{Slovo}-{_istorija}'
    pouchenie_istorija = f'{Pouchenie}-{_istorija}'


class BookSource(StrEnum):
    ot_Limonisa = 'от Лимониса'
    ot_Paterika = 'от Патерика'
    ot_Pandeka = 'от Пандека'


class BookTopic(StrEnum):
    o_Svjatyh_Ikonah = 'о Святых Иконах'
    o_Ljubvi = 'о Любви'
    o_Prichastii = 'о Причастии'
    o_Molitve = 'о Молитве'
    o_Smirennoj_Mudrosti = 'о Смиренной Мудрости'
    o_Smirenii = 'о Смирении'
    o_Dolgoterpenii = 'о Долготерпении'
    o_Terpenii = 'о Терпении'
    o_Pokajanii = 'о Покаянии'
    o_Ispovedanii_grehov = 'о Исповедании грехов'
    o_Dobrodeteli = 'о Добродетели'
    o_Poslushanii = 'о Послушании'
    o_Milostyni = 'о Милостыни'
    o_Molchanii = 'о Молчании'
    o_Nischeljubii = 'о Нищелюбии'
    ezhe_ne_osuzhdat = 'еже не осуждать'
    o_pomysle = 'о помысле'
    o_Nakazanii = 'о Наказании'
    o_Trude = 'о Труде'
    o_Tsarstvii_Nebesnom = 'о Царствии Небесном'
    o_muke_beskonechnoj = 'о муке бесконечной'
    o_Strashnom_Sude = 'о Страшном Суде'
    o_kljanuschihsja = 'о клянущихся'
    o_leni = 'о лени'
    o_zavisti = 'о зависти'
    o_sheptanii = 'о шептании'
    o_klevetanii = 'о клеветании'
    o_lzhivyh = 'о лживых'
    o_lihoimanii = 'о лихоимании'
    o_dajuschih_v_lihvu = 'о дающих в лихву'
    o_gneve = 'о гневе'
    o_derzosti = 'о дерзости'
    o_jarosti = 'о ярости'
    o_pjanstve = 'о пьянстве'
    o_objadenii = 'о объядении'
    o_usopshih = 'о усопших'

    o_Videnii = 'о Видении'


class BookUtil(StrEnum):
    Upominanie = 'Упоминание'
    Chudo = 'Чудо'
