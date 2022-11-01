from pathlib import Path

from bs4 import BeautifulSoup
from bs4.element import Tag


def collect_table(path_to_index: Path = Path('../../../data/index.html')) -> Tag:
    """

    :param path_to_index: Насчет пути по умолчанию СКОРЕЕ ВСЕГО НЕПРАВИЛЬНО
    """
    src: str = path_to_index.read_text(encoding="utf-8")

    soup: BeautifulSoup = BeautifulSoup(src, "lxml")

    table: Tag = soup.find("table", class_="adaptive").find("tbody")

    return table
