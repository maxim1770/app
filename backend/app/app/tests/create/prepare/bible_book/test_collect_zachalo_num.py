import pytest
import requests

from app.create.prepare import PrepareError
from app.create.prepare.bible_book.zachalo import _collect_zachalo_num
from app.tests import test_utils


@pytest.mark.parametrize(
    'zachalo_abbr, zachalo_num',
    [
        ('Jn.4:46-54', 13),  # INFO Когда zachalo первый выделенный div
        ('Jn.7:1-13', 25),  # INFO Когда zachalo первый выделенный div
        ('Act.9:20-31', 22),  # WARNING Когда zachalo выше на один первого выделенного div
        ('Jn.5:30-6:2', 17),  # WARNING Когда zachalo ниже (на 1 или больше)
        ('Rom.1:7-12', 79),  # ERROR Когда zachalo выше (на 2 или больше) первого выделенного div
        ('Act.27:1-44', 50),  # ERROR Когда zachalo первое найденное на странице, стр. без выделения
    ])
def test_collect_zachalo_num(
        requests_mock,
        session: requests.Session,
        zachalo_abbr: str,
        zachalo_num: int
) -> None:
    test_utils.requests_mock_get_zachalo_data(
        requests_mock,
        zachalo_abbr=zachalo_abbr,
    )
    assert _collect_zachalo_num(zachalo_abbr) == zachalo_num


@pytest.mark.parametrize(
    'zachalo_abbr',
    [
        'Act.23:1-11',  # Когда zachalo нет на странице и его стоит ввести вручную в api
    ])
def test_collect_zachalo_num_not_found(
        requests_mock,
        session: requests.Session,
        zachalo_abbr: str
) -> None:
    test_utils.requests_mock_get_zachalo_data(
        requests_mock,
        zachalo_abbr=zachalo_abbr,
    )
    with pytest.raises(PrepareError) as e:
        _collect_zachalo_num(zachalo_abbr)
    assert e.type is PrepareError
    assert e.value.args[0] == 'Когда zachalo нет на странице и его стоит ввести вручную в api'
