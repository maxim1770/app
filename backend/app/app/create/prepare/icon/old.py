import logging
import re

import requests
from bs4 import Tag
from sqlalchemy.orm import Session

from app import crud, models, enums

# def collect_icons_desc_saint(icons: list[Tag]) -> list[str]:
#     icons_desc_saint: list[str] = [icon.find('p').text.replace('Описание:', '').strip() for icon in
#                                    icons
#                                    ]
#     return icons_desc_saint


REGEX_FIND_YEAR_: Pattern[str] = re.compile(
    r'''(?x)
    (ок\.|после|до)?
    \s?
    (?:\s?(\d+|[XVI]+)\s?(-|–)?){1,2}
    \s?
    (года|г{1,2}\.|в\.)?
    (\sдо\sР\.\sХ\.)?
    '''
)


def __find_face_sanctity_and_dignity_abbrs(saint_name: str) -> list[str]:
    # REGEX_FIND_FACE_SANCTITY: Pattern[str] = re.compile(r'''(?x),?\s?(?:[�-�]+\.\s?)''')  # +
    REGEX_FIND_FACE_SANCTITY: Pattern[str] = re.compile(
        r'''(?x)
        [�-�]{2,}\.
        '''
    )
    return REGEX_FIND_FACE_SANCTITY.findall(saint_name)


def __main_old(db: Session, *, session: requests.Session):
    icons_saints: list[Tag] = _collect_icons_saints(session)
    saints: list[models.Saint] = crud.saint.get_multi(db, limit=3000)
    # num: int = 0
    # num_eq: int = 0
    for saint in saints:
        if saint.name is None:
            continue
        # num += 1
        saint_dignity_title: enums.FaceSanctityTitle | None = saint.dignity.title if saint.dignity else None
        saint_name: str = _prepare_saint_name(
            saint.name,
            saint_face_sanctity_title=saint.face_sanctity.title,
            saint_dignity_title=saint_dignity_title
        )
        # flag = False

        for icon_saint in icons_saints:
            collected_saint_name: str = _prepare_collected_saint_name(icon_saint.text)
            if collected_saint_name == saint_name:
                logging.info(f'{saint_name} | {collected_saint_name}')
                int(icon_saint['href'].replace('/icon-', ''))
                num_eq += 1
                flag = False
                break

            # if SequenceMatcher(None, saint_name, collected_saint_name).ratio() > 0.93:
            #     logging.warning(f'{saint_name} | {collected_saint_name}')
            #     flag = True
            #
            # if SequenceMatcher(None, saint_name, collected_saint_name).ratio() > 0.87:
            #     logging.error(f'{saint_name} | {collected_saint_name}')

        # if flag:
        #     num_eq += 1
        #     # TODO: � ��� ��� ����������� (���������� pravicon_saint_id), ������� compare � ��������� > 0.93
        #     #  ������ ��� �� �����, ����� ������ ��� ����� ������ � ���������� � ������ ������� �� 100% ��������� ��� ����� � 100%

    # elif SequenceMatcher(None, saint_name, icon_saint_name).ratio() > 0.8:
    #     logging.warning(f'{saint_name} | {icon_saint_name}')

    # logging.warning(f'num: {num}')
    # logging.warning(f'num_eq: {num_eq}')

    ### �� if __name__ == '__main__':

    # import jellyfish

    # print(jellyfish.jaro_similarity(a, b))
    # s = jellyfish.levenshtein_distance(u'sjellyfsdffish', u'smellyfish')
    # print(s)
