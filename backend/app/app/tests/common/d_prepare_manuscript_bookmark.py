import logging

import boto3
from sqlalchemy.orm import Session

from app import crud, create, utils
from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == "__main__":
    db: Session = next(deps.get_db())
    boto_session: boto3.session.Session = next(deps.get_boto())
    object_storage = utils.ObjectStorage(boto_session)
    for manuscript_code in [
        # '50d07a48-b72e-4372-b020-ad5baf59f797',
        # 'f-304i-718',
        # '4a7fb0e6-5d48-4d05-8e93-7e6c3fc93c1d',

        # 'f-113-630',
        # 'f-218-1132',  # sbornik-slov-i-zhitiy-a-sia-kniga-otecheskaa-prepodobnyh-otec-velikih-pustynnozhitel
        # 'f-113-629',
        # 'f-304i-682',
        # 'f-304i-692',
        # 'f-173i-57',
        # 'f-304i-712',
        # 'f-304i-686',
        # 'f-304i-684',
        # 'f-113-641',
        # 'cc3883b7-f9f8-4cb1-aeeb-aa835c900a16',
        # '75a3eb09-dbc0-4b0f-8689-bc9f8c8b01e0',
        # 'f-37-170',
        # 'f-304i-364',
        # 'f-37-430',
        # 'f-304i-629',
        # 'f-304i-693',

        # '0aa8e89f-0267-4d66-b5e9-399e4474e7b3',
        # 'f-113-431',
        # 'f-98-80',

        # 'f-304i-206',
        # 'ba4b7090-357d-49b9-9d7d-35ce714b6236',  # kormchaya_bookmark_data.kormchaya_pisec_sava_danilov

        # 'f-37-216',
        # 'f-173i-11',
        # 'f-304i-87',
        # 'a05ec697-47ed-4ccf-bc2c-5b8025cc8127',
        # '44e98e44-f6a7-43bb-bd45-c56bc603e93d',
        # '2eadd685-eb71-40c5-bdec-7e9dc9b7efce',  # 'номера л. не совпадают'

        # --- сверху обработанные Рукописи

        # 'f-178i-9500',  # elizavetgradskoe-evangelie-licevoe
        # 'f-228-67',
        # 'f-256-472',
        # 'f-173i-5',
        # 'f-98-30',  # 'номера зачал не совпадают с изображениями', где то потеряна страница ( не совпадает img (643 всего л.) и pdf (638 всего л.)) (Апостола Павла 2-е послание к коринфянам - где-то тут ошибка возможно)

        # 'e40b1692-8a78-4543-8495-3aa0c4e1deee',  # kormchaya_bookmark_data.kormchaya_3
        # 'fbcc305d-7632-44bb-8264-d18e4df174ac',  # kormchaya_bookmark_data.kormchaya_4
    ]:
        manuscript = crud.manuscript.get_by_code(db, code=manuscript_code)
        create.create_manuscript_bookmarks(db, manuscript=manuscript, object_storage=object_storage)
