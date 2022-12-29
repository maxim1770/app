# TODO создать файл с title_en всех соборов,
#  чтобы при парсинге, мы смотрели в этот файл, и если есть, то пропускали, т.к парсим Святых

import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

from app.create import const


def collect_all_cathedrals_saints():
    req = requests.get(f'{const.AZBYKA_NETLOC}/days/sobory-svjatyh')

    table: Tag = BeautifulSoup(req.text, "lxml").find('table', class_="menology")

    cathedrals_saints_data: list[Tag] = table.find_all('tr')

    cathedrals_saints: list[str] = []

    for cathedral_saints in cathedrals_saints_data:
        cathedrals_saints.append(
            cathedral_saints.find('a')['href'].replace('/days/sv-', '').strip()
        )

    return cathedrals_saints


def write_all_cathedrals_saints(cathedrals_saints: list[str]):
    path: Path = Path('all_cathedrals_saints.json')
    path.write_text(json.dumps(cathedrals_saints), encoding='utf-8')


def main():
    cathedrals_saints = collect_all_cathedrals_saints()
    write_all_cathedrals_saints(cathedrals_saints)


if __name__ == '__main__':
    main()
