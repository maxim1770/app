from enum import StrEnum, IntEnum


class FaceSanctityTitle(StrEnum):
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


class Gender(IntEnum):
    man = 1
    woman = 2


class SaintGender(IntEnum):
    apostol = Gender.man
    apostol_ot_70_ti = Gender.man
    ravnoapostolnyj = Gender.man
    ravnoapostolnaja = Gender.woman

    vethozavetnyj_patriarh = Gender.man

    prorok = Gender.man
    prorochitsa = Gender.woman

    Hrista_radi_jurodivyj = Gender.man

    velikomuchenitsa = Gender.woman
    velikomuchenik = Gender.man
    muchenitsa = Gender.woman
    muchenik = Gender.man
    prepodobnomuchenitsa = Gender.woman
    prepodobnomuchenik = Gender.man
    svjaschennomuchenik = Gender.man

    ispovednik = Gender.man
    ispovednitsa = Gender.woman

    bessrebrenik = Gender.man

    blazhennyj = Gender.man
    blazhennaja = Gender.woman

    blagovernyj = Gender.man
    blagovernaja = Gender.woman
    blagovernyj_knjaz = Gender.man
    blagovernaja_knjaginja = Gender.woman

    pravednyj = Gender.man
    pravednaja = Gender.woman

    prepodobnyj = Gender.man
    prepodobnaja = Gender.woman

    svjatoj = Gender.man
    svjataja = Gender.woman

    svjatitel = Gender.man
