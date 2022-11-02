from bs4.element import Tag
from pydantic import parse_obj_as

from app import schemas
from app.create import prepare


def combine_fields_for_c1_days(
        # c1_days_abbrs: list[schemas.DayAbbrEnum],
        # c1_days_titles: list[str | None]
) -> list[schemas.DayCreate]:
    table: Tag = prepare.collect_table()

    prepare_day: prepare.PrepareDay = prepare.PrepareDay(table=table)
    prepare_c1_day: prepare.PrepareС1Day = prepare.PrepareС1Day(prepare_day.data.copy())
    c1_days_abbrs: list[schemas.DayAbbrEnum] = prepare.PrepareС1DayAbbr(prepare_c1_day.data.copy()).data
    c1_days_titles: list[str | None] = prepare.PrepareС1DayTitle(prepare_c1_day.data.copy()).data

    days_data: list[dict[str, schemas.DayAbbrEnum | str | None]] = [
        {'abbr': abbr, 'title': title}
        for abbr, title in
        zip(c1_days_abbrs, c1_days_titles)
    ]

    days: list[schemas.DayCreate] = parse_obj_as(list[schemas.DayCreate], days_data)
    return days
