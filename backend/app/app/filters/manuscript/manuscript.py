from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from app import models
from .fund import FundFilter
from ..year import YearFilter


class ManuscriptFilter(Filter):
    handwriting__lt: int | None
    handwriting__gte: int | None
    year: YearFilter | None = FilterDepends(with_prefix('year', YearFilter))
    fund: FundFilter | None = FilterDepends(with_prefix('fund', FundFilter))
    search: str | None
    order_by: list[str] = ['handwriting']

    class Constants(Filter.Constants):
        model = models.Manuscript
        search_model_fields = ['title', 'code_title']
