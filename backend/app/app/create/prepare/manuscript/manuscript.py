from uuid import UUID

import requests
from pydantic import ValidationError

from app import enums
from app.schemas import ManuscriptDataCreateAny, ManuscriptDataCreate, ManuscriptCreate, YearCreate
from .collect_manuscript_data import CollectManuscriptDataFromNeb, CollectManuscriptDataFromRsl, \
    CollectManuscriptDataFromNlr
from .search_manuscript import SearchManuscriptFactory, SearchManuscriptInNeb
from ..base_classes import PrepareError


class CollectManuscriptDataFactory(object):

    @classmethod
    def get_by_manuscript_code(
            self,
            session: requests.Session,
            *,
            manuscript_code: UUID | str
    ) -> CollectManuscriptDataFromRsl | CollectManuscriptDataFromNlr | CollectManuscriptDataFromNeb:
        if isinstance(manuscript_code, UUID):
            collect_manuscript_data = CollectManuscriptDataFromNlr(session, manuscript_code=manuscript_code)
        else:
            collect_manuscript_data = CollectManuscriptDataFromRsl(session, manuscript_code=manuscript_code)
        search_manuscript_in_neb = SearchManuscriptInNeb(
            session,
            manuscript_code_title=collect_manuscript_data.manuscript_code_title
        )
        if not search_manuscript_in_neb.manuscript_neb_slug:
            return collect_manuscript_data
        collect_manuscript_data_from_neb = CollectManuscriptDataFromNeb(
            session,
            manuscript_code=search_manuscript_in_neb.manuscript_neb_slug
        )
        if collect_manuscript_data.manuscript_code_title != collect_manuscript_data_from_neb.manuscript_code_title:
            raise PrepareError(
                f'Manuscript_code_title in libs не равны {collect_manuscript_data.manuscript_code_title} != {collect_manuscript_data_from_neb.manuscript_code_title}'
            )
        return collect_manuscript_data_from_neb


class ManuscriptDataCreateFactory(object):

    def __init__(
            self,
            session: requests.Session,
            *,
            manuscript_data_in_any: ManuscriptDataCreateAny
    ):
        if manuscript_data_in_any.manuscript_in.neb_slug:
            self.collect_manuscript_data = CollectManuscriptDataFromNeb(
                session,
                manuscript_code=manuscript_data_in_any.manuscript_in.neb_slug
            )
            search_manuscript = SearchManuscriptFactory.get(
                session,
                manuscript_code_title=self.collect_manuscript_data.manuscript_code_title
            )
            manuscript_code: UUID | str = search_manuscript.manuscript_code
            manuscript_data_in_any.manuscript_in.code = manuscript_code
        elif manuscript_data_in_any.manuscript_in.code:
            self.collect_manuscript_data = CollectManuscriptDataFactory.get_by_manuscript_code(
                session,
                manuscript_code=manuscript_data_in_any.manuscript_in.code
            )
            if isinstance(self.collect_manuscript_data, CollectManuscriptDataFromNeb):
                manuscript_neb_slug: str = self.collect_manuscript_data._manuscript_code
                manuscript_data_in_any.manuscript_in.neb_slug = manuscript_neb_slug
        self._manuscript_data_in_any = manuscript_data_in_any

    @property
    def _year_in(self) -> YearCreate:
        if not self._manuscript_data_in_any.year_in:
            try:
                return self.collect_manuscript_data.year_in
            except (ValidationError, ValueError) as e:
                raise PrepareError(e.args[0])
        return self._manuscript_data_in_any.year_in

    @property
    def _fund_title(self) -> enums.FundTitle:
        if not self._manuscript_data_in_any.fund_title:
            return self.collect_manuscript_data.fund_title
        return self._manuscript_data_in_any.fund_title

    @property
    def _manuscript_in(self) -> ManuscriptCreate:
        if not self._manuscript_data_in_any.manuscript_in.title:
            self._manuscript_data_in_any.manuscript_in.title = self.collect_manuscript_data.manuscript_title
        if not self._manuscript_data_in_any.manuscript_in.code_title:
            self._manuscript_data_in_any.manuscript_in.code_title = self.collect_manuscript_data.manuscript_code_title
        manuscript_in = ManuscriptCreate(**self._manuscript_data_in_any.manuscript_in.dict())
        return manuscript_in

    def get(self) -> ManuscriptDataCreate:
        return ManuscriptDataCreate(
            manuscript_in=self._manuscript_in,
            fund_title=self._fund_title,
            year_in=self._year_in,
        )
