import logging

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import schemas, crud, models, enums
from app.api import deps
from app.create import const
from app.create.create.saint.dignity import create_dignities
from app.create.create.saint.face_sanctity import create_faces_sanctity
from app.db.session import engine, Base

logging.basicConfig(level=logging.INFO)


class UpdateSaintData(BaseModel):
    name: str
    face_sanctity_title: enums.FaceSanctityTitle
    dignity_title: enums.DignityTitle | None


def collect_saint_data(saint_slug: str) -> Tag:
    req = requests.get(f'{const.AZBYKA_NETLOC}/days/sv-{saint_slug}')

    saint_data: Tag = BeautifulSoup(req.text, "lxml").find('div', {'id': 'main'})

    return saint_data


def prepare_saint_data(collected_saint_data: Tag) -> UpdateSaintData:
    name_tag: Tag = collected_saint_data.find('h1')
    name: str = ' '.join(name_tag.text.split())

    face_sanctity_text: str = name_tag.find(lambda tag: tag.name == 'a' and 'p-tip-svjatosti' in tag['href']).text
    face_sanctity_title: enums.FaceSanctityTitle = enums.FaceSanctityTitle(
        face_sanctity_text.lower().strip()
    )

    dignity_tag: Tag | None = name_tag.find(lambda tag: tag.name == 'a' and 'p-san' in tag['href'])
    dignity_text: str | None = dignity_tag.text if dignity_tag else None
    dignity_title: enums.DignityTitle | None = enums.DignityTitle(
        dignity_text.replace(',', '').strip()
    ) if dignity_text else None

    return UpdateSaintData(name=name, face_sanctity_title=face_sanctity_title, dignity_title=dignity_title)


def update_saint_data(db: Session, saint: models.Saint, updated_saint_data: UpdateSaintData):
    if saint.name is None:
        saint.name = updated_saint_data.name

    if saint.face_sanctity is None:
        face_sanctity: models.FaceSanctity = crud.get_face_sanctity(db, title=updated_saint_data.face_sanctity_title)
        saint.face_sanctity = face_sanctity

    if saint.dignity is None and updated_saint_data.dignity_title:
        dignity: models.Dignity = crud.get_dignity(db, title=updated_saint_data.dignity_title)
        saint.dignity = dignity

    db.add(saint)
    db.commit()
    db.refresh(saint)


def main(db: Session):
    saints: list[models.Saint] = crud.get_saints(db, skip=200, limit=2000)

    for saint in saints:
        collected_saint_data: Tag = collect_saint_data(saint.slug)
        updated_saint_data: UpdateSaintData = prepare_saint_data(collected_saint_data)

        # TODO: тут возможно стоит поменять логику и сначала,
        #  проверять есть ли значение в базе данных, и только если нет, то парсить и добавлять

        update_saint_data(db, saint=saint, updated_saint_data=updated_saint_data)


if __name__ == '__main__':
    db: Session = deps.get_db().__next__()
    Base.metadata.create_all(bind=engine)

    # create_dignities(db)
    # create_faces_sanctity(db)

    main(db)
