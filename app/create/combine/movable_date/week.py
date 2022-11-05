from pydantic import parse_obj_as

from app import schemas


def combine_fields_weeks(
        weeks_titles: list[str | None],
        weeks_nums: list[int | None],
        sundays_titles: list[str],
        sundays_nums: list[int]
) -> list[schemas.WeekCreate]:
    weeks_data: list[dict[str, str | int | None]] = [
        {'title': title, 'num': num, 'sunday_title': sunday_title, 'sunday_num': sunday_num}
        for title, num, sunday_title, sunday_num in
        zip(weeks_titles, weeks_nums, sundays_titles, sundays_nums)
    ]

    return parse_obj_as(list[schemas.WeekCreate], weeks_data)
