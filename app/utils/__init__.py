from .manuscript import combine_fund_with_manuscript_code


def enum2regex(str_enum) -> str:
    regex_str: str = '(' + '|'.join([word.replace(' ', '\s') for word in str_enum]) + ')'
    return regex_str
