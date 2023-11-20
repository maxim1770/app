import logging

from sqlalchemy.orm import Session

from app.api import deps
from PIL import Image
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == "__main__":
    db: Session = next(deps.get_db())
    im = Image.open(r"C:\Users\MaxDroN\Desktop\RAIN.jpg")

    # уменьшаем изображение на 50%
    width, height = im.size
    new_size = (int(width / 2), int(height / 2))
    im_resized = im.resize(new_size)

    # сохраняем уменьшенное изображение
    im_resized.save(r"C:\Users\MaxDroN\Desktop\RAIN-preview.jpg")

    # create_all_movable_dates(db)
    # create_all_zachalos_movable_dates_associations(db)

    # for bookmark_, slug in zip(f_304i_206.bookmark_pages.pages_list[:-1], enums.СathedralSlug):
    #     print(f'(СathedralSlug.{slug.value}, { bookmark_.page + 2}),')

    # manuscript: models.Manuscript = crud.manuscript.get_by_code(db, code='ba4b7090-357d-49b9-9d7d-35ce714b6236')
    # bookmark_pages_turnover = kormchaya_pisec_sava_danilov.bookmark_pages_turnover
    # not_numbered_pages = schemas.NotNumberedPages.model_validate(manuscript.not_numbered_pages)
    # for i, bookmark_ in enumerate(bookmark_pages_turnover.pages_list[:-1]):
    #     page_in = schemas.PagesCreate(
    #         first_page=schemas.PageCreate(
    #             num=bookmark_.page,
    #             position=bookmark_.turnover + 1,
    #         ),
    #         end_page=schemas.PageCreate(
    #             num=bookmark_pages_turnover.pages_list[i + 1].page,
    #             position=bookmark_pages_turnover.pages_list[i + 1].turnover + 1,
    #         )
    #     )
    #     pages_nums = pages_in2pages_nums(
    #         first_page=page_in.first_page,
    #         end_page=page_in.end_page,
    #         not_numbered_pages=not_numbered_pages,
    #         has_left_and_right=True if manuscript.neb_slug else False,
    #         first_page_position=manuscript.first_page_position
    #     )
    #     print(f'(СathedralSlug.{list(enums.СathedralSlug)[i].value}, {pages_nums[0] - 1}),')
