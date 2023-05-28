from typing import Match

from app.const import YearRegex


def main():
    s = """
        1
    10 31 35 38 45 48 51 54 54 57 72 75 89 90 107 121 122 124 126
    127 176 210 220 228 234 241 243 256 259 294 340 369 404 442
        """
    l = []
    start_year = 1113
    for i in s.split():
        l.append((start_year, int(i)))
        start_year += 1

    for i in l:
        print(i, end='')
        print(',')


def _delete_year_in_brackets(title: str) -> str:
    match: Match[str] | None = YearRegex.FIND_YEAR.search(title)
    if not match:
        return title
    year_title: str = match[0]
    title: str = title.replace(f'({year_title})', '')
    title = title.strip()
    return title


def __prepare_title(title: str) -> str:
    title = title.strip()
    title = title[0].upper() + title[1:]
    title = title.replace(' ,', ',').replace('  ', ' ').replace(' .', '')
    title = ' '.join(title.split())
    title = title.strip()
    return title


def main_1_split_on_bookmarks_and_prepare_title(s) -> str:
    out = ''
    l = []
    for i in s.split('…'):
        l.append(' '.join(i.split()).strip())

    for title in l:
        for title in title.split('.'):
            # title: str = _delete_year_in_brackets(title)
            if not title:
                continue
            title = __prepare_title(title)
            title = title.strip()
            out += title + '\n'
    return out


if __name__ == '__main__':
    s = """

        """
    main_1_split_on_bookmarks_and_prepare_title(s)
