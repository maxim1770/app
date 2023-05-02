import logging
import re
from difflib import SequenceMatcher

import requests
from bs4 import BeautifulSoup, Tag
from sqlalchemy.orm import Session

from app import crud, models, enums, utils
from app.api import deps
from app.create import const

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def _collect_icons_saints(session: requests.Session) -> list[Tag]:
    r = session.get(const.PraviconUrl.GET_SAINTS)
    table: Tag = BeautifulSoup(r.text, 'lxml').find('table', {'border': '0'})
    icons_saints: list[Tag] = table.find_all('a')
    return icons_saints


def _prepare_saint_name(
        saint_name: str,
        *,
        saint_face_sanctity_title: enums.FaceSanctityTitle | None,
        saint_dignity_title: enums.DignityTitle | None
):
    if saint_face_sanctity_title:
        saint_name = saint_name.replace(saint_face_sanctity_title, '')
    if saint_dignity_title:
        saint_name = saint_name.replace(saint_dignity_title, '')
    saint_name = saint_name.replace('́', '')
    return saint_name


def __prepare_collected_saint_name(collected_saint_name: str) -> str:
    collected_saint_name = collected_saint_name.strip()
    if collected_saint_name[-1] == '.':
        if collected_saint_name.rfind(',') != -1:
            collected_saint_name = collected_saint_name[:collected_saint_name.rfind(',')]  # name, прп.
        else:
            collected_saint_name = collected_saint_name[:collected_saint_name.rfind(' ')]  # name прп.
    return collected_saint_name


def _common_prepare_saint_name(some_saint_name: str) -> str:
    some_saint_name = some_saint_name.strip()
    some_saint_name = some_saint_name.lower()
    some_saint_name = some_saint_name.replace(' ,  ', ' ')
    for deleted_word in [' князь ', ' дева ', ' авва ', 'i']:
        some_saint_name = some_saint_name.replace(deleted_word, '')
    some_saint_name = re.sub(r'\([^()]*\)', '', some_saint_name)  # 683 (когда разкоментированно)
    some_saint_name = some_saint_name.replace('(', '').replace(')', '')  # 621 (когда разкоментированно)
    some_saint_name = some_saint_name.replace(',', ' ').replace('  ', ' ').replace('  ', ' ')
    some_saint_name: str = utils.clean_extra_spaces(some_saint_name)
    return some_saint_name


def _final_prepare_collected_saint_name(collected_saint_name: str) -> str:
    collected_saint_name: str = _common_prepare_saint_name(collected_saint_name)
    collected_saint_name: str = __prepare_collected_saint_name(collected_saint_name)
    collected_saint_name: str = __prepare_collected_saint_name(collected_saint_name)
    collected_saint_name: str = _common_prepare_saint_name(collected_saint_name)
    return collected_saint_name


def __collect_pravicon_saint_id(icon_saint: Tag) -> int:
    pravicon_saint_id = int(icon_saint['href'].replace('/icon-', ''))
    return pravicon_saint_id


def _find_pravicon_saint_id(saint_name: str, *, icons_saints: list[Tag]) -> int | None:
    for icon_saint in icons_saints:
        collected_saint_name: str = _final_prepare_collected_saint_name(icon_saint.text)
        if saint_name == collected_saint_name:
            return __collect_pravicon_saint_id(icon_saint)
    for icon_saint in icons_saints:
        collected_saint_name: str = _final_prepare_collected_saint_name(icon_saint.text)
        saint_name, collected_saint_name = _final_common_prepare_saint_name(saint_name, collected_saint_name)
        if collected_saint_name == saint_name:
            return __collect_pravicon_saint_id(icon_saint)
        # __sequence_matcher(saint_name, collected_saint_name=collected_saint_name)  # delete me
    return None


