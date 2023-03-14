from uuid import UUID

import pytest
import requests

from app.create.prepare.manuscript.collect_manuscript_data import CollectManuscriptDataFromNlr, \
    CollectManuscriptDataFromRsl, CollectManuscriptDataFromNeb
from app.create.prepare.manuscript.manuscript import CollectManuscriptDataFactory
from app.tests import test_utils


@pytest.mark.parametrize('manuscript_code, manuscript_code_title, manuscript_neb_slug, collect_manuscript_data_class', [
    (
            UUID('D157FA07-FF83-4AF2-851A-09DC187B4F9F'),
            'Гильф. 2',
            None,
            CollectManuscriptDataFromNlr
    ),
    (
            UUID('2EADD685-EB71-40C5-BDEC-7E9DC9B7EFCE'),
            'Сол. 754/864',
            'psaltyr-s-vossledovaniem-1',
            CollectManuscriptDataFromNeb
    ),
    (
            UUID('466FB16F-C1B8-443E-BD95-C02D272D0251'),
            'Кир.-Бел. 19/1096',
            'sbornik-slov-kanonov-i-zhitiy',
            CollectManuscriptDataFromNeb
    ),
    (
            'f-7-16',
            'Ф.7 №16',
            None,
            CollectManuscriptDataFromRsl
    ),
    (
            'f-98-80',
            'Ф.98 №80',
            'evangelie-uchitelnoe-licevoe',
            CollectManuscriptDataFromNeb
    ),
    (
            'f-37-15',
            'Ф.37 №15',
            'zhitie-nikolaya-chudotvorca-licevoe-otryvok-iz-letopisnogo-svoda-licevoy',
            CollectManuscriptDataFromNeb
    )
])
def test_сollect_manuscript_data_factory_get_by_manuscript_code(
        requests_mock,
        session: requests.Session,
        manuscript_code: UUID | str,
        manuscript_code_title: str,
        manuscript_neb_slug: str | None,
        collect_manuscript_data_class: [
            CollectManuscriptDataFromNlr | CollectManuscriptDataFromRsl | CollectManuscriptDataFromNeb
        ]
) -> None:
    if isinstance(manuscript_code, UUID):
        test_utils.requests_mock_get_manuscript_data_nlr(requests_mock, manuscript_code=manuscript_code)
    else:
        test_utils.requests_mock_get_manuscript_data_rsl(requests_mock, manuscript_code=manuscript_code)
    test_utils.requests_mock_search_manuscript_in_neb(
        requests_mock,
        manuscript_code_title=manuscript_code_title,
        manuscript_neb_slug=manuscript_neb_slug,
    )
    if manuscript_neb_slug:
        test_utils.requests_mock_get_manuscript_data_neb(
            requests_mock,
            manuscript_neb_slug=manuscript_neb_slug,
        )
    collect_manuscript_data = CollectManuscriptDataFactory.get_by_manuscript_code(
        session,
        manuscript_code=manuscript_code
    )
    assert isinstance(collect_manuscript_data, collect_manuscript_data_class)
    assert collect_manuscript_data.manuscript_code_title == manuscript_code_title
    if isinstance(collect_manuscript_data, CollectManuscriptDataFromNeb):
        assert collect_manuscript_data._manuscript_code == manuscript_neb_slug
    else:
        assert collect_manuscript_data._manuscript_code == manuscript_code
