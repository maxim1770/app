from enum import StrEnum


class BookTitle(StrEnum):
    Prolog = 'Пролог'
    Paterik = 'Патерик'
    Zhitija_Svjatyh = 'Жития Святых'
    Sluzhby_i_Zhitija_Svjatyh = 'Службы и Жития Святых'
    Mesjatseslov = 'Месяцеслов'
    Sbornik_Slov = 'Сборник Слов'
    Sbornik_Slov_i_Zhitij = 'Сборник Слов и Житий'
    Sinaksar = 'Синаксарь'
    Evangelie = 'Евангелие'
    Evangelie_uchitelnoe = 'Евангелие учительное'
    Evangelie_tolkovoe = 'Евангелие толковое'
    Apostol = 'Апостол'
    Apostol_tolkovyj = 'Апостол толковый'
    Psaltyr = 'Псалтырь'
    Psaltyr_tolkovaja = 'Псалтырь толковая'
    Kormchaja = 'Кормчая'
    Lls = 'ЛЛС'


class BookType(StrEnum):
    Slovo = 'Слово'
    Oglashenie = 'Оглашение'
    Skazanie = 'Сказание'
    Pouchenie = 'Поучение'
    Pritcha = 'Притча'
    Povest = 'Повесть'
    Poslanie = 'Послание'
    Pohvala = 'Похвала'
    Slovo_Pohvalnoe = 'Слово Похвальное'
    Slovo_Vospominatelnoe = 'Слово Воспоминательное'
    Prolog = 'Пролог'
    Beseda = 'Беседа'
    Sluzhba = 'Служба'
    Nakazanie = 'Наказание'
    Nravouchenie = 'Нравоучение'
    Glavy = 'Главы'
    _istorija = 'история'
    slovo_istorija = f'{Slovo}-{_istorija}'
    pouchenie_istorija = f'{Pouchenie}-{_istorija}'
    Sinaksar = 'Синаксарь'
    Zachalo = 'Зачало'
    Psalom = 'Псалом'
    Pravilo = 'Правило'
    Tropar = 'Тропарь'
    Kondak = 'Кондак'
    Molitva = 'Молитва'
    Stih = 'Стих'


class BookSource(StrEnum):
    ot_Limonisa = 'от Лимониса'
    ot_Paterika = 'от Патерика'
    ot_Pandeka = 'от Пандека'
    ot_Starchestva = 'от Старчества'


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

    o_smerti = 'о смерти'
    o_gordosti = 'о гордости'
    ezhe_ne_otchajatsja = 'еже не отчаяться'
    o_snah = 'о снах'
    o_rabah = 'о рабах'
    o_Svjatom_Prichastii = 'о Святом Причастии'
    o_suete = 'о суете'
    o_Kaznjah_Bozhiih = 'о Казнях Божиих'
    o_Proschenii_grehov = 'о Прощении грехов'
    o_Nravah_Dobryh = 'о Нравах Добрых'
    ezhe_Dobro_est_Truditsja_svoimi_rukami = 'еже Добро есть Трудиться своими руками'
    ezhe_ne_Propovedati_Bozhestva_nevernym = 'еже не Проповедати Божества неверным'
    o_mnogoimenii = 'о многоимении'
    o_Pochitanii_Knizhnom = 'о Почитании Книжном'
    o_Chesti_Iereistei = 'о Чести Иереистеи'
    o_Uchiteljah = 'о Учителях'
    o_Strannoljubii = 'о Страннолюбии'
    o_Upovanii_na_Boga = 'о Уповании на Бога'
    o_Episkopah = 'о Епископах'
    o_Svjaschennikah = 'о Священниках'
    o_Oblichenii = 'о Обличении'
    o_Srebroljubii = 'о Сребролюбии'
    o_pechali = 'о печали'
    o_Hitrosti_Knizhnoj = 'о Хитрости Книжной'
    o_zlobe = 'о злобе'
    o_sogreshajuschih_i_ne_Kajuschihsja = 'о согрешающих и не Кающихся'
    o_jadenii = 'о ядении'
    o_Epitimjah = 'о Епитимьях'

    o_Videnii = 'о Видении'


class BookUtil(StrEnum):
    Upominanie = 'Упоминание'
    Chudo = 'Чудо'
