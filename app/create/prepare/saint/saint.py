from bs4 import Tag
from requests import Session

from app import enums, schemas
from ..base_collect import collect_saint_data


class SaintDataUpdateFactory(object):

    def __init__(self, session: Session, *, saint_slug: str):
        self.saint_data_collect: Tag = collect_saint_data(session, saint_slug=saint_slug)

    @property
    def _name_data(self) -> Tag:
        return self.saint_data_collect.find('h1')

    @property
    def saint_in(self) -> schemas.SaintUpdate:
        name: str = ' '.join(self._name_data.text.split())
        return schemas.SaintUpdate(name=name)

    @property
    def face_sanctity_title(self) -> enums.FaceSanctityTitle:
        face_sanctity_text: str = self._name_data.find(
            lambda tag: tag.name == 'a' and 'p-tip-svjatosti' in tag['href']
        ).text
        face_sanctity_title: enums.FaceSanctityTitle = enums.FaceSanctityTitle(
            face_sanctity_text.lower().strip()
        )
        return face_sanctity_title

    @property
    def dignity_title(self) -> enums.DignityTitle | None:
        dignity_tag: Tag | None = self._name_data.find(lambda tag: tag.name == 'a' and 'p-san' in tag['href'])
        dignity_text: str | None = dignity_tag.text if dignity_tag else None
        dignity_title: enums.DignityTitle | None = enums.DignityTitle(
            dignity_text.replace(',', '').strip()
        ) if dignity_text else None
        return dignity_title

    def get(self) -> schemas.SaintDataUpdate:
        return schemas.SaintDataUpdate(
            saint_in=self.saint_in,
            face_sanctity_title=self.face_sanctity_title,
            dignity_title=self.dignity_title
        )
