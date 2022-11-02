from bs4.element import Tag
from pydantic import parse_obj_as

from app import schemas
from app.create import prepare


def combine_fields_for_c1_weeks(
        # c1_sundays_nums: list[int],
        # c1_sundays_titles: list[str],
        # c1_weeks_nums: list[int],
        # c1_weeks_titles: list[str]
) -> list[schemas.WeekCreate]:
    table: Tag = prepare.collect_table()

    prepare_sunday: prepare.PrepareSunday = prepare.PrepareSunday(table=table)
    prepare_c1_sunday: prepare.PrepareС1Sunday = prepare.PrepareС1Sunday(prepare_sunday.data.copy())
    c1_sundays_nums: list[int] = prepare.PrepareС1SundayNum(prepare_c1_sunday.data.copy()).data
    c1_sundays_titles: list[str] = prepare.PrepareС1SundayTitle(prepare_c1_sunday.data.copy()).data

    prepare_week: prepare.PrepareWeek = prepare.PrepareWeek(table=table)
    prepare_c1_week: prepare.PrepareС1Week = prepare.PrepareС1Week(prepare_week.data.copy())
    c1_weeks_nums: list[int] = prepare.PrepareС1WeekNum(prepare_c1_week.data.copy()).data
    c1_weeks_titles: list[str] = prepare.PrepareС1WeekTitle(prepare_c1_week.data.copy()).data

    weeks_data: list[dict[str, str | int]] = [
        {'title': title, 'num': num, 'sunday_title': sunday_title, 'sunday_num': sunday_num}
        for title, num, sunday_title, sunday_num in
        zip(c1_weeks_titles, c1_weeks_nums, c1_sundays_titles, c1_sundays_nums)
    ]

    weeks: list[schemas.WeekCreate] = parse_obj_as(list[schemas.WeekCreate], weeks_data)
    return weeks
