from typing import Final

from bs4.element import Tag
from sqlalchemy.orm import Session

from app import schemas, crud


def pars_zachalo_num(db: Session, zachalo_tag: Tag) -> int:
    DOMIN_AZBYKA: str = 'https://azbyka.ru'
    tag_a: Tag = zachalo_tag.find('a', {'target': "BibleAV"})

    try:
        num: int = int(re.search(r'(?<=\[)\d*(?=\])', zachalo_tag.text)[0])
    except TypeError:
        req = requests.get(
            url=DOMIN_AZBYKA + tag_a['href'],
            headers=HEADERS
        )
        soup = BeautifulSoup(req.text, "lxml")

        num_str: str | None = None
        tag_div_verse: Tag = soup.find('div', {'class': 'crossref-verse', 'data-lang': 'r'})
        try:
            num_str: str = tag_div_verse.find('span', class_='zachala').text
        except AttributeError:
            try:
                # Когда zachala выше на один первого выделенного div
                num_str: str = tag_div_verse.find_previous_sibling('div').find(
                    'span',
                    class_='zachala').text

                print(zachalo_tag.text, 'Когда zachala выше на один первого выделенного div')
            except AttributeError:
                try:
                    # Когда zachala ниже (на 1 или больше) первого выделенного div, но находится так же в выделении
                    for div in tag_div_verse.find_next_siblings('div', {'class': 'crossref-verse'}):
                        tag_span: Tag = div.find('span', class_='zachala')
                        if tag_span:
                            num_str: str = tag_span.text
                            break

                    if not num_str:
                        raise AttributeError

                    print(zachalo_tag.text, 'Когда zachala ниже (на 1 или больше)')
                except AttributeError:
                    # Берем первое попавшееся zachala на странице
                    try:
                        num_str: str = soup.find('span', class_='zachala').text
                        print(zachalo_tag.text, 'Берем первое попавшееся zachala на странице')
                    except AttributeError:

                        # Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.
                        tag_a_nav_left: Tag = soup.find('span', class_="title-nav").find('a',
                                                                                         class_="icon-arrow-left")

                        req = requests.get(
                            url=DOMIN_AZBYKA + tag_a_nav_left['href'],
                            headers=HEADERS
                        )
                        soup = BeautifulSoup(req.text, "lxml")

                        for div in soup.find_all('div', {'data-lang': 'r'})[::-1]:
                            tag_span: Tag = div.find('span', class_='zachala')
                            if tag_span:
                                num_str: str = tag_span.text
                                break

                        if not num_str:
                            raise AttributeError

                        print(zachalo_tag.text,
                              'Когда zachala нет на странице, ищем самое нижнее zachala на предыдущей стр.')

        num: int = int(re.search(
            r'\d+',
            num_str
        )[0])

    return num


def create_c1_zachalos(db: Session, c1_apostles: list[Tag], c1_evangels: list[Tag]) -> bool:
    """
    Создает 110 = 8*7 + 8*7 - 2 (ПОКА ЧТО НЕ ПОЛУЧИЛОСЬ ДОБАВИТЬ ИХ) записи о Апостольских и Евангельских зачалах в таблице 'nums'.

    **Если записи уже есть, то ничего не создает, и возвращает 0.**

    **Большинство данных с парсера, но данные не надежны (номера зачал), возможны баги при получении данных с сайта azbyka.ru/biblia/...**

    :return: количество созданных записей в таблице.
    """
    number_zachalos: Final[int] = 110

    number_creatures: int = 0

    for zachalo_tag in c1_apostles + c1_evangels:
        zachalo: schemas.ZachaloCreate = schemas.ZachaloCreate(
            num=pars_zachalo_num(db, zachalo_tag=zachalo_tag)
        )

        tag_a: Tag = zachalo_tag.find('a', {'target': "BibleAV"})
        bible_book_abbr: schemas.AbbrEnum = schemas.AbbrEnum._value2member_map_[
            re.search(
                r'(?<=\?)\S+(?=\.)',
                tag_a['href']
            )[0]
        ]

        if crud.get_zachalo(db, bible_book_abbr=bible_book_abbr, num=zachalo.num):
            raise ValueError(
                f'Zachalo: bible_book_abbr={bible_book_abbr}, num={zachalo.num} уже была создана')
        else:
            crud.create_zachalo(db=db, bible_book_abbr=bible_book_abbr, zachalo=zachalo)
            number_creatures += 1
            print('(+)', number_creatures, "|", zachalo_tag.text, "|", zachalo.num, "|", bible_book_abbr)
        #
        # else:
        #     print("ERROR! not create", "|", zachalo_tag.text)

    if number_zachalos != number_creatures:
        raise ValueError(
            f'Не создались {number_zachalos} записи об зачалах в таблице `zachalos`.')
    return True
