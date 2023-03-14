import re


def combine_fund_with_manuscript_code(manuscript_code: str) -> str:
    fund: str = manuscript_code[manuscript_code.find('-') + 1: manuscript_code.rfind('-')]
    if not fund.isdigit():
        fond_num: str = re.search(r'\d+', fund)[0]
        fund = fund.replace(fond_num, f'{fond_num}-')
    return f'{fund}/{manuscript_code}'
