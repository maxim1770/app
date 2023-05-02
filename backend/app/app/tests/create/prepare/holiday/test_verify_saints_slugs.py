import pytest
import requests

from app.create.prepare.holiday.holiday_create import SaintsHolidayNewCreateFactory


@pytest.mark.parametrize('saints_slugs, verified_saints_slugs', [
    ('prov-anazarvskij-tarah-anazarvskij-andronik-anazarvskij',
     ['prov-anazarvskij', 'tarah-anazarvskij', 'andronik-anazarvskij']
     ),
    ('iustinian-i-upravda-feodora-grecheskaja-carica',
     ['iustinian-i-upravda', 'feodora-grecheskaja-carica']
     ),
    ('varvara-iliopolskaja-iulianija-iliopolskaja',
     ['varvara-iliopolskaja', 'iulianija-iliopolskaja']
     ),
    ('simeon-palestinskij-ioann-palestinskij-spostnik',
     ['simeon-palestinskij', 'ioann-palestinskij-spostnik']
     ),
])
def test_verify_saints_slugs(
        session: requests.Session,
        saints_slugs: str,
        verified_saints_slugs: list[str]
) -> None:
    assert SaintsHolidayNewCreateFactory._verify_saints_slugs(
        session,
        saints_slugs=saints_slugs
    ) == verified_saints_slugs


@pytest.mark.parametrize('saints_slugs, verified_saints_slugs', [
    ('konstantin-aetij-feofil-feodor-ammorejskie-frigijskie',
     ['konstantin-ammorejskij-frigijskij', 'aetij-ammorejskij-frigijskij', 'feofil-ammorejskij-frigijskij',
      'feodor-ammorejskij-frigijskij']
     ),
])
def test_verify_saints_slugs_method_2(
        session: requests.Session,
        saints_slugs: str,
        verified_saints_slugs: list[str]
) -> None:
    assert SaintsHolidayNewCreateFactory._verify_saints_slugs_method_2(
        session,
        saints_slugs=saints_slugs
    ) == verified_saints_slugs


@pytest.mark.parametrize('saints_slugs, verified_saints_slugs', [
    ('avgusta-vasilissa-rimskaja-porfirij-stratilat',
     ['avgusta-vasilissa-rimskaja', 'porfirij-stratilat']
     ),
])
def test_verify_saints_slugs_bad(
        session: requests.Session,
        saints_slugs: str,
        verified_saints_slugs: list[str]
) -> None:
    assert SaintsHolidayNewCreateFactory._verify_saints_slugs(
        session,
        saints_slugs=saints_slugs
    ) != verified_saints_slugs
