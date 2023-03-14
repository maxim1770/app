from uuid import UUID

import pytest
import requests

from app import schemas, enums
from app.create.prepare.manuscript.collect_manuscript_data import CollectManuscriptDataFromNlr
from app.tests import test_utils


@pytest.mark.parametrize('manuscript_code, manuscript_data_any', [
    (
            UUID('14CB689B-8344-49F0-9DD6-0AAE09460BE0'),
            {
                'manuscript_title': 'Апостол толковый',
                'manuscript_code_title': 'Сол. 24/24',
                'year_in': schemas.YearCreate(title='1458'),
                'fund_title': enums.FundTitle.sol
            }
    ),
    (
            UUID('59014138-46CC-4335-9E3C-9F903FD854A3'),
            {
                'manuscript_title': 'Пролог. Декабрь-февраль',
                'manuscript_code_title': 'Кир.-Бел. 1/1240',
                'year_in': schemas.YearCreate(title='1452'),
                'fund_title': enums.FundTitle.kir_bel
            }
    ),
    (
            UUID('919048C3-8920-40C1-A94D-AA216B5E2FD6'),
            {
                'manuscript_title': 'Лицевой летописный свод',
                'manuscript_code_title': 'F.IV.225',
                'year_in': None,
                'fund_title': enums.FundTitle.f_i
            }
    ),

])
def test_collect_manuscript_data_from_nlr(
        requests_mock,
        session: requests.Session,
        manuscript_code: UUID,
        manuscript_data_any: dict[str, str | schemas.YearCreate | enums.FundTitle | None]
) -> None:
    test_utils.requests_mock_get_manuscript_data_nlr(requests_mock, manuscript_code=manuscript_code)
    collect_manuscript_data = CollectManuscriptDataFromNlr(session, manuscript_code=manuscript_code)
    assert manuscript_data_any['manuscript_code_title'] == collect_manuscript_data.manuscript_code_title
    assert manuscript_data_any['manuscript_title'] == collect_manuscript_data.manuscript_title
    assert manuscript_data_any['fund_title'] == collect_manuscript_data.fund_title


@pytest.mark.parametrize('manuscript_code_title, fund_title', [
    ('F.I.60', enums.FundTitle.f_i),
    ('F.IV.225', enums.FundTitle.f_i),
    ('O.I.279', enums.FundTitle.f_i),
    ('Q.I.1138', enums.FundTitle.f_i),
    ('Q.п.I.54', enums.FundTitle.f_i),
    ('Кир.-Бел. 2/1079', enums.FundTitle.kir_bel),
    ('Сол. 1128/1237', enums.FundTitle.sol),
    ('Сол. 24/24', enums.FundTitle.sol),
    ('Гильф. 64', enums.FundTitle.gilf),
    ('Погод. 59', enums.FundTitle.pogod)
])
def test_prepare_fund_title_from_nlr(manuscript_code_title: str, fund_title: enums.FundTitle):
    assert CollectManuscriptDataFromNlr.prepare_fund_title(manuscript_code_title) == fund_title
