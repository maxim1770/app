from typing import Final

__PUNCTUATION_MARKS: Final[list[str]] = [',', '.', ';', ':', '!', '?']


def clean_extra_spaces(some_text: str) -> str:
    some_text = ' '.join(some_text.split()).strip()
    return some_text


def remove_extra_end_letter(some_text: str) -> str:
    if some_text[-1] in __PUNCTUATION_MARKS or some_text.endswith(' и'):
        some_text = some_text[:-1]
    return some_text


def remove_extra_first_letter(some_text: str) -> str:
    if some_text[0] in __PUNCTUATION_MARKS or some_text.startswith('и '):
        some_text = some_text[1:]
    return some_text


def remove_extra_space_before_punctuation_marks(some_text: str) -> str:
    for punctuation_mark in __PUNCTUATION_MARKS:
        some_text = some_text.replace(' ' + punctuation_mark, punctuation_mark)
    return some_text


def prepare_dash(some_text: str) -> str:
    some_text = some_text.replace('—', '-').replace('–', '-')
    some_text = some_text.replace(' -', '-').replace('- ', '-')
    return some_text


def common_prepare_text(some_text: str) -> str:
    """
    WARNING: Убирает точку с конца предложения
    """
    some_text: str = clean_extra_spaces(some_text)
    some_text: str = remove_extra_space_before_punctuation_marks(some_text)
    some_text: str = prepare_dash(some_text)
    some_text: str = remove_extra_end_letter(some_text)
    some_text: str = remove_extra_first_letter(some_text)
    some_text: str = clean_extra_spaces(some_text)
    return some_text


def set_first_letter_upper(some_text: str) -> str:
    some_text = some_text[0].upper() + some_text[1:]
    return some_text
