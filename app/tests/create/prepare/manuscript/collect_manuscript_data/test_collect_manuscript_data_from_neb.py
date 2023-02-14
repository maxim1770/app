from pathlib import Path

import pytest
import requests

from app import schemas, const, enums
from app.core.config import settings
from app.create.prepare.manuscript.collect_manuscript_data import CollectManuscriptDataFromNeb


@pytest.mark.parametrize('manuscript_neb_slug, manuscript_data_any', [
    (
            'apostol-aprakos-licevaya-rukopis',
            {
                'manuscript_title': 'Апостол апракос: Лицевая рукопись',
                'manuscript_code_title': 'F.I.60',
                'year_in': None,
                'fund_title': enums.FundTitle.f_i
            }
    ),
    (
            'prolog-mart-avgust-4',
            {
                'manuscript_title': 'Пролог. Март-август',
                'manuscript_code_title': 'Соф. 1345',
                'year_in': schemas.YearCreate(title='1501'),
                'fund_title': enums.FundTitle.sof
            }
    ),
    (
            'evangelie-uchitelnoe-licevoe',
            {
                'manuscript_title': 'Евангелие учительное',
                'manuscript_code_title': 'Ф.98 №80',
                'year_in': None,
                'fund_title': enums.FundTitle.f_98
            }
    ),

])
def test_collect_manuscript_data_from_neb(
        requests_mock,
        session: requests.Session,
        manuscript_neb_slug: str,
        manuscript_data_any: dict[str, str | schemas.YearCreate | enums.FundTitle | None]
) -> None:
    path = Path(settings.TEST_DATA_DIR) / f'manuscript/get/neb/{manuscript_neb_slug}.html'
    requests_mock_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(
        f'{const.NebUrl.GET_MANUSCRIPT_DATA}/{manuscript_neb_slug}',
        text=requests_mock_text
    )
    collect_manuscript_data = CollectManuscriptDataFromNeb(session, manuscript_code=manuscript_neb_slug)
    assert manuscript_data_any['manuscript_code_title'] == collect_manuscript_data.manuscript_code_title
    assert manuscript_data_any['manuscript_title'] == collect_manuscript_data.manuscript_title
    assert manuscript_data_any['fund_title'] == collect_manuscript_data.fund_title


@pytest.mark.parametrize('manuscript_code_title_from_neb, manuscript_code_title', [
    ('Ф.178.1 №9500', 'Ф.178/I №9500'),
    ('Ф.304.3 №15', 'Ф.304/III №15'),
    ('Ф.304.3 №3', 'Ф.304/III №3'),
    ('Ф.98 №80', 'Ф.98 №80'),
    ('Ф.7 №27', 'Ф.7 №27'),
])
def test_prepare_rsl_manuscript_code_title_from_neb(manuscript_code_title_from_neb: str, manuscript_code_title: str):
    assert CollectManuscriptDataFromNeb._prepare_rsl_manuscript_code_title_from_neb(
        manuscript_code_title_from_neb
    ) == manuscript_code_title
