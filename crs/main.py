from pathlib import Path

from pypdf2_bookmark_plus_title import add_bookmarks
from pages_turnover_models import get_pages_models


from books.neb.from_nlr.kormchaya_pisec_sava_danilov.bookmark_pages import bookmark_pages_turnover as bpt_kormchaya_pisec_sava_danilov

from books.neb.from_nlr.kormchaya_3.bookmark_pages import bookmark_pages_turnover as bpt_kormchaya_3
from books.neb.from_nlr.kormchaya_4.bookmark_pages import bookmark_pages_turnover as bpt_kormchaya_4

def main():


    # add_bookmarks(get_pages_models(bpt_kormchaya_pisec_sava_danilov))

    # add_bookmarks(get_pages_models(bpt_kormchaya_3))
    #
    # add_bookmarks(get_pages_models(bpt_kormchaya_4))

    pass





if __name__ == '__main__':
    main()