from enum import StrEnum


class FaceSanctityTitle(StrEnum):
    """
        l: list = [
        'апостол', 'апостол от 70-ти', 'равноапостольный', 'равноапостольная',
        'ветхозаветный патриарх',
        'пророк', 'пророчица',
        'Христа ради юродивый',
        'великомученица', 'великомученик', 'мученица', 'мученик', 'преподобномученица', 'преподобномученик',
        'священномученик',
        'исповедник', 'исповедница',
        'бессребреник',
        'блаженный', 'блаженная',
        'благоверный', 'благоверная', 'благоверный князь', 'благоверная княгиня',
        'праведный', 'праведная',
        'преподобный', 'преподобная',
        'святой', 'святая',
        'святитель',
    ]

    """
    apostol = 'Апостол'
    apostol_ot_70_ti = 'Апостол от 70-ти'
    ravnoapostolnyj = 'Равноапостольный'
    ravnoapostolnaja = 'Равноапостольная'

    vethozavetnyj_patriarh = 'Ветхозаветный Патриарх'

    prorok = 'Пророк'
    prorochitsa = 'Пророчица'

    Hrista_radi_jurodivyj = 'Христа ради Юродивый'

    velikomuchenitsa = 'Великомученица'
    velikomuchenik = 'Великомученик'
    muchenitsa = 'Мученица'
    muchenik = 'Мученик'
    prepodobnomuchenitsa = 'Преподобномученица'
    prepodobnomuchenik = 'Преподобномученик'
    svjaschennomuchenik = 'Священномученик'

    ispovednik = 'Исповедник'
    ispovednitsa = 'Исповедница'

    bessrebrenik = 'Бессребреник'

    blazhennyj = 'Блаженный'
    blazhennaja = 'Блаженная'

    blagovernyj = 'Благоверный'
    blagovernaja = 'Благоверная'
    blagovernyj_knjaz = 'Благоверный Князь'
    blagovernaja_knjaginja = 'Благоверная Княгиня'

    pravednyj = 'Праведный'
    pravednaja = 'Праведная'

    prepodobnyj = 'Преподобный'
    prepodobnaja = 'Преподобная'

    svjatoj = 'Святой'
    svjataja = 'Святая'

    svjatitel = 'Святитель'


class FaceSanctityAbbr(StrEnum):
    svjaschennomuchenik = 'Сщмч'
    prepodobnyj = 'Прп'
    pravednyj = 'Прав'
    prepodobnomuchenik = 'Прмч'
    prepodobnomuchenitsa = 'Прмц'
    ravnoapostolnyj = 'Равноап'
    muchenik = 'Мч'
    muchenitsa = 'Мц'
    svjatitel = 'Свт'
    apostol = 'Ап'
    ispovednik = 'Исп'
