from .movable_date import PrepareWeek, \
    PrepareC1Week, PrepareC1WeekNum, PrepareC1WeekTitle, \
    PrepareC2Week, PrepareC2WeekNum, PrepareC2WeekTitle, \
    PrepareSunday, \
    PrepareC1Sunday, PrepareC1SundayNum, PrepareC1SundayTitle, \
    PrepareC2Sunday, PrepareC2SundayNum, PrepareC2SundayTitle, \
    prepare_fields_c1_weeks, prepare_fields_c2_weeks
from .movable_date import PrepareDay, PrepareC1Day, PrepareC1DayAbbr, PrepareC1DayTitle, \
    prepare_fields_c1_days, prepare_fields_c2_days
from .movable_date import PrepareSundayMatins, PrepareC1SundayMatins, PrepareC2SundayMatins, \
    PrepareC1SundayVespers, \
    prepare_c1_sundays_matins, prepare_c2_sundays_matins

from .bible_book import PrepareEvangelZachalo, PrepareC1EvangelZachalo, \
    PrepareC1EvangelZachaloNum, PrepareC1EvangelAbbr, \
    PrepareApostleZachalo, PrepareC1ApostleZachalo, \
    prepare_fields_c1_zachalos, \
    prepare_с1_bible_books_abbrs

from .base_collect import collect_table
