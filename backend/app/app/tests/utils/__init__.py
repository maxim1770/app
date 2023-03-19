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
    main_3_offset_pages(s)
