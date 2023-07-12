def _(first_rule_num: int, end_rule_num: int, page_num: int) -> None:
    for i in range(first_rule_num, end_rule_num + 1):
        print(f'            ({i}, {page_num}),')
    print()
    # print(f'    foo({end_rule_num + 1}, {end_rule_num + 1}, {page_num + 1})')
    print(f'({end_rule_num + 1}, {end_rule_num + 1}, {page_num + 1})')


if __name__ == '__main__':
    _(7, 7, 715)
