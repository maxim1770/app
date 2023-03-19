from datetime import timedelta, date as date_type

import pytest

from app import enums
from app.create import const
from app.create.prepare.movable_date.from_movable_date import from_movable_date

TEST_MAP_CYCLE_1: list[tuple[tuple[enums.CycleNum, int, int], date_type]] = [
    (
        (enums.CycleNum.cycle_1, 1, 0),
        const.const.DATE_PASKHA),
    (
        (enums.CycleNum.cycle_1, 1, 1),
        const.DATE_PASKHA + timedelta(days=1)),
    (
        (enums.CycleNum.cycle_1, 2, 0),
        const.DATE_PASKHA + timedelta(weeks=1)),
    (
        (enums.CycleNum.cycle_1, 2, 2),
        const.DATE_PASKHA + timedelta(weeks=1, days=2)),
    (
        (enums.CycleNum.cycle_1, 4, 4),
        const.DATE_PASKHA + timedelta(weeks=3, days=4)),
    (
        (enums.CycleNum.cycle_1, 8, 6),
        const.DATE_PASKHA + timedelta(weeks=7, days=6)),
]


@pytest.mark.parametrize('movable_date, date', TEST_MAP_CYCLE_1)
def test_from_movable_date_cycle_1(movable_date: tuple[enums.CycleNum, int, int], date: date_type):
    assert from_movable_date(*movable_date) == date


TEST_MAP_CYCLE_2: list[tuple[tuple[enums.CycleNum, int, int], date_type]] = [
    (
        (enums.CycleNum.cycle_2, 1, 0),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1)),
    (
        (enums.CycleNum.cycle_2, 1, 1),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(days=1)),
    (
        (enums.CycleNum.cycle_2, 2, 0),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(weeks=1)),
    (
        (enums.CycleNum.cycle_2, 2, 2),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(weeks=1, days=2)),
    (
        (enums.CycleNum.cycle_2, 4, 4),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(weeks=3, days=4)),
    (
        (enums.CycleNum.cycle_2, 35, 6),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(weeks=34, days=6)),
    (
        (enums.CycleNum.cycle_2, 36, 0),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1) + timedelta(weeks=35, days=0)),
]


@pytest.mark.parametrize('movable_date, date', TEST_MAP_CYCLE_2)
def test_from_movable_date_cycle_2(movable_date: tuple[enums.CycleNum, int, int], date: date_type):
    assert from_movable_date(*movable_date) == date


TEST_MAP_CYCLE_3: list[tuple[tuple[enums.CycleNum, int, int], date_type]] = [
    (
        (enums.CycleNum.cycle_3, 1, 0),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2)),
    (
        (enums.CycleNum.cycle_3, 1, 1),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2) + timedelta(
            days=1)),
    (
        (enums.CycleNum.cycle_3, 2, 0),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2) + timedelta(
            weeks=1)),
    (
        (enums.CycleNum.cycle_3, 2, 2),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2) + timedelta(
            weeks=1,
            days=2)),
    (
        (enums.CycleNum.cycle_3, 4, 4),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2) + timedelta(
            weeks=3,
            days=4)),
    (
        (enums.CycleNum.cycle_3, 8, 6),
        const.DATE_PASKHA + timedelta(days=const.NumMovableDay.IN_CYCLE_1 + const.NumMovableDay.IN_CYCLE_2) + timedelta(
            weeks=7,
            days=6)),
]


@pytest.mark.parametrize('movable_date, date', TEST_MAP_CYCLE_3)
def test_from_movable_date_cycle_3(movable_date: tuple[enums.CycleNum, int, int], date: date_type):
    assert from_movable_date(*movable_date) == date
