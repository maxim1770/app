import logging
from pathlib import Path

import requests

from app import create, utils, enums
from app.api.deps import get_driver, get_session
from app.create.create.manuscript.collect_manuscript import create_manuscript_pdf_from_lls

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def collect():
    session = next(get_session())
    driver = next(get_driver())
    try:
        # collect_manuscript = create.CollectManuscriptFactory.get(
        #     session,
        #     driver,
        #     fund_title=enums.FundTitle.sol,
        #     library_title=enums.LibraryTitle.nlr,
        #     code='A05EC697-47ED-4CCF-BC2C-5B8025CC8127',
        #     neb_slug='psaltyr-tolkovaya-s-pribavleniyami'
        # )
        collect_manuscript = create.CollectManuscriptFactory.get(
            session,
            driver,
            fund_title=enums.FundTitle.f_304i,
            library_title=enums.LibraryTitle.rsl,
            code='f-304i-87',
            neb_slug=None
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise ValueError('fsfsdf')
    collect_manuscript.save_imgs()
    collect_manuscript.create_pdf()


if __name__ == '__main__':
    collect()
