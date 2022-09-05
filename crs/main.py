from pathlib import Path

from pypdf2_bookmark_plus_title import add_bookmarks
from pages_turnover_models import get_pages_models


from books.neb.from_nlr.kormchaya_pisec_sava_danilov.bookmark_pages import bookmark_pages_turnover

def main():

    add_bookmarks(get_pages_models(bookmark_pages_turnover))


if __name__ == '__main__':
    main()