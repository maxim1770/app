import pytest
import requests

from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNeb
from app.tests import test_utils


@pytest.mark.parametrize('manuscript_code_title, manuscript_neb_slug', [
    ('F.I.60', 'apostol-aprakos-licevaya-rukopis'),
    ('Соф. 1345', 'prolog-mart-avgust-4'),
    ('Ф.98 №80', 'evangelie-uchitelnoe-licevoe')
])
def test_search_manuscript_in_neb(
        requests_mock,
        session: requests.Session,
        manuscript_code_title: str,
        manuscript_neb_slug: str
) -> None:
    test_utils.requests_mock_search_manuscript_in_neb(
        requests_mock,
        manuscript_code_title=manuscript_code_title,
        manuscript_neb_slug=manuscript_neb_slug
    )
    search_manuscript = SearchManuscriptInNeb(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_neb_slug == manuscript_neb_slug


def test_search_manuscript_in_neb_not_found(
        requests_mock,
        session: requests.Session,
) -> None:
    manuscript_code_title: str = 'some manuscript not found in neb'
    test_utils.requests_mock_search_manuscript_in_neb(
        requests_mock,
        manuscript_code_title=manuscript_code_title,
        manuscript_neb_slug=None
    )
    search_manuscript = SearchManuscriptInNeb(session, manuscript_code_title=manuscript_code_title)
    assert search_manuscript.manuscript_neb_slug is None


@pytest.mark.parametrize('manuscript_code_title, manuscript_code_title_from_neb', [
    ('Ф.178/I №9500', 'Ф.178.1 №9500'),
    ('Ф.304/III №15', 'Ф.304.3 №15'),
    ('Ф.304/III №3', 'Ф.304.3 №3'),
    ('Ф.98 №80', 'Ф.98 №80')
])
def test_prepare_rsl_manuscript_code_title(manuscript_code_title: str, manuscript_code_title_from_neb: str):
    assert SearchManuscriptInNeb.prepare_rsl_manuscript_code_title(
        manuscript_code_title
    ) == manuscript_code_title_from_neb
