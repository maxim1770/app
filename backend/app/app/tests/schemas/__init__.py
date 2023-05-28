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


def main_3_offset_pages(s, *, num_offset_pages: int = 4) -> str:
    out = ''
    for i in s.split('\n'):
        if not i or i == ' ':
            continue
        if i.strip() == '-':
            # print(i)
            continue
        page_str = i[-5:-2].strip()
        if ',' in page_str:
            page_str = page_str.replace(',', '').strip()
        page = int(page_str)
        page_new = page - num_offset_pages
        out += i.replace(str(page), str(page_new)) + '\n'
    return out



if __name__ == '__main__':
    s = """
    
    """
    print(main_2_add_brackets_and_offset_years(s))

    s = """
    """
    main_3_offset_pages(s)
