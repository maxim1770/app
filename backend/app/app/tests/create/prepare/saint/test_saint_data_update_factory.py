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
                    name='Святитель Иоа́нн Златоуст, Архиепископ Константинопольский',
                    name_in_dative='святителю Иоанну Златоусту'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.svjatitel,
                dignity_title=enums.DignityTitle.arhiepiskop,
            )
    ),
    (
            'marija-egipetskaja',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Преподобная Мари́я Египетская',
                    name_in_dative='преподобной Марии Египетской'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.prepodobnaja
            )
    ),
    # (
    #         'igor-v-kreshchenii-georgij-chernigovskij-i-kievskij',
    #         schemas.SaintDataUpdate(
    #             saint_in=schemas.SaintUpdate(
    #                 name='Благоверный Князь И́горь (в Крещении Гео́ргий, в иночестве Гаврии́л) Ольгович, Черниговский и Киевский',
    #                 name_in_dative='благоверному князю Игорю (в Крещении Георгию, в иночестве Гавриилу) Черниговскому и Киевскому'
    #             ),
    #             face_sanctity_title=enums.FaceSanctityTitle.blagovernyj_knjaz
    #         )
    # ),
    (
            'luka-evangelist',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Апостол от 70-ти Лука́ Евангелист, иконописец',
                    name_in_dative='апостолу и евангелисту Луке'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.apostol_ot_70_ti
            )
    ),
    (
            'kliment-rimskij',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Священномученик Кли́мент Римский, Папа Римский',
                    name_in_dative='священномученику Клименту, папе Римскому'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.svjaschennomuchenik,
                dignity_title=enums.DignityTitle.papa_rimskij
            )
    ),
    (
            'andrej-konstantinopolskij',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Блаженный Андре́й Константинопольский, Христа ради Юродивый',
                    name_in_dative='блаженному Андрею Константинопольскому, Христа ради юродивому'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.blazhennyj,
            )
    ),
    (
            'avraam',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Ветхозаветный Патриарх Авраа́м'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.vethozavetnyj_patriarh,
            )
    ),
    (
            'ioann-bogoslov',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Апостол Иоа́нн Богослов, евангелист',
                    name_in_dative='апостолу и евангелисту Иоанну Богослову'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.apostol,
            )
    ),
    (
            'anna-novgorodskaja',
            schemas.SaintDataUpdate(
                saint_in=schemas.SaintUpdate(
                    name='Благоверная Княгиня А́нна Новгородская',
                    name_in_dative='благоверной княгине Анне Новгородской'
                ),
                face_sanctity_title=enums.FaceSanctityTitle.blagovernaja_knjaginja,
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
