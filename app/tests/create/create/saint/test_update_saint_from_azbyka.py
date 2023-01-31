from pathlib import Path

import pytest
import requests
from sqlalchemy.orm import Session

from app import crud, schemas, enums, create
from app.core.config import settings


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
def test_update_saint_from_azbyka(
        db: Session,
        requests_mock,
        session: requests.Session,
        saint_slug: str,
        saint_data_in: schemas.SaintDataUpdate
) -> None:
    saint = crud.saint.create(db, obj_in=schemas.SaintCreate(slug=saint_slug))
    dignity = crud.create_dignity(
        db,
        dignity_in=schemas.DignityCreate(title=saint_data_in.dignity_title)
    ) if saint_data_in.dignity_title else None
    face_sanctity = crud.create_face_sanctity(
        db,
        face_sanctity_in=schemas.FaceSanctityCreate(title=saint_data_in.face_sanctity_title)
    ) if saint_data_in.face_sanctity_title else None
    path = Path(settings.TEST_DATA_DIR) / f'saint/{saint_slug}.html'
    requests_text: str = path.read_text(encoding="utf-8")
    requests_mock.get(f'https://azbyka.ru/days/sv-{saint_slug}', text=requests_text)
    saint_2 = create.update_saint_from_azbyka(db, session=session, saint=saint)
    assert saint_2.id == saint.id
    assert saint_2.slug == saint_slug
    assert saint_2.dignity == dignity
    assert saint_2.face_sanctity == face_sanctity
    assert saint_2.face_sanctity.title == saint_data_in.face_sanctity_title
    assert saint_2.name == saint_data_in.saint_in.name


def test_update_saint_from_azbyka_name_already_exists_bad(
        db: Session,
        session: requests.Session,
) -> None:
    saint_in = schemas.SaintCreate(slug='some-slug', name='some name')
    saint = crud.saint.create(db, obj_in=saint_in)
    with pytest.raises(create.FatalCreateError) as e:
        saint_2 = create.update_saint_from_azbyka(db, session=session, saint=saint)
    assert e.type is create.FatalCreateError
    assert e.value.args[0] == f'Saint name already exists, saint.slug = {saint.slug}'
