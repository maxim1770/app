import requests
from bs4 import Tag

from app import enums, schemas, utils
from ..base_collect import collect_saint_data


class SaintDataUpdateFactory(object):

    def __init__(self, session: requests.Session, *, saint_slug: str):
        self._saint_data_collect: Tag = collect_saint_data(session, saint_slug=saint_slug)
        self._saint_slug = saint_slug

    @property
    def _name_data(self) -> Tag:
        return self._saint_data_collect.find('h1')

    @property
    def name_in_dative(self) -> str | None:
        try:
            names_in_dative: list[str] = [
                name_in_dative_tag_.find('h3').text for name_in_dative_tag_ in
                self._saint_data_collect.find('div', class_='boxes').find_all('div', class_='frame')
            ]
        except AttributeError:
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
        return name_in_dative

    @property
    def saint_in(self) -> schemas.SaintUpdate:
        name: str = utils.clean_extra_spaces(self._name_data.text)
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
        return schemas.SaintUpdate(name=name, name_in_dative=self.name_in_dative)

    @property
    def face_sanctity_title(self) -> enums.FaceSanctityTitle:
        face_sanctity_text: str = self._name_data.find(
            lambda tag: tag.name == 'a' and 'p-tip-svjatosti' in tag['href']
        ).text
        face_sanctity_text: str = utils.clean_extra_spaces(face_sanctity_text)
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
