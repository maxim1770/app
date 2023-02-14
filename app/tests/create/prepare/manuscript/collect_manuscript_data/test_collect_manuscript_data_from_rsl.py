from pathlib import Path

import pytest
import requests

from app import schemas, const, enums, utils
from app.core.config import settings
from app.create.prepare.manuscript.collect_manuscript_data import CollectManuscriptDataFromRsl


@pytest.mark.parametrize('manuscript_code, manuscript_data_any', [
    (
            'f-304iii-15',
            {
                'manuscript_title': 'Евангелие-тетр (Евангелие Исаака Бирёва)',
                'manuscript_code_title': 'Ф.304/III №15',
                'year_in': schemas.YearCreate(title='1531'),
                'fund_title': enums.FundTitle.f_304iii
            }
    ),
    (
            'f-173i-2',
            {
                'manuscript_title': 'Четвероевангелие',
                'manuscript_code_title': 'Ф.173/I №2',
                'year_in': None,
                'fund_title': enums.FundTitle.f_173i
            }
    ),
    (
            'f-98-36',
            {
                'manuscript_title': 'Псалтырь с восследованием',
                'manuscript_code_title': 'Ф.98 №36',
                'year_in': None,
                'fund_title': enums.FundTitle.f_98
            }
    ),
    (
            'f-98-80',
            {
                'manuscript_title': 'Евангелие учительное («Патриарший гомилиарий»), лицевое',
                'manuscript_code_title': 'Ф.98 №80',
                'year_in': None,
                'fund_title': enums.FundTitle.f_98
            }
    )
])
def test_collect_manuscript_data_from_rsl(
        requests_mock,
        session: requests.Session,
        manuscript_code: str,
        manuscript_data_any: dict[str, str | schemas.YearCreate | None]
) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/rsl/{manuscript_code}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(
        f'{const.RslUrl.GET_MANUSCRIPT}/{utils.combine_fund_with_manuscript_code(manuscript_code)}',
        text=requests_mock_text
    )
    collect_manuscript_data = CollectManuscriptDataFromRsl(session, manuscript_code=manuscript_code)
    assert manuscript_data_any['manuscript_code_title'] == collect_manuscript_data.manuscript_code_title
    assert manuscript_data_any['manuscript_title'] == collect_manuscript_data.manuscript_title
    assert manuscript_data_any['fund_title'] == collect_manuscript_data.fund_title


@pytest.mark.parametrize('manuscript_code_title, fund_title', [
    ('Ф.173/I №2', enums.FundTitle.f_173i),
    ('Ф.304/III №3', enums.FundTitle.f_304iii),
    ('Ф.98 №80', enums.FundTitle.f_98),
])
def test_prepare_fund_title_from_rsl(manuscript_code_title: str, fund_title: enums.FundTitle):
    assert CollectManuscriptDataFromRsl.prepare_fund_title(manuscript_code_title) == fund_title
