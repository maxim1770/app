# Define exceptions
class CyrillicError(Exception):
    pass


class OutOfRangeError(CyrillicError):
    pass


class NotIntegerError(CyrillicError):
    pass


class InvalidCyrillicNumeralError(CyrillicError):
    pass


# Define digit mapping
CyrillicNumeralMap: tuple[tuple[str, int], ...] = (
    ('Т', 10000), ('ц', 900), ('ѿ', 800), ('ѱ', 700), ('х', 600), ('ф', 500), ('у', 400), ('т', 300), ('с', 200),
    ('р', 100), ('ч', 90), ('п', 80), ('о', 70), ('Ѯ', 60), ('н', 50), ('м', 40), ('л', 30), ('к', 20), ('i', 10),
    ('Ѳ', 9),
    ('и', 8), ('з', 7), ('s', 6), ('є', 5), ('д', 4), ('г', 3), ('в', 2),
    ('а', 1)
)


def __to_cyrillic_11_19(n: int) -> str:
    """

    CyrillicNumeralMap[START_OF_DIGITS_IN_MAP:]:
    (('Ѳ', 9), ('и', 8), ('з', 7), ('s', 6), ('є', 5), ('д', 4), ('г', 3), ('в', 2), ('а', 1))
    """

    # Знаем что n: [11, 19], поэтому, без проверок, отнимаем 10
    n: int = n - 10
    START_OF_DIGITS_IN_MAP: int = 19
    for numeral, integer in CyrillicNumeralMap[START_OF_DIGITS_IN_MAP:]:
        if n == integer:
            return f'{numeral}i'


def to_cyrillic(n: int) -> str:
    """convert integer to cyrillic numeral
    """
    if not isinstance(n, int):
        raise NotIntegerError("decimals can not be converted")
    if not (-1 < n < 5000):
        raise OutOfRangeError("number out of range (must be 0..4999)")

    # special case
    if n == 0:
        return 'N'

    result = ""
    for numeral, integer in CyrillicNumeralMap:
        if n >= integer:

            # Мой код
            if 10 < n < 20:
                result += __to_cyrillic_11_19(n)
                break

            result += numeral
            n -= integer

    return result


# # Define pattern to detect valid cyrillic numerals
# CyrillicNumeralPattern = re.compile("""
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


def from_cyrillic(s: str) -> int:
    """convert cyrillic numeral to integer"""
    if not s:
        raise InvalidCyrillicNumeralError('Input can not be blank')

    # special case
    if s == 'N':
        return 0

    # if not CyrillicNumeralPattern.search(s):
    #     raise InvalidCyrillicNumeralError('Invalid cyrillic numeral: %s' % s)

    result: int = 0
    index: int = 0
    for numeral, integer in CyrillicNumeralMap:
        if len(s) == index:
            break

        if s[index] == numeral:

            result += integer
            index += 1

    if len(s) != index:
        """
        Если index не равен длине строки, значит какие то символы из строки s не были считаны
        Вроде как такое может быть, только если строка == s: {Xаi, Xвi, Xгi, ...}, где X набор других символов
        Значит мы просто добавим 10 к result
        """
        result += 10

    return result
