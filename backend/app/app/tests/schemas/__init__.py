def main_2_add_brackets_and_offset_years(s: str) -> str:
    out = ''
    for i in s.split('\n'):
        i = i.strip()
        if i == '':
            continue
        if '!!!' in i:
            title, year = i.split('!!!')
            title = title.strip()
            year = year.strip()
            year = int(year) - 8
            out += f"    (('{title}', {year}), )," + '\n'
            continue
        out += f"    ('{i}', )," + '\n'
    return out


if __name__ == '__main__':
    s = """
    
    """
    print(main_2_add_brackets_and_offset_years(s))
