import re
from uuid import UUID

from app import enums, const


def _combine_fund_with_manuscript_code(manuscript_code: str) -> str:
    fund: str = manuscript_code[manuscript_code.find('-') + 1: manuscript_code.rfind('-')]
    if not fund.isdigit():
        fond_num: str = re.search(r'\d+', fund)[0]
        fund = fund.replace(fond_num, f'{fond_num}-')
    return f'{fund}/{manuscript_code}'


def is_rsl_manuscript_code(manuscript_code: UUID | str) -> bool:
    manuscript_code: str = str(manuscript_code)
    if const.REGEX_RSL_MANUSCRIPT_CODE.match(manuscript_code):
        return True
    return False


def is_rsl_manuscript_code_title(manuscript_code_title: str) -> bool:
    if manuscript_code_title[:2] == 'Ф.':
        return True
    return False


def is_rsl_library(fund_title: enums.FundTitle) -> bool:
    if is_rsl_manuscript_code_title(fund_title):
        return True
    return False


def is_nlr_manuscript_code(manuscript_code: UUID | str) -> bool:
    manuscript_code: str = str(manuscript_code)
    if len(manuscript_code) == 36:
        return True
    return False


def prepare_manuscript_url(manuscript_code: UUID | str) -> str:
    manuscript_code: str = str(manuscript_code)
    if is_rsl_manuscript_code(manuscript_code):
        manuscript_url: str = f'{const.RslUrl.GET_MANUSCRIPT}/{_combine_fund_with_manuscript_code(manuscript_code)}'
    elif is_nlr_manuscript_code(manuscript_code):
        manuscript_url: str = f'{const.NlrUrl.GET_MANUSCRIPT}?ab={manuscript_code}'
    elif manuscript_code in [f'lls_book_rus_{i}' for i in range(1, 11)]:
        manuscript_url: str = f'{const.RuniversUrl.GET_LLS_FOR_RUS_1_10}/{manuscript_code}'
    else:
        manuscript_url: str = f'{const.RuniversUrl.GET_LLS}/{manuscript_code}'
    return manuscript_url


def prepare_manuscript_neb_url(manuscript_neb_slug: str) -> str:
    manuscript_neb_slug: str = f'{const.NebUrl.GET_MANUSCRIPT_DATA}/{manuscript_neb_slug}'
    return manuscript_neb_slug
