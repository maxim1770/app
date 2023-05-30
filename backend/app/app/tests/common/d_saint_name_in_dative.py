import logging

import requests

from app import utils, crud
from app.api import deps
from app.create.prepare.base_collect import collect_saint_data

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def find_saint_name_in_dative(saint_slug: str) -> str | None:
    logging.info(saint_slug)
    try:
        names_in_dative: list[str] = [
            name_in_dative_tag_.find('h3').text for name_in_dative_tag_ in
            collect_saint_data(session, saint_slug=saint_slug).find('div', class_='boxes').find_all('div',
                                                                                                    class_='frame')
        ]
    except AttributeError:
        logging.info('- - -')
        return None
    if not names_in_dative:
        return None
    name_in_dative = names_in_dative[0]
    if 'апостолам,' in name_in_dative:
        if len(names_in_dative) > 1:
            name_in_dative = names_in_dative[1]
            names_in_dative = names_in_dative[1:]
        else:
            return None
    if names_in_dative_not_has_i := [name_in_dative for name_in_dative in names_in_dative
                                     if ' и ' not in name_in_dative]:
        name_in_dative = names_in_dative_not_has_i[0]
    name_in_dative: str = utils.clean_extra_spaces(name_in_dative)
    name_in_dative = name_in_dative.replace(', на обретение мощей', '').replace(', на перенесение мощей', '')
    if 'глас' in name_in_dative:
        if name_in_dative[-1].isdigit():
            name_in_dative = name_in_dative[:-1]
        name_in_dative = name_in_dative.replace(', глас', '')
        name_in_dative: str = utils.clean_extra_spaces(name_in_dative)
    name_in_dative: str = utils.common_prepare_text(name_in_dative)
    name_in_dative = name_in_dative.replace('Ин ', '')
    name_in_dative = ' '.join(name_in_dative.split()[1:])
    name_in_dative: str = utils.clean_extra_spaces(name_in_dative)
    if name_in_dative == 'апостолам':
        return None
    logging.warning(name_in_dative)
    logging.info('- - -')
    return name_in_dative


if __name__ == '__main__':
    db = next(deps.get_db())
    session: requests.Session = next(deps.get_session())

    for saint in crud.saint.get_multi(db, limit=3000):
        if not saint.name_in_dative:
            name_in_dative: str | None = find_saint_name_in_dative(saint_slug=saint.slug)
            if name_in_dative:
                saint.name_in_dative = name_in_dative
                db.add(saint)
                db.commit()
                db.refresh(saint)
