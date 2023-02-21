import pytest
import requests

from app import schemas, enums
from app.create import prepare
from app.tests import test_utils


@pytest.mark.parametrize('saint_slug, saint_data_in', [
    (
            'ioann-zlatoust',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Святитель Иоа́нн Златоуст, архиепископ Константинопольский'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.svjatitel,
                dignity_title=enums.DignityTitle.arhiepiskop,
            )
    ),
    (
            'marija-egipetskaja',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Преподобная Мари́я Египетская'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.prepodobnaja
            )
    ),
    (
            'igor-v-kreshchenii-georgij-chernigovskij-i-kievskij',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Благоверный князь И́горь (в Крещении Гео́ргий, в иночестве Гаврии́л) Ольгович, Черниговский и Киевский'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.blagovernyj_knjaz
            )
    )

])
def test_saint_data_update_factory(
        requests_mock,
        session: requests.Session,
        saint_slug: str,
        saint_data_in: schemas.SaintDataUpdate
) -> None:
    test_utils.requests_mock_get_saint_data(requests_mock, saint_slug=saint_slug)
    saint_data_in_2 = prepare.SaintDataUpdateFactory(session, saint_slug=saint_slug).get()
    assert saint_data_in_2 == saint_data_in
