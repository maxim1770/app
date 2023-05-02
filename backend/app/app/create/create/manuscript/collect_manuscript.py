import logging
from pathlib import Path

from PIL import Image, ImageFile
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver

from app import enums, utils
from app.core.config import settings
from ....create import prepare

ImageFile.LOAD_TRUNCATED_IMAGES = True


class CollectManuscript(object):

    def __init__(self, session: Session, *, imgs_urls: list[str], path: Path, pdf_path: Path):
        self._imgs: list[Image] = self.collect_imgs(session, imgs_urls=imgs_urls)
        self._path = path
        self._pdf_path = pdf_path

    @staticmethod
    def collect_imgs(session: Session, *, imgs_urls: list[str]) -> list[Image]:
        imgs: list[Image] = []
        for img_url in imgs_urls:
            img = Image.open(session.get(img_url, stream=True).raw)
            imgs.append(img)
            logging.info(f'{len(imgs)} | {img_url}')
        return imgs

    def save_imgs(self) -> None:
        self._path.mkdir()
        for i, img in enumerate(self._imgs):
            current_path: Path = self._path / f'{i + 1}.webp'
            img.save(current_path, format='webp')
            logging.info(f'{i + 1} | {current_path}')
        logging.info(f'The Manuscript imgs {self._path} saved')

    def create_pdf(self) -> None:
        logging.info(f'The Manuscript pdf {self._pdf_path} creating...')
        self.create_pdf_from_imgs(self._pdf_path, imgs=self._imgs)
        logging.info(f'The Manuscript pdf {self._pdf_path} created')

    @staticmethod
    def create_pdf_from_imgs(pdf_path: Path, *, imgs: list[Image]):
        imgs[0].save(
            pdf_path, "PDF", resolution=99.0, save_all=True, append_images=imgs[1:]
        )


class CollectManuscriptFactory(object):

    @classmethod
    def get(
            cls,
            session: Session,
            driver: WebDriver,
            *,
            fund_title: enums.FundTitle,
            library_title: enums.LibraryTitle,
            code: str,
            neb_slug: str | None
    ) -> CollectManuscript:
        prepare_manuscript_path = utils.PrepareManuscriptPath(fund_title=fund_title, library_title=library_title,
                                                              code=code)
        path: Path = prepare_manuscript_path.path
        pdf_path: Path = prepare_manuscript_path.pdf_path
        imgs_urls: list[str] = prepare.СollectManuscriptImgsUrls(session, driver, code=code,
                                                                 neb_slug=neb_slug).imgs_urls
        collect_manuscript = CollectManuscript(session, imgs_urls=imgs_urls, path=path, pdf_path=pdf_path)
        return collect_manuscript


def create_manuscript_pdf(
        *,
        fund_title: enums.FundTitle,
        library_title: enums.LibraryTitle,
        code: str,
) -> None:
    prepare_manuscript_path = utils.PrepareManuscriptPath(fund_title=fund_title, library_title=library_title,
                                                          code=code)
    created_path: Path = prepare_manuscript_path.created_path
    pdf_path: Path = prepare_manuscript_path.pdf_path
    imgs = [
        Image.open(created_path / f'{num + 1}.webp')
        for num in range(len(list(created_path.iterdir())))
    ]
    CollectManuscript.create_pdf_from_imgs(pdf_path, imgs=imgs)


def create_manuscript_data_dirs():
    path = Path(settings.DATA_DIR) / 'img' / 'manuscripts'
    for fund_title in enums.FundTitle:
        if utils.is_rsl_library(fund_title):
            library_title = enums.LibraryTitle.rsl
        else:
            library_title = enums.LibraryTitle.nlr
        current_path = path / library_title.name / fund_title.name
        current_path.mkdir(exist_ok=True)
