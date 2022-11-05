from pydantic import parse_obj_as

from app.create import const
from app import schemas


def combine_fields_zachalos(
        zachalos_nums: list[int],
        zachalos_titles: list[str | None]
) -> list[schemas.ZachaloCreate]:
    zachalos_data: list[dict[str, int | str | None]] = [
        {'num': num, 'title': title}
        for num, title in
        zip(zachalos_nums, zachalos_titles)
    ]

    return parse_obj_as(list[schemas.ZachaloCreate], zachalos_data)
