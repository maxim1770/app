import requests
from bs4 import Tag

from app import enums, schemas
from ..base_collect import collect_saint_data


class SaintDataUpdateFactory(object):

    def __init__(self, session: requests.Session, *, saint_slug: str):
        self.saint_data_collect: Tag = collect_saint_data(session, saint_slug=saint_slug)

    @property
    def _name_data(self) -> Tag:
        return self.saint_data_collect.find('h1')

    @property
    def saint_in(self) -> schemas.SaintUpdate:
        name: str = ' '.join(self._name_data.text.split())
        name = name.replace(' и и евангелист', '')
        name = name.replace(' и евангелист', '')
        name = name.replace('юродивый', 'Юродивый')
        name = name.replace(
            self.face_sanctity_title.capitalize(),
            self.face_sanctity_title
        )
        if self.dignity_title:
            name = name.replace(
                self.dignity_title[0].lower() + self.dignity_title[1:],
                self.dignity_title
            )
        return schemas.SaintUpdate(name=name)

    @property
    def face_sanctity_title(self) -> enums.FaceSanctityTitle:
        face_sanctity_text: str = self._name_data.find(
            lambda tag: tag.name == 'a' and 'p-tip-svjatosti' in tag['href']
        ).text.strip()
        if face_sanctity_text.endswith('и евангелист'):
            face_sanctity_text = face_sanctity_text.replace('и евангелист', '').strip()
            if face_sanctity_text.endswith(' ' + 'и'):
                face_sanctity_text = face_sanctity_text[:-1].strip()
        for part_face_sanctit in ['Патриарх', 'Юродивый', 'Князь', 'Княгиня']:
            if face_sanctity_text.endswith(part_face_sanctit.lower()):
                face_sanctity_text = face_sanctity_text.replace(part_face_sanctit.lower(), part_face_sanctit)
                break
        face_sanctity_title = enums.FaceSanctityTitle(face_sanctity_text)
        return face_sanctity_title

    @property
    def dignity_title(self) -> enums.DignityTitle | None:
        dignity_tag: Tag | None = self._name_data.find(
            lambda tag: tag.name == 'a' and 'p-san' in tag['href']
        )
        dignity_text: str | None = dignity_tag.text if dignity_tag else None
        if not dignity_text:
            return None
        dignity_title = enums.DignityTitle(
            dignity_text.replace(',', '').strip().title()
        )
        return dignity_title

    def get(self) -> schemas.SaintDataUpdate:
        return schemas.SaintDataUpdate(
            saint_in=self.saint_in,
            face_sanctity_title=self.face_sanctity_title,
            dignity_title=self.dignity_title
        )
