import logging
from enum import IntEnum
from pathlib import Path

from PIL import Image, ImageFile
from requests import Session
from selenium.webdriver.chrome.webdriver import WebDriver

from app import enums, utils, const
from app.core.config import settings
from app.create import prepare

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

    def crop_watermarks_from_bottom(self):
        for i, img in enumerate(self._imgs):
            x_max, y_max = img.size
            self._imgs[i] = img.crop((0, 0, x_max, y_max - 62))

    def save_imgs(self) -> None:
        self._path.mkdir()
        for i, img in enumerate(self._imgs):
            current_path: Path = self._path / f'{i + 1}.webp'
            img.save(current_path, format='webp')
        logging.info(f'The Manuscript imgs saved: {self._path}')

    def create_pdf(self) -> None:
        self.create_pdf_from_imgs(self._pdf_path, imgs=self._imgs)
        logging.info(f'The Manuscript pdf created: {self._pdf_path}')

    @staticmethod
    def create_pdf_from_imgs(pdf_path: Path, *, imgs: list[Image], resolution: float = 99.0):  # 99.0 # 100.0
        imgs[0].save(
            pdf_path, 'PDF', resolution=resolution, save_all=True, append_images=imgs[1:]
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
        prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lib(
            fund_title=fund_title,
            library_title=library_title,
            code=code
        )
        path: Path = prepare_manuscript_path.path
        pdf_path: Path = prepare_manuscript_path.pdf_path
        imgs_urls: list[str] = prepare.CollectManuscriptImgsUrls(session, driver, code=code,
                                                                 neb_slug=neb_slug).imgs_urls
        collect_manuscript = CollectManuscript(session, imgs_urls=imgs_urls, path=path, pdf_path=pdf_path)
        return collect_manuscript


class CollectManuscriptLlsFactory(object):
    class RuniversLlsNumPages(IntEnum):
        lls_book_1 = 507
        lls_book_2 = 629
        lls_book_3 = 1063
        lls_book_5 = 927
        lls_book_6 = 880
        lls_book_7 = 1031
        lls_book_8 = 816
        lls_book_9 = 827
        lls_book_10 = 839

        # lls_book_rus_1 = 1023  # Русь Книга 1 (Тут получается Русь Книга 1-2)

        # - - -
        # https://runivers.ru/lib/book19785

        lls_book_rus_1 = 499
        lls_book_rus_2 = 539
        lls_book_rus_3 = 533
        lls_book_rus_4 = 545
        lls_book_rus_5 = 543
        lls_book_rus_6 = 490
        lls_book_rus_7 = 505
        lls_book_rus_8 = 489
        lls_book_rus_9 = 575
        lls_book_rus_10 = 509

        # - - -

        lls_book_rus_11 = 543  # Русь Книга 11
        lls_book_rus_12 = 485
        lls_book_rus_13 = 531
        lls_book_rus_14 = 523
        lls_book_rus_15 = 491
        lls_book_rus_16 = 531
        lls_book_rus_17 = 503
        lls_book_rus_18 = 510
        lls_book_rus_19 = 665
        lls_book_rus_20 = 519
        lls_book_rus_21 = 578
        lls_book_rus_22 = 552
        lls_book_rus_23 = 520  # Русь Книга 23

    @classmethod
    def get(
            cls,
            session: Session,
            *,
            code: str,
    ) -> CollectManuscript:
        prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lls(code=code)
        path: Path = prepare_manuscript_path.path
        pdf_path: Path = prepare_manuscript_path.pdf_path
        imgs_urls: list[str] = [
            f'{const.RuniversUrl.GET_MANUSCRIPT_PAGES}/{const.RuniversLlsId[code.replace("-", "_")]}/{cls._add_zeros_to_num(num + 1)}.gif'
            for num in range(cls.RuniversLlsNumPages[code.replace('-', '_')])
        ]
        collect_manuscript = CollectManuscript(session, imgs_urls=imgs_urls, path=path, pdf_path=pdf_path)
        return collect_manuscript

    @classmethod
    def _add_zeros_to_num(cls, num: int) -> str:
        return '0' * (4 - len(str(num))) + str(num)


def create_manuscript_pdf(
        *,
        fund_title: enums.FundTitle,
        library_title: enums.LibraryTitle,
        code: str,
) -> None:
    prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lib(
        fund_title=fund_title,
        library_title=library_title,
        code=code
    )
    created_path: Path = prepare_manuscript_path.created_path
    pdf_path: Path = prepare_manuscript_path.pdf_path
    imgs = [
        Image.open(created_path / f'{num + 1}.webp')
        for num in range(len(list(created_path.iterdir())))
    ]
    CollectManuscript.create_pdf_from_imgs(pdf_path, imgs=imgs)


def create_manuscript_pdf_from_lls(
        *,
        code: str,
        resolution: float = 99.0
) -> None:
    prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lls(code=code)
    created_path: Path = prepare_manuscript_path.created_path
    pdf_path: Path = prepare_manuscript_path.pdf_path
    imgs = [
        Image.open(created_path / f'{num + 1}.webp')
        for num in range(len(list(created_path.iterdir())))
    ]
    CollectManuscript.create_pdf_from_imgs(pdf_path, imgs=imgs, resolution=resolution)


def create_manuscript_data_dirs():
    path = Path(settings.DATA_DIR) / 'img' / 'manuscripts'
    for fund_title in enums.FundTitle:
        if utils.is_rsl_library(fund_title):
            library_title = enums.LibraryTitle.rsl
        else:
            library_title = enums.LibraryTitle.nlr
        current_path = path / library_title.name / fund_title.name
        current_path.mkdir(exist_ok=True)
