import re
from pathlib import Path
from uuid import UUID

from app import enums, const, models
from .collect_manuscript import PrepareManuscriptPathFactory
from ..object_storage import ObjectStorage


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


def __is_nlr_manuscript_code(manuscript_code: UUID | str) -> bool:
    manuscript_code: str = str(manuscript_code)
    if len(manuscript_code) == 36:
        return True
    return False


def __is_lls_manuscript_code(manuscript_code: str) -> bool:
    if manuscript_code.startswith('lls'):
        return True
    return False


def __is_lls_rus_1_10_manuscript_code(manuscript_code: str) -> bool:
    if manuscript_code in [f'lls_book_rus_{i}' for i in range(1, 11)]:
        return True
    return False


def manuscript_has_left_and_right(
        neb_slug: str | None,
        *,
        manuscript_code: str,
) -> bool:
    if neb_slug or __is_lls_manuscript_code(manuscript_code):
        return True
    return False


def prepare_manuscript_url(manuscript_code: UUID | str) -> str:
    manuscript_code: str = str(manuscript_code)
    if is_rsl_manuscript_code(manuscript_code):
        manuscript_url: str = f'{const.RslUrl.GET_MANUSCRIPT}/{_combine_fund_with_manuscript_code(manuscript_code)}'
    elif __is_nlr_manuscript_code(manuscript_code):
        manuscript_url: str = f'{const.NlrUrl.GET_MANUSCRIPT}?ab={manuscript_code}'
    elif __is_lls_manuscript_code(manuscript_code):
        if __is_lls_rus_1_10_manuscript_code(manuscript_code):
            runivers_all_lls_url: str = const.RuniversUrl.GET_ALl_Lls_FOR_RUS_1_10
        else:
            runivers_all_lls_url: str = const.RuniversUrl.GET_ALl_Lls
        runivers_lls_id: int = const.RuniversLlsId[manuscript_code.replace("-", "_")]
        manuscript_url: str = f'{runivers_all_lls_url}/{runivers_lls_id}'
    return manuscript_url


def prepare_manuscript_neb_url(manuscript_neb_slug: str) -> str:
    manuscript_neb_slug: str = f'{const.NebUrl.GET_MANUSCRIPT_DATA}/{manuscript_neb_slug}'
    return manuscript_neb_slug


def assemble_manuscript_path(manuscript: models.Manuscript) -> Path:
    if manuscript.fund:
        path: Path = PrepareManuscriptPathFactory.from_lib(
            fund_title=manuscript.fund.title,
            library_title=manuscript.fund.library,
            code=manuscript.code,
        )
    elif __is_lls_manuscript_code(manuscript.code):
        path: Path = PrepareManuscriptPathFactory.from_lls(
            code=manuscript.code
        )
    return path


def assemble_manuscript_pdf_path(manuscript: models.Manuscript, *, object_storage: ObjectStorage) -> Path:
    try:
        if manuscript.fund:
            created_pdf_path: Path = PrepareManuscriptPathFactory.from_lib(
                fund_title=manuscript.fund.title,
                library_title=manuscript.fund.library,
                code=manuscript.code,
                object_storage=object_storage
            ).created_pdf_path
        elif __is_lls_manuscript_code(manuscript.code):
            created_pdf_path: Path = PrepareManuscriptPathFactory.from_lls(
                code=manuscript.code,
                object_storage=object_storage
            ).created_pdf_path
    except FileNotFoundError as e:
        raise ValueError(e.args[0])
    else:
        return created_pdf_path
