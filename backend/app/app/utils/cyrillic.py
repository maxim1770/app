from pydantic import BaseModel, conint, constr, Field


class _CyrillicNumberScheme(BaseModel):
    cyrillic: constr(min_length=1, max_length=2, regex=r"[ТцѿѱхфутсрчпоѮнмлкѲiѲизsєдгва]") = Field(default='')
    number: conint(strict=True, ge=1, le=10000) | None = Field(default=None)


class _CyrillicNumberMapScheme(BaseModel):
    __root__: list[_CyrillicNumberScheme]


class Cyrillic:
    _CyrillicNumberMap: list[tuple[str, int], ...] = [
        ('Т', 10000), ('ц', 900), ('ѿ', 800), ('ѱ', 700), ('х', 600), ('ф', 500), ('у', 400), ('т', 300), ('с', 200),
        ('р', 100), ('ч', 90), ('п', 80), ('о', 70), ('Ѯ', 60), ('н', 50), ('м', 40), ('л', 30), ('к', 20),
        ('Ѳi', 19), ('иi', 18), ('зi', 17), ('si', 16), ('єi', 15), ('дi', 14), ('гi', 13), ('вi', 12), ('аi', 11),
        ('i', 10), ('Ѳ', 9), ('и', 8), ('з', 7), ('s', 6), ('є', 5), ('д', 4), ('г', 3), ('в', 2), ('а', 1)
    ]

    _CYRILLIC_NUMBER_MAP: _CyrillicNumberMapScheme = _CyrillicNumberMapScheme(__root__=[
        _CyrillicNumberScheme(cyrillic="Т"
                              ,
                              number=10000
                              ),
        _CyrillicNumberScheme(cyrillic="ц"
                              ,
                              number=900
                              ),
        _CyrillicNumberScheme(cyrillic="ѿ"
                              ,
                              number=800
                              ),

        _CyrillicNumberScheme(cyrillic="ѱ"
                              ,
                              number=700
                              ),

        _CyrillicNumberScheme(cyrillic="х"
                              ,
                              number=600
                              ),

        _CyrillicNumberScheme(cyrillic="ф"
                              ,
                              number=500
                              ),

        _CyrillicNumberScheme(cyrillic="у"
                              ,
                              number=400
                              ),

        _CyrillicNumberScheme(cyrillic="т"
                              ,
                              number=300
                              ),

        _CyrillicNumberScheme(cyrillic="с"
                              ,
                              number=200
                              ),

        _CyrillicNumberScheme(cyrillic="р"
                              ,
                              number=100
                              ),

        _CyrillicNumberScheme(cyrillic="ч"
                              ,
                              number=90
                              ),

        _CyrillicNumberScheme(cyrillic="п"
                              ,
                              number=80
                              ),

        _CyrillicNumberScheme(cyrillic="о"
                              ,
                              number=70
                              ),

        _CyrillicNumberScheme(cyrillic="Ѯ"
                              ,
                              number=60
                              ),

        _CyrillicNumberScheme(cyrillic="н"
                              ,
                              number=50
                              ),

        _CyrillicNumberScheme(cyrillic="м"
                              ,
                              number=40
                              ),

        _CyrillicNumberScheme(cyrillic="л"
                              ,
                              number=30
                              ),

        _CyrillicNumberScheme(cyrillic="к"
                              ,
                              number=20
                              ),

        _CyrillicNumberScheme(cyrillic="Ѳi"
                              ,
                              number=19
                              ),

        _CyrillicNumberScheme(cyrillic="иi"
                              ,
                              number=18
                              ),

        _CyrillicNumberScheme(cyrillic="зi"
                              ,
                              number=17
                              ),

        _CyrillicNumberScheme(cyrillic="si"
                              ,
                              number=16
                              ),

        _CyrillicNumberScheme(cyrillic="єi"
                              ,
                              number=15
                              ),

        _CyrillicNumberScheme(cyrillic="дi"
                              ,
                              number=14
                              ),

        _CyrillicNumberScheme(cyrillic="гi"
                              ,
                              number=13
                              ),

        _CyrillicNumberScheme(cyrillic="вi"
                              ,
                              number=12
                              ),

        _CyrillicNumberScheme(cyrillic="аi"
                              ,
                              number=11
                              ),

        _CyrillicNumberScheme(cyrillic="i"
                              ,
                              number=10
                              ),

        _CyrillicNumberScheme(cyrillic="Ѳ"
                              ,
                              number=9
                              ),

        _CyrillicNumberScheme(cyrillic="и"
                              ,
                              number=8
                              ),

        _CyrillicNumberScheme(cyrillic="з"
                              ,
                              number=7
                              ),

        _CyrillicNumberScheme(cyrillic="s"
                              ,
                              number=6
                              ),

        _CyrillicNumberScheme(cyrillic="є"
                              ,
                              number=5
                              ),

        _CyrillicNumberScheme(cyrillic="д"
                              ,
                              number=4
                              ),

        _CyrillicNumberScheme(cyrillic="г"
                              ,
                              number=3
                              ),

        _CyrillicNumberScheme(cyrillic="в"
                              ,
                              number=2
                              ),

        _CyrillicNumberScheme(cyrillic="а"
                              ,
                              number=1
                              ),
    ])

    @classmethod
    def to_cyrillic(cls, num: int) -> str:
        cyr_num_scheme = _CyrillicNumberScheme(number=num)
        for const_scheme in cls._CYRILLIC_NUMBER_MAP.__root__:
            while cyr_num_scheme.number >= const_scheme.number:
                cyr_num_scheme.cyrillic += const_scheme.cyrillic
                cyr_num_scheme.number -= const_scheme.number
        return cyr_num_scheme.cyrillic

    @classmethod
    def from_cyrillic(cls, cyrillic: str) -> int:
        num: int = 0
        for tuple_ in cls._CyrillicNumberMap:
            if tuple_[0] == cyrillic:
                num = tuple_[1]
                return num
        for symbol in list(cyrillic):
            num += [tuple_[1] for tuple_ in cls._CyrillicNumberMap if tuple_[0] == symbol][0]
        return num
