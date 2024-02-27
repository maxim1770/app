from uuid import uuid4

from app import models, enums
from ._calendar_attribute import CalendarAttribute, HighlightColor, Highlight, Popover, Highlights


def prepare_some_day_attributes(some_day: models.Day | models.MovableDay) -> list[CalendarAttribute]:
    attributes: list[CalendarAttribute] = []
    for holiday in some_day.holidays:
        label = holiday.title
        if year := holiday.year:
            label += f' ({year.title})'
        match holiday.tipikon.title if holiday.tipikon else None:
            case enums.TipikonTitle.Velikij_Prazdnik:
                highlight = HighlightColor.red
                dot = None
                order = 4
            case enums.TipikonTitle.Srednij_Prazdnik | enums.TipikonTitle.Srednij_Prazdnik_Vsenoschnoe_Bdenie:
                highlight = Highlight(color=HighlightColor.red)
                dot = None
                order = 3
            case enums.TipikonTitle.Malyj_Prazdnik | enums.TipikonTitle.Malyj_Prazdnik_Slavoslovnaja_Sluzhba:
                highlight = None
                dot = HighlightColor.red
                order = 1
            case _:
                highlight = None
                dot = None
                order = 0
        attributes.append(
            CalendarAttribute(
                highlight=highlight,
                dot=dot,
                popover=Popover(label=label),
                order=order
            )
        )
    if len(some_day.before_after_holidays):
        __before_after_holiday = some_day.before_after_holidays[0].before_after_holiday
        label = __before_after_holiday.holiday.title
        key = __before_after_holiday.id
        if some_day.before_after_holidays[0].is_last_day:
            key = uuid4()
            label = label.replace('Попразднство', 'Отдание Праздника')
            highlight = Highlight(color=HighlightColor.red, fillMode='outline')
        else:
            __highlight = Highlight(color=HighlightColor.red)
            highlight = Highlights(start=__highlight, base=__highlight, end=__highlight)
        attributes.append(
            CalendarAttribute(
                key=key,
                highlight=highlight,
                popover=Popover(label=label),
                order=3
            )
        )
    return attributes
