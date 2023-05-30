from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models
from .dignity import DignityFilter
from .face_sanctity import FaceSanctityFilter
from ..book import BookFilter


class SaintFilter(Filter):
    dignity: DignityFilter | None = FilterDepends(with_prefix('dignity', DignityFilter))
    face_sanctity: FaceSanctityFilter | None = FilterDepends(with_prefix('face_sanctity', FaceSanctityFilter))
    book: BookFilter | None = FilterDepends(with_prefix('book', BookFilter))
    # books__isnull: bool | None

    search: str | None

    order_by: list[str] = ['name', 'face_sanctity_id', 'dignity_id']

    class Constants(Filter.Constants):
        model = models.Saint
        search_model_fields = ['name', 'slug']
