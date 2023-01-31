from pathlib import Path

import pytest
import requests

from app import schemas, enums
from app.core.config import settings
from app.create import prepare


@pytest.mark.parametrize("saint_slug, saint_data_in", [
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
    path = Path(settings.TEST_DATA_DIR) / f'saint/{saint_slug}.html'
    requests_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(f'https://azbyka.ru/days/sv-{saint_slug}', text=requests_text)
    saint_data_in_2 = prepare.SaintDataUpdateFactory(session=session, saint_slug=saint_slug).get()
    assert saint_data_in_2 == saint_data_in
