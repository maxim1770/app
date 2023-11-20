from pathlib import Path

import requests
from bs4 import Tag, BeautifulSoup

from app import const
from app.api import deps
from app.core.config import settings
from app.create.prepare.base_collect import collect_saint_data
from app.create.prepare.manuscript.collect_manuscript_data import CollectManuscriptDataFromRsl, \
    CollectManuscriptDataFromNeb
from app.create.prepare.manuscript.search_manuscript import SearchManuscriptInNeb


def create_dirs_for_test_data():
    path = Path(settings.TEST_DATA_DIR)
    path.mkdir(exist_ok=True)
    for dir, sub_dirs in {
        'manuscript': ['get', 'search'],
        'saint': []
    }.items():
        dir_path = path / dir
        dir_path.mkdir(exist_ok=True)
        for sub_dir in sub_dirs:
            sub_dir_path = dir_path / sub_dir
            sub_dir_path.mkdir(exist_ok=True)


def create_get_saints_data(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'saint/some_saint_slug.html'
    for saint_slug in [
        'ioann-zlatoust',
        'marija-egipetskaja',
        'igor-v-kreshchenii-georgij-chernigovskij-i-kievskij',
        'luka-evangelist',
        'kliment-rimskij',
        'andrej-konstantinopolskij',
        'avraam',
        'ioann-bogoslov',
        'anna-novgorodskaja'
    ]:
        current_path = path.with_stem(saint_slug)
        if not current_path.exists():
            saint_data: Tag = collect_saint_data(session, saint_slug=saint_slug)
            current_path.write_text(str(saint_data), encoding="utf-8")


def create_get_manuscripts_data_rsl(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'manuscript/get/rsl/some_manuscript_code.html'
    for manuscript_code in [
        'f-304iii-15',
        'f-173i-2',
        'f-98-36',
        'f-98-80',
        'f-7-16',
        'f-37-15'
    ]:
        current_path = path.with_stem(manuscript_code)
        if not current_path.exists():
            collect_manuscript_data = CollectManuscriptDataFromRsl(session, manuscript_code=manuscript_code)
            manuscript_data: Tag = collect_manuscript_data._soup
            current_path.write_text(str(manuscript_data), encoding="utf-8")


def create_get_manuscripts_data_neb(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'manuscript/get/neb/some_manuscript_neb_slug.html'
    for manuscript_neb_slug in [
        'apostol-aprakos-licevaya-rukopis',
        'prolog-mart-avgust-4',
        'evangelie-uchitelnoe-licevoe',
        'psaltyr-s-vossledovaniem-1',
        'sbornik-slov-kanonov-i-zhitiy',
        'zhitie-nikolaya-chudotvorca-licevoe-otryvok-iz-letopisnogo-svoda-licevoy'
    ]:
        current_path = path.with_stem(manuscript_neb_slug)
        if not current_path.exists():
            collect_manuscript_data = CollectManuscriptDataFromNeb(session, manuscript_code=manuscript_neb_slug)
            manuscript_data: Tag = collect_manuscript_data._soup
            current_path.write_text(str(manuscript_data), encoding="utf-8")


def create_get_manuscripts_data_nlr(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'manuscript/get/nlr/some_manuscript_code.json'
    for manuscript_code in [
        '14CB689B-8344-49F0-9DD6-0AAE09460BE0',
        '59014138-46CC-4335-9E3C-9F903FD854A3',
        '919048C3-8920-40C1-A94D-AA216B5E2FD6',
        'D157FA07-FF83-4AF2-851A-09DC187B4F9F',
        '2EADD685-EB71-40C5-BDEC-7E9DC9B7EFCE',
        '466FB16F-C1B8-443E-BD95-C02D272D0251'
    ]:
        current_path = path.with_stem(manuscript_code)
        if not current_path.exists():
            r = session.post(const.NlrUrl.GET_MANUSCRIPT_DATA_API, data={'ab': manuscript_code})
            manuscript_data_json: str = r.text
            current_path.write_text(manuscript_data_json, encoding="utf-8")


def create_search_manuscripts_nlr(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'manuscript/search/nlr/some_manuscript_code.json'
    for manuscript_code_title, manuscript_code in [
        ('Сол. 24/24', '14CB689B-8344-49F0-9DD6-0AAE09460BE0'),
        ('Кир.-Бел. 1/1240', '59014138-46CC-4335-9E3C-9F903FD854A3'),
        ('F.IV.225', '919048C3-8920-40C1-A94D-AA216B5E2FD6')
    ]:
        current_path = path.with_stem(manuscript_code)
        if not current_path.exists():
            search_data: dict[str, str] = {
                'doc_Shifr': manuscript_code_title,
                'doc_IsYesDigital': 'on'
            }
            r = session.post(const.NlrUrl.SEARCH_MANUSCRIPT_API, data=search_data)
            search_manuscript_json: str = r.text
            current_path.write_text(search_manuscript_json, encoding="utf-8")


def create_search_manuscripts_neb(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'manuscript/search/neb/some_manuscript_neb_slug.json'
    for manuscript_code_title, manuscript_neb_slug in [
        ('F.I.60', 'apostol-aprakos-licevaya-rukopis'),
        ('Соф. 1345', 'prolog-mart-avgust-4'),
        ('Ф.98 №80', 'evangelie-uchitelnoe-licevoe'),
        ('Сол. 754/864', 'psaltyr-s-vossledovaniem-1'),
        ('Кир.-Бел. 19/1096', 'sbornik-slov-kanonov-i-zhitiy'),
        ('Ф.37 №15', 'zhitie-nikolaya-chudotvorca-licevoe-otryvok-iz-letopisnogo-svoda-licevoy'),
        ('NOT_FOUND_IN_NEB', 'NOT_FOUND_IN_NEB')
    ]:
        current_path = path.with_stem(manuscript_neb_slug)
        if not current_path.exists():
            url: str = SearchManuscriptInNeb.prepare_neb_search_manuscript_api_url(manuscript_code_title)
            r = session.get(url)
            search_manuscript_json: str = r.text
            current_path.write_text(search_manuscript_json, encoding="utf-8")


def _prepare_zachalo_abbr_to_path(zachalo_abbr):
    zachalo_abbr: str = zachalo_abbr.replace('.', '_').replace(':', '_')
    return zachalo_abbr


def create_get_zachalos_data(session: requests.Session):
    path = Path(settings.TEST_DATA_DIR) / 'zachalo/some_zachalo_abbr.html'
    for zachalo_abbr in [
        'Jn.4:46-54',
        'Jn.7:1-13',
        'Act.9:20-31',
        'Jn.5:30-6:2',
        'Act.27:1-44',
        'Act.23:1-11',
        'Rom.1:7-12',
    ]:
        current_path = path.with_stem(_prepare_zachalo_abbr_to_path(zachalo_abbr))
        if not current_path.exists():
            r = session.get(url=const.AzbykaUrl.GET_ZACHALO + zachalo_abbr)
            soup = BeautifulSoup(r.text, 'lxml')
            current_path.write_text(str(soup), encoding="utf-8")


def create_all_test_data(session: requests.Session):
    # create_dirs_for_test_data()
    create_get_saints_data(session)
    create_get_manuscripts_data_rsl(session)
    create_get_manuscripts_data_neb(session)
    create_get_manuscripts_data_nlr(session)
    create_search_manuscripts_nlr(session)
    create_search_manuscripts_neb(session)
    create_get_zachalos_data(session)


if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    create_all_test_data(session)
