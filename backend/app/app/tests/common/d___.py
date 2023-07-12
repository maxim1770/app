from calendar import monthrange

if __name__ == '__main__':
    d: dict[int, dict[int, list]] = {
        month_num: {day_num: [] for day_num in range(1, monthrange(2033, month_num + 1)[1])} for
        month_num in range(1, 12 + 1)
    }
    d[3][1].append(3)
    print(d[3])
    # print(dict(filter(lambda x: x[1], d.items())))

    # d = {1:list_ for month_num, days_nums_dict in d.items() for day_num, list_ in days_nums_dict.items() if list_}
    # print(d)

    d: dict[int, dict[int, list]] = {
        month_num: {day_num: list_ for day_num, list_ in days_nums_dict.items() if list_} for
        month_num, days_nums_dict in d.items()
    }
    d = {month_num: days_nums_dict for month_num, days_nums_dict in d.items() if days_nums_dict}
    print(d)
