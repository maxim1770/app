from sqlalchemy.orm import Session

from app import crud, enums
from app.schemas import CathedralCreate, CathedralDataCreate, YearCreate
from ..base_cls import FatalCreateError


def create_all_cathedrals(db: Session) -> None:
    if crud.cathedral.get_all(db):
        raise FatalCreateError(f'Cathedral: cathedrals already created')
    cathedrals_data_in: list[CathedralDataCreate] = [
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pravila_svjatyh_apostolov,
                title='Правила святых Апостолов', num_rules=85
            ),
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.svjatogo_apostola_pavla_osobno_pravil,
                title='Святого Апостола Павла особно правил', num_rules=17
            ),
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.togo_zh_pravila_o_usopshih_i_vlasteleh,
                title='Того ж правила о усопших и властелех', num_rules=2
            ),
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_1_nikejskij,
                title='Первый Вселенский Собор - Никейский', num_rules=20, num_saints=318
            ),
            year_in=YearCreate(title='333')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_ankirskij,
                title='Поместный Собор - Анкирский', num_rules=25
            ),
            year_in=YearCreate(title='322')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_neokesarijskij,
                title='Поместный Собор - Неокесарийский', num_rules=14
            ),
            year_in=YearCreate(title='323-327')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_gangrskij,
                title='Поместный Собор - Гангрский', num_rules=19
            ),
            year_in=YearCreate(title='348')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_antiohijskij,
                title='Поместный Собор - Антиохийский', num_rules=25
            ),
            year_in=YearCreate(title='349')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_laodikijskij,
                title='Поместный Собор - Лаодикийский', num_rules=58
            ),
            year_in=YearCreate(title='Около 368')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_2_konstantinopolskij,
                title='Второй Вселенский Собор - Константинопольский', num_rules=8,
                num_saints=152
            ),
            year_in=YearCreate(title='389')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_3_efesskij,
                title='Третий Вселенский Собор - Эфесский', num_rules=8, num_saints=300
            ),
            year_in=YearCreate(title='439')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_4_halkidonskij,
                title='Четвертый Вселенский Собор - Халкидонский', num_rules=30,
                num_saints=630
            ),
            year_in=YearCreate(title='459')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_sardikijskij,
                title='Поместный Собор - Сардикийский', num_rules=21
            ),
            year_in=YearCreate(title='355')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_karfagenskij,
                title='Поместный Собор - Карфагенский', num_rules=134
            ),
            year_in=YearCreate(title='427')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_6_konstantinopolskij_trulskij,
                title='Шестой Вселенский Собор - Константинопольский, Трульский',
                num_rules=102, num_saints=215
            ),
            year_in=YearCreate(title='688')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.vselenskij_sobor_7_nikejskij,
                title='Седьмой Вселенский Собор - Никейский', num_rules=22, num_saints=368
            ),
            year_in=YearCreate(title='795')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_konstantinopolskij_dvukratnyj,
                title='Поместный Собор - Константинопольский (двукратный)', num_rules=16
            ),
            year_in=YearCreate(title='869')
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pomestnyj_sobor_konstantinopolskij,
                title='Поместный Собор - Константинопольский', num_rules=3
            )
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.pravila_svjatogo_vasilija_velikogo_ot_poslanij,
                title='Правила святого Василия Великого от посланий к епископу Амфилохию Иконийскому, Диодору Тарскому, и к другим неким послания',
                num_rules=91
            )),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.svjatago_vasilja_o_vremeni_sogreshajuschih_vkrattse,
                title='Святаго Василя о времени согрешающих вкратце', num_rules=26
            )
        ),
        CathedralDataCreate(
            cathedral_in=CathedralCreate(
                slug=enums.СathedralSlug.iustinijana_razlichnyja_zapovedi,
                title='От книг Божественных повелении, Божественыя кончины, Иустинияна, различныя заповеди',
                num_rules=87
            )
        )
    ]
    for cathedral_data_in in cathedrals_data_in:
        year_id: int | None = crud.year.get_or_create(
            db,
            year_in=cathedral_data_in.year_in
        ).id if cathedral_data_in.year_in else None
        crud.cathedral.create_with_any(db, obj_in=cathedral_data_in.cathedral_in, year_id=year_id)
