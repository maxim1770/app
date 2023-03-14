import pytest

from app.create.prepare.year import PrepareYearTitle


@pytest.mark.parametrize('year_title, prepared_year_title', [
    ('1531 г.', '1539'),
    ('Середина XVI в.', 'Середина XVI'),
    ('1282-1283 г.', '1290-1291'),
    ('1156 - 1163', '1164-1171'),
    ('XIII - XV вв.', 'XIII-XV'),
    ('Первая половина XIV в.', 'Первая половина XIV'),
    ('Вторая половина XV в.', 'Вторая половина XV'),
    ('Последняя четверть X в', 'Последняя четверть X'),
    ('Вторая треть XVI в.', 'Вторая треть XVI'),
    ('Третья четверть X в', 'Третья четверть X'),
    ('Последняя треть XV в.', 'Последняя треть XV'),
    ('Посл. четв. XV в.', 'Последняя четверть XV'),
    ('Перв. четв. XV в.', 'Первая четверть XV'),
    ('последняя треть X в', 'Последняя треть X'),
    ('Конец XII в.', 'Конец XII'),
    ('Начало XIV в.', 'Начало XIV'),
    # ('1540-е', '1550-е'), ('1560-1570-е', '1570-1580-е'), ('1460-е гг.', '1470-е')
])
def test_prepare_year_title(year_title: str, prepared_year_title: str):
    assert PrepareYearTitle(year_title).year_title == prepared_year_title


@pytest.mark.parametrize('year_title, prepared_year_title', [
    ('Конец XII в. (?)', 'Конец XII в. (?)'),
])
def _test_prepare_year_title_hard(year_title: str, prepared_year_title: str):
    assert PrepareYearTitle(year_title).year_title == prepared_year_title
