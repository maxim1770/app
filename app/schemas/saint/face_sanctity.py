from enum import Enum

from pydantic import BaseModel

from app.schemas.saint.saint import Saint


class FaceSanctityTitle(str, Enum):
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
    apostol = 'апостол'
    apostol_ot_70_ti = 'апостол от 70-ти'
    ravnoapostolnyj = 'равноапостольный'
    ravnoapostolnaja = 'равноапостольная'

    vethozavetnyj_patriarh = 'ветхозаветный патриарх'

    prorok = 'пророк'
    prorochitsa = 'пророчица'

    Hrista_radi_jurodivyj = 'Христа ради юродивый'

    velikomuchenitsa = 'великомученица'
    velikomuchenik = 'великомученик'
    muchenitsa = 'мученица'
    muchenik = 'мученик'
    prepodobnomuchenitsa = 'преподобномученица'
    prepodobnomuchenik = 'преподобномученик'
    svjaschennomuchenik = 'священномученик'

    ispovednik = 'исповедник'
    ispovednitsa = 'исповедница'

    bessrebrenik = 'бессребреник'

    blazhennyj = 'блаженный'
    blazhennaja = 'блаженная'

    blagovernyj = 'благоверный'
    blagovernaja = 'благоверная'
    blagovernyj_knjaz = 'благоверный князь'
    blagovernaja_knjaginja = 'благоверная княгиня'

    pravednyj = 'праведный'
    pravednaja = 'праведная'

    prepodobnyj = 'преподобный'
    prepodobnaja = 'преподобная'

    svjatoj = 'святой'
    svjataja = 'святая'

    svjatitel = 'святитель'


class FaceSanctityBase(BaseModel):
    title: FaceSanctityTitle


class FaceSanctityCreate(FaceSanctityBase):
    pass


class FaceSanctity(FaceSanctityBase):
    id: int

    saints: list[Saint] = []

    class Config:
        orm_mode = True