def get_pravicon_saints_ids(db: Session, *, session: requests.Session) -> list[tuple[str, int]]:
    pravicon_saints_ids: list[tuple[str, int]] = []
    icons_saints: list[Tag] = _collect_icons_saints(session)
    saints: list[models.Saint] = crud.saint.get_multi(db, limit=3000)
    for saint in saints:
        if saint.name is None:
            continue
        saint_face_sanctity_title: enums.FaceSanctityTitle | None = saint.face_sanctity.title if saint.face_sanctity else None
        saint_dignity_title: enums.DignityTitle | None = saint.dignity.title if saint.dignity else None
        saint_name: str = _prepare_saint_name(
            saint.name,
            saint_face_sanctity_title=saint_face_sanctity_title,
            saint_dignity_title=saint_dignity_title
        )
        saint_name: str = _common_prepare_saint_name(saint_name)
        pravicon_saint_id: int | None = _find_pravicon_saint_id(saint_name, icons_saints=icons_saints)
        if pravicon_saint_id:
            pravicon_saints_ids.append((saint.slug, pravicon_saint_id))
    return pravicon_saints_ids


def _final_common_prepare_saint_name(some_saint_name_1: str, some_saint_name_2) -> tuple[str, str]:
    words: list[tuple[str, str | list[str]]] = [
        ('', 'дева'),
        ('', 'отрок'),
        ('', 'воин'),
        ('', 'князь'),
        ('', 'царевич'),
        ('', 'пресвитер'),
        ('', 'чтец'),
        ('', ' авва'),
        ('', 'исповедник'),
        ('', 'new'),
        ('', 'g_y_1'),
        ('', 'прп.'),
        ('', 'исп.'),
        ('', 'ап. еп.'),
        ('ученик ап.', 'еп. ученик'),
        ('пророчица', 'прор.'),
        ('анна пророчица мать', 'анна мать'),
        ('персиянин', 'персянин'),
        ('севастиан', 'севастьян'),
        ('ахила', 'ахилла'),
        ('пелусиот', 'пилусиот'),
        ('переяславский', 'переславский'),
        ('азийский', 'асийский'),
        ('аврамий', 'авраамий'),
        ('херсонесский', ['херсонский', 'херсонессий']),
        ('синопский', 'синопийский'),
        ('капитолийский', 'капетолийский'),
        ('препростый', 'препростой'),
        ('аназаровская', 'аназарвская'),
        ('аназаровский', 'аназарвский'),
        ('медикийский', 'мидикийский'),
        ('ларисийский', 'ларисский'),
        ('бастийский', 'бастрийский'),
        ('городноезерский', 'гродноезерский'),
        ('сингелл', 'синкелл'),
        ('ливийский', 'ликийский'),
        ('бастийский', 'бастрийский'),
        ('илия', 'илья'),
        ('фесвитянин', 'фесфитянин'),
        ('елисавета', 'елизавета'),
    ]
    saints_names: list[str, str] = []
    for some_saint_name in [some_saint_name_1, some_saint_name_2]:
        for final_word, words_to_replace in words:
            if isinstance(words_to_replace, list):
                for word_to_replace in words_to_replace:
                    some_saint_name = some_saint_name.replace(word_to_replace, final_word)
            else:
                some_saint_name = some_saint_name.replace(words_to_replace, final_word)
        some_saint_name: str = utils.clean_extra_spaces(some_saint_name)
        saints_names.append(some_saint_name)
    return tuple(saints_names)


def __sequence_matcher(saint_name: str, *, collected_saint_name: str) -> None:
    if SequenceMatcher(None, saint_name, collected_saint_name).ratio() > 0.80:
        logging.error(f'{saint_name}')
        logging.error(collected_saint_name)
        logging.warning('- - -')


def __test_():
    collected_saint_name = __prepare_collected_saint_name('Макарий Великий, Египетский, прп.')
    saint_name = _prepare_saint_name(
        'Преподобный Макарий Великий, Египетский',
        saint_face_sanctity_title=enums.FaceSanctityTitle.prepodobnyj,
        saint_dignity_title=None
    )
    collected_saint_name = _common_prepare_saint_name(collected_saint_name)
    saint_name = _common_prepare_saint_name(saint_name)
    logging.info(saint_name)
    logging.info(collected_saint_name)
    if saint_name == collected_saint_name:
        logging.warning('==')
    else:
        logging.warning('!=')


if __name__ == '__main__':
    db: Session = next(deps.get_db())
    session: requests.Session = next(deps.get_session())
    pravicon_saints_ids: list[tuple[str, int]] = get_pravicon_saints_ids(db, session=session)
    print(len(pravicon_saints_ids))
