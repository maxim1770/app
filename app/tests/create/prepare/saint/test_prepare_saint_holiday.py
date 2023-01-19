from app.create.prepare.saint.prepare_saint_data import PrepareSaintHoliday, CollectedSaintHoliday


def test_find_year_in_saint_title_warning():
    saint_holiday = CollectedSaintHoliday(
        saint_slug='foo',
        full_title=''
    )
    prepare_saint_holiday = PrepareSaintHoliday(saint_holiday)
    assert prepare_saint_holiday
