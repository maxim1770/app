from pydantic import BaseModel, conint, constr, Field

# CyrillicNumberMap_: tuple[tuple[str, int], ...] = (
#     ('Т', 10000), ('ц', 900), ('ѿ', 800), ('ѱ', 700), ('х', 600), ('ф', 500), ('у', 400), ('т', 300), ('с', 200),
#     ('р', 100), ('ч', 90), ('п', 80), ('о', 70), ('Ѯ', 60), ('н', 50), ('м', 40), ('л', 30), ('к', 20),
#     ('Ѳi', 19), ('иi', 18), ('зi', 17), ('si', 16), ('єi', 15), ('дi', 14), ('гi', 13), ('вi', 12),
#     ('аi', 11),
#     ('i', 10),
#     ('Ѳ', 9),
#     ('и', 8), ('з', 7), ('s', 6), ('є', 5), ('д', 4), ('г', 3), ('в', 2),
#     ('а', 1)
# )


class CyrillicNumberScheme(BaseModel):
    cyrillic: constr(min_length=1, max_length=2, regex=r"[ТцѿѱхфутсрчпоѮнмлкѲiѲизsєдгва]") = Field(default='')
    number: conint(strict=True, ge=1, le=10000) | None = Field(default=None)


class CyrillicNumberMapScheme(BaseModel):
    __root__: list[CyrillicNumberScheme]


class Cyrillic:
    CYRILLIC_NUMBER_MAP: CyrillicNumberMapScheme = CyrillicNumberMapScheme(__root__=[
        CyrillicNumberScheme(cyrillic="Т"
                             ,
                             number=10000
                             ),
        CyrillicNumberScheme(cyrillic="ц"
                             ,
                             number=900
                             ),
        CyrillicNumberScheme(cyrillic="ѿ"
                             ,
                             number=800
                             ),

        CyrillicNumberScheme(cyrillic="ѱ"
                             ,
                             number=700
                             ),

        CyrillicNumberScheme(cyrillic="х"
                             ,
                             number=600
                             ),

        CyrillicNumberScheme(cyrillic="ф"
                             ,
                             number=500
                             ),

        CyrillicNumberScheme(cyrillic="у"
                             ,
                             number=400
                             ),

        CyrillicNumberScheme(cyrillic="т"
                             ,
                             number=300
                             ),

        CyrillicNumberScheme(cyrillic="с"
                             ,
                             number=200
                             ),

        CyrillicNumberScheme(cyrillic="р"
                             ,
                             number=100
                             ),

        CyrillicNumberScheme(cyrillic="ч"
                             ,
                             number=90
                             ),

        CyrillicNumberScheme(cyrillic="п"
                             ,
                             number=80
                             ),

        CyrillicNumberScheme(cyrillic="о"
                             ,
                             number=70
                             ),

        CyrillicNumberScheme(cyrillic="Ѯ"
                             ,
                             number=60
                             ),

        CyrillicNumberScheme(cyrillic="н"
                             ,
                             number=50
                             ),

        CyrillicNumberScheme(cyrillic="м"
                             ,
                             number=40
                             ),

        CyrillicNumberScheme(cyrillic="л"
                             ,
                             number=30
                             ),

        CyrillicNumberScheme(cyrillic="к"
                             ,
                             number=20
                             ),

        CyrillicNumberScheme(cyrillic="Ѳi"
                             ,
                             number=19
                             ),

        CyrillicNumberScheme(cyrillic="иi"
                             ,
                             number=18
                             ),

        CyrillicNumberScheme(cyrillic="зi"
                             ,
                             number=17
                             ),

        CyrillicNumberScheme(cyrillic="si"
                             ,
                             number=16
                             ),

        CyrillicNumberScheme(cyrillic="єi"
                             ,
                             number=15
                             ),

        CyrillicNumberScheme(cyrillic="дi"
                             ,
                             number=14
                             ),

        CyrillicNumberScheme(cyrillic="гi"
                             ,
                             number=13
                             ),

        CyrillicNumberScheme(cyrillic="вi"
                             ,
                             number=12
                             ),

        CyrillicNumberScheme(cyrillic="аi"
                             ,
                             number=11
                             ),

        CyrillicNumberScheme(cyrillic="i"
                             ,
                             number=10
                             ),

        CyrillicNumberScheme(cyrillic="Ѳ"
                             ,
                             number=9
                             ),

        CyrillicNumberScheme(cyrillic="и"
                             ,
                             number=8
                             ),

        CyrillicNumberScheme(cyrillic="з"
                             ,
                             number=7
                             ),

        CyrillicNumberScheme(cyrillic="s"
                             ,
                             number=6
                             ),

        CyrillicNumberScheme(cyrillic="є"
                             ,
                             number=5
                             ),

        CyrillicNumberScheme(cyrillic="д"
                             ,
                             number=4
                             ),

        CyrillicNumberScheme(cyrillic="г"
                             ,
                             number=3
                             ),

        CyrillicNumberScheme(cyrillic="в"
                             ,
                             number=2
                             ),

        CyrillicNumberScheme(cyrillic="а"
                             ,
                             number=1
                             ),
    ])

    @classmethod
    def to_cyrillic(cls, number: int) -> str:
        """convert integer to cyrillic number
        """
        # if not isinstance(n, int):
        #     raise NotIntegerError("decimals can not be converted")
        # if not (-1 < n < 5000):
        #     raise OutOfRangeError("number out of range (must be 0..4999)")

        cyr_num_scheme: CyrillicNumberScheme = CyrillicNumberScheme(number=number)

        for const_scheme in cls.CYRILLIC_NUMBER_MAP.__root__:
            while cyr_num_scheme.number >= const_scheme.number:
                cyr_num_scheme.cyrillic += const_scheme.cyrillic
                cyr_num_scheme.number -= const_scheme.number

        return cyr_num_scheme.cyrillic


if __name__ == '__main__':
    # sn = CyrillicNumberScheme(cyrillic="аi")
    # print(sn)
    c = Cyrillic.to_cyrillic(5)
    print(type(c))


# # Define pattern to detect valid cyrillic numbers
# CyrillicnumberPattern = re.compile("""
#     ^                   # beginning of string
#     M{0,4}              # thousands - 0 to 4 M's
#     (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
#                         #            or 500-800 (D, followed by 0 to 3 C's)
#     (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
#                         #        or 50-80 (L, followed by 0 to 3 X's)
#     (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
#                         #        or 5-8 (V, followed by 0 to 3 I's)
#     $                   # end of string
#     """, re.VERBOSE)


# def from_cyrillic(s: str) -> int:
#     """convert cyrillic number to integer"""
#     if not s:
#         raise InvalidCyrillicnumberError('Input can not be blank')
#
#     # special case
#     if s == 'N':
#         return 0
#
#     # if not CyrillicnumberPattern.search(s):
#     #     raise InvalidCyrillicnumberError('Invalid cyrillic number: %s' % s)
#
#     result: int = 0
#     index: int = 0
#     for number, integer in CyrillicnumberMap:
#         if len(s) == index:
#             break
#
#         if s[index] == number:
#
#             result += integer
#             index += 1
#
#     if len(s) != index:
#         """
#         Если index не равен длине строки, значит какие то символы из строки s не были считаны
#         Вроде как такое может быть, только если строка == s: {Xаi, Xвi, Xгi, ...}, где X набор других символов
#         Значит мы просто добавим 10 к result
#         """
#         result += 10
#
#     return result
