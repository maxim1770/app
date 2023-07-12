import logging
from pathlib import Path

import requests

from app import create, utils
from app.create.create.manuscript.collect_manuscript import create_manuscript_pdf_from_lls

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def collect(manuscript_code: str):
    session = requests.Session()
    try:
        collect_manuscript = create.CollectManuscriptLlsFactory.get(
            session,
            code=manuscript_code,
        )
    except (FileNotFoundError, FileExistsError) as e:
        raise e
    collect_manuscript.crop_watermarks_from_bottom()
    collect_manuscript.save_imgs()
    # collect_manuscript.create_pdf()


def create_pdf(manuscript_code: str):
    try:
        create_manuscript_pdf_from_lls(code=manuscript_code, resolution=99.0)
    except (FileNotFoundError, FileExistsError) as e:
        raise e


def __fix_sort_lls_book_3_pages():
    prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lls(code='lls-book-3')
    created_imgs_path: Path = prepare_manuscript_path.created_path
    some_img_path: Path = created_imgs_path / 'img_num.webp'
    img_num_89: int = 89
    img_num_899: int = 899
    img_num_988: int = 988
    for i, img_num in enumerate(range(img_num_899, img_num_988 + 1)):
        current_path = some_img_path.with_stem(str(img_num))
        current_path.rename(current_path.with_stem(str(i + img_num_89) + '_'))
    for img_num in range(img_num_89, img_num_899):
        current_path = some_img_path.with_stem(str(img_num))
        current_path.rename(current_path.with_stem(str(img_num + img_num_89 + 1) + '_'))
    for img_num in range(img_num_89, img_num_988 + 1):
        current_path = some_img_path.with_stem(str(img_num) + '_')
        current_path.rename(current_path.with_stem(str(img_num)))


def __move_imgs_from_lls_book_3_to_lls_book_4():
    lls_book_3_created_imgs_path: Path = utils.PrepareManuscriptPathFactory.from_lls(code='lls-book-3').created_path
    lls_book_3_some_img_path: Path = lls_book_3_created_imgs_path / 'img_num.webp'
    lls_book_4_imgs_path: Path = utils.PrepareManuscriptPathFactory.from_lls(code='lls-book-4').path
    lls_book_4_some_img_path: Path = lls_book_4_imgs_path / 'img_num.webp'
    lls_book_4_imgs_path.mkdir()
    lls_book_4_first_page: int = 457
    for lls_book_4_img_num, img_num in enumerate(
            range(lls_book_4_first_page, create.CollectManuscriptLlsFactory.RuniversLlsNumPages.lls_book_3 + 1)):
        lls_book_3_current_img_path = lls_book_3_some_img_path.with_stem(str(img_num))
        lls_book_4_current_img_path = lls_book_4_some_img_path.with_stem(str(img_num))
        lls_book_3_current_img_path.rename(lls_book_4_current_img_path.with_stem(str(lls_book_4_img_num + 1)))


def create_lls_book_3_4_imgs_and_pdfs():
    collect('lls-book-3')
    __fix_sort_lls_book_3_pages()
    __move_imgs_from_lls_book_3_to_lls_book_4()
    for manuscript_code in ['lls-book-3', 'lls-book-4']:
        create_pdf(manuscript_code)


if __name__ == '__main__':
    # db = next(deps.get_db())
    # create.create_all_manuscripts_lls(db)
    for manuscript_code in []:
        create_pdf(manuscript_code)
