import logging
import re
from difflib import SequenceMatcher

import requests
from bs4 import Tag

from app import models, enums, utils
from ..icon import __collect


def get_pravicon_saints_ids(session: requests.Session, *, saints: list[models.Saint]) -> list[tuple[models.Saint, int]]:
    pravicon_saints_ids: list[tuple[models.Saint, int]] = []  # название возможно стоит поменять
    icons_saints: list[Tag] = __collect.collect_icons_saints(session)
    for saint in saints:
        if saint.name is None:
            continue
        saint_face_sanctity_title: enums.FaceSanctityTitle | None = saint.face_sanctity.title if saint.face_sanctity else None
        saint_dignity_title: enums.DignityTitle | None = saint.dignity.title if saint.dignity else None
        saint_name: str = __prepare_saint_name(
            saint.name,
            saint_face_sanctity_title=saint_face_sanctity_title,
            saint_dignity_title=saint_dignity_title
        )
        saint_name: str = ___common_prepare_saint_name(saint_name)
        pravicon_saint_id: int | None = _find_pravicon_saint_id(saint_name, icons_saints=icons_saints)
        if pravicon_saint_id:
            if pravicon_saint_id in [pravicon_saint_id for _, pravicon_saint_id in pravicon_saints_ids]:
                # logging.error(saint.slug)
                # logging.error(str(pravicon_saint_id))
                # logging.error('- - -')
                continue
            pravicon_saints_ids.append((saint, pravicon_saint_id))
    return pravicon_saints_ids


def __prepare_saint_name(
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


def _find_pravicon_saint_id(saint_name: str, *, icons_saints: list[Tag]) -> int | None:
    for icon_saint in icons_saints:
        collected_saint_name: str = __final_prepare_collected_saint_name(icon_saint.text)
        if saint_name == collected_saint_name:
            return __collect.collect_pravicon_saint_id(icon_saint)
    for icon_saint in icons_saints:
        collected_saint_name: str = __final_prepare_collected_saint_name(icon_saint.text)
        saint_name, collected_saint_name = ___final_common_prepare_saint_name(saint_name, collected_saint_name)
        if collected_saint_name == saint_name:
            return __collect.collect_pravicon_saint_id(icon_saint)
    return None


def ___common_prepare_saint_name(some_saint_name: str) -> str:
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


def __final_prepare_collected_saint_name(collected_saint_name: str) -> str:
    collected_saint_name: str = ___common_prepare_saint_name(collected_saint_name)
    collected_saint_name: str = ___prepare_collected_saint_name(collected_saint_name)
    collected_saint_name: str = ___prepare_collected_saint_name(collected_saint_name)
    collected_saint_name: str = ___common_prepare_saint_name(collected_saint_name)
    return collected_saint_name


def ___prepare_collected_saint_name(collected_saint_name: str) -> str:
    collected_saint_name = collected_saint_name.strip()
    if collected_saint_name[-1] == '.':
        if collected_saint_name.rfind(',') != -1:
            collected_saint_name = collected_saint_name[:collected_saint_name.rfind(',')]  # name, прп.
        else:
            collected_saint_name = collected_saint_name[:collected_saint_name.rfind(' ')]  # name прп.
    return collected_saint_name


def ___final_common_prepare_saint_name(some_saint_name_1: str, some_saint_name_2) -> tuple[str, str]:
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


def ___sequence_matcher(saint_name: str, *, collected_saint_name: str) -> None:
    if SequenceMatcher(None, saint_name, collected_saint_name).ratio() > 0.80:
        logging.error(f'{saint_name}')
        logging.error(collected_saint_name)
        logging.warning('- - -')
