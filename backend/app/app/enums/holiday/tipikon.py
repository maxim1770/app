from enum import StrEnum, IntEnum


class TipikonTitle(StrEnum):
    Velikij_Prazdnik = 'Великий Праздник'
    Srednij_Prazdnik_Vsenoschnoe_Bdenie = 'Средний Праздник (Всенощное Бдение)'
    Srednij_Prazdnik = 'Средний Праздник'
    Malyj_Prazdnik_Slavoslovnaja_Sluzhba = 'Малый Праздник (Славословная Служба)'
    Malyj_Prazdnik = 'Малый Праздник'


class TipikonPriority(IntEnum):
    Velikij_Prazdnik = 1
    Srednij_Prazdnik_Vsenoschnoe_Bdenie = 2
    Srednij_Prazdnik = 3
    Malyj_Prazdnik_Slavoslovnaja_Sluzhba = 4
    Malyj_Prazdnik = 5
