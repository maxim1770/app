import logging

from sqlalchemy.orm import Session

from app import crud, create
from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == "__main__":
    db: Session = next(deps.get_db())
    for manuscript_code in [
        # UUID('50D07A48-B72E-4372-B020-AD5BAF59F797'),
        # 'f-37-170',
        # 'f-304i-364'

        # 'f-98-80',
        # 'f-113-431',
        # '0aa8e89f-0267-4d66-b5e9-399e4474e7b3',
        # 'f-113-629',
        # 'f-173i-57',
        # 'f-304i-682',
        # '75a3eb09-dbc0-4b0f-8689-bc9f8c8b01e0',
        # 'f-304i-692',
        # 'f-218-1132',  # sbornik-slov-i-zhitiy-a-sia-kniga-otecheskaa-prepodobnyh-otec-velikih-pustynnozhitel
        # 'f-178i-9500',  # elizavetgradskoe-evangelie-licevoe
        # 'f-256-472',
        # 'f-228-67',
        # 'f-173i-5',
        # 'f-98-30',

        # 'f-304i-87',
        # 'f-37-216',
        # 'f-173i-11',
        # '2eadd685-eb71-40c5-bdec-7e9dc9b7efce',
        # 'a05ec697-47ed-4ccf-bc2c-5b8025cc8127',
        # '44e98e44-f6a7-43bb-bd45-c56bc603e93d',

        # 'f-304i-206',
        # 'e40b1692-8a78-4543-8495-3aa0c4e1deee',  # kormchaya_bookmark_data.kormchaya_3
        # 'fbcc305d-7632-44bb-8264-d18e4df174ac',  # kormchaya_bookmark_data.kormchaya_4
        # 'ba4b7090-357d-49b9-9d7d-35ce714b6236',  # kormchaya_bookmark_data.kormchaya_pisec_sava_danilov

        # 'lls-book-rus-1'
        # 'lls-book-rus-2'
        # 'lls-book-1'
        # 'lls-book-2'
        # 'lls-book-3'
        'lls-book-4'
    ]:
        manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
        create.create_manuscript_bookmarks(db, manuscript=manuscript)
