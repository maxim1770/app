from pathlib import Path


def __swap_imgs_names(some_img_path: Path, *, img_1_num: int, img_2_num: int) -> None:
    """
    Функция не понадобилась, но вроде неплохая
    Меняет местами названия двух файлов
    # common_path = Path(...)
    # _swap_imgs_names(common_path, img_1_num=1012, img_2_num=1013)"""
    img_1_stem = str(img_1_num)
    img_2_stem = str(img_2_num)
    img_1_path: Path = some_img_path.with_stem(img_1_stem)
    img_2_path: Path = some_img_path.with_stem(img_2_stem)
    img_1_path = img_1_path.rename(img_1_path.with_stem('temp'))
    img_2_path = img_2_path.rename(img_2_path.with_stem(img_1_stem))
    img_1_path = img_1_path.rename(img_1_path.with_stem(img_2_stem))


def __fix_sort_lls_book_4_pages():
    # prepare_manuscript_path = utils.PrepareManuscriptPathFactory.from_lls(code='lls-book-4')
    # created_imgs_path: Path = prepare_manuscript_path.created_path
    created_imgs_path: Path = Path(r'C:\Users\MaxDroN\Desktop\lls-book-4')
    some_img_path: Path = created_imgs_path / 'img_num.webp'
    img_first_num_to_add: int = 89
    img_first_num: int = 521
    img_end_num: int = 609
    for i, img_num in enumerate(range(img_first_num, img_end_num + 1)):
        current_path = some_img_path.with_stem(str(img_num))
        current_path = current_path.rename(current_path.with_stem(str(i + img_first_num_to_add) + '_'))
    for img_num in range(img_first_num_to_add, img_first_num):
        current_path = some_img_path.with_stem(str(img_num))
        current_path = current_path.rename(current_path.with_stem(str(img_num + img_first_num_to_add + 1) + '_'))
    # for img_num in range(img_first_num_to_add, img_end_num + 1):
    #     current_path = some_img_path.with_stem(str(img_num) + '_')
    #     current_path = current_path.rename(current_path.with_stem(str(img_num)))


if __name__ == '__main__':
    # create_lls_book_3_4_imgs_and_pdfs()

    # new_location = shutil.move(source_path, destination_path)

    # created_imgs_path: Path = Path(r'C:\Users\MaxDroN\Desktop\lls-book-4')
    # some_img_path: Path = created_imgs_path / 'img_num.webp'
    #
    # img_first_num_to_add: int = 89
    # img_first_num: int = 521
    # img_end_num: int = 609
    # # for img_num in range(img_first_num_to_add, img_end_num + 1):
    # #     current_path = some_img_path.with_stem(str(img_num) + '_')
    # #     current_path = current_path.rename(current_path.with_stem(str(img_num)))
    #
    # for i in range(1, 1063):
    #     current_path = some_img_path.with_stem(str(i))
    #     current_path_ = some_img_path.with_stem(str(i) + '_')
    #     if current_path.exists() and current_path_.exists():
    #         raise Exception
    #     if current_path_.exists():
    #         print(current_path_)
    #         print(current_path)

    pass
