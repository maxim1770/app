from enum import StrEnum


def enum2regex(str_enum: [StrEnum], group: StrEnum = None) -> str:
    regex_group: str = f'?P<{group}>' if group else ''
    regex_str: str = f'({regex_group}' + '|'.join([word.replace(' ', '\s') for word in str_enum]) + ')'
    return regex_str
