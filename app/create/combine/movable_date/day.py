from pydantic import parse_obj_as

from app import schemas


def combine_fields_for_days(
        days_abbrs: list[schemas.DayAbbrEnum],
        days_titles: list[str | None]
) -> list[schemas.DayCreate]:
    days_data: list[dict[str, schemas.DayAbbrEnum | str | None]] = [
        {'abbr': abbr, 'title': title}
        for abbr, title in
        zip(days_abbrs, days_titles)
    ]

    return parse_obj_as(list[schemas.DayCreate], days_data)
