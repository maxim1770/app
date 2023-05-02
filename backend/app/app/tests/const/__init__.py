from datetime import date

from bs4 import NavigableString, Tag

from app.create.const import AzbykaUrl
from app.create.prepare.base_collect import get_holidays_new_in_day


def main():
    day = date(2031, 9, 1)
    all_holidays: list[Tag] = get_holidays_new_in_day(day)
    saints_holidays: list[Tag] = []
    for holiday in all_holidays:
        if AzbykaUrl.GET_SAINT_BY_SLUG in holiday['href'].replace('http:', 'https:').lower().strip() \
                and not isinstance(holiday.previous_sibling, NavigableString) \
                and 'p-znaki-prazdnikov' in holiday.previous_sibling['href']:
            print(holiday)
            print(holiday.next_sibling is None)

            # print('- - -')
            # if holiday.next_sibling is None or holiday.next_sibling.next_sibling is None:
            #     print('fsf')
            #     if or 'p-znaki-prazdnikov' in holiday.next_sibling.next_sibling['href']:


if __name__ == '__main__':
    # main()
    day = date(2031, 9, 2)
    # saints_holidays = get_saints_holidays_new_in_day(day)
    # for saint_holiday in saints_holidays:
    #     print(saint_holiday)

    all_holidays: list[Tag] = get_holidays_new_in_day(day)
    print('href' in all_holidays[4].next_sibling.next_sibling.next_element.name)

    # for saint_holiday in saints_holidays:
    #     if not isinstance(saint_holiday.previous_sibling, NavigableString) \
    #             and 'p-znaki-prazdnikov' in saint_holiday.previous_sibling['href'] \
    #             and (
    #             saint_holiday.next_sibling.next_sibling is None
    #             or 'p-znaki-prazdnikov' in saint_holiday.next_sibling.next_sibling['href']
    #     ):
    #         print(saint_holiday)

    # print('text ', saint_holiday)

    # for a in [saints_holidays[0], saints_holidays[1], saints_holidays[4]]:
    #     print(a)
    #     var = a.previous_sibling
    #     print(var)
    #     print(type(var))
    #     print(isinstance(var, NavigableString))
    #     print('- - -')
