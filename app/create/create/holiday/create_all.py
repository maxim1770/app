import logging

from sqlalchemy.orm import Session

from app import crud
from app.enums import CycleNum, MovableDayAbbr
from app.enums import FaceSanctityTitle, HolidayCategoryTitle
from app.schemas import MovableSaintHolidayCreate, MovableSaintHolidayCreateWithoutData, MovableDayGet
from app.schemas import SaintDataCreate, SaintCreate, HolidayCreate, YearCreate, HolidayDataCreate
from app.schemas import SaintHolidayCreate, DayCreate
from app.schemas import SaintsHolidayCreate
from .holiday import create_holiday, create_saint_holiday, create_saints_holiday, create_movable_saint_holiday
from ..saint import create_saint
from ....create import const, prepare


def create_all_saints_holidays(db: Session):
    for day in const.all_days_in_year():
        logging.info(day)
        saints_holidays_in = prepare.saints_holidays_in_factory(day)
        for saint_holiday_in in saints_holidays_in:
            holiday = crud.holiday.get_by_slug(db, slug=saint_holiday_in.holiday_in.slug)
            if holiday:
                logging.warning(f'The Holiday with this slug already exists, {saint_holiday_in.holiday_in.slug}')
                continue
            holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)


def create_all_great_holidays(db: Session):
    great_holidays: list[tuple[SaintDataCreate, list[SaintHolidayCreate | MovableSaintHolidayCreate]]] = [
        (
            SaintDataCreate(
                saint_in=SaintCreate(
                    slug='gospod-bog-i-spas-nash-isus-hristos',
                    name='Господь Бог и Спас наш Исус Христос'
                )
            ), [
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='izhe-po-ploti-rozhdestvo-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Иже по плоти Рождество Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='5500 от Адама'),
                    day_in=DayCreate(month=12, day=25),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='izhe-po-ploti-obrezanie-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Иже по Плоти Обре́зание Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='5500 от Адама'),
                    day_in=DayCreate(month=1, day=1),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='svjatoe-bogojavlenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Святое Богоявление Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='30'),
                    day_in=DayCreate(month=1, day=6),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='sretenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Сретение Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='5500 от Адама'),
                    day_in=DayCreate(month=2, day=2),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='blagoveschenie-presvjatoj-vladychitsy-nashej-bogoroditsy-i-prisnodevy-marii',
                        title='Благовещение Пресвятой Владычицы нашей Богородицы и Приснодевы Марии',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='5499 от Адама'),
                    day_in=DayCreate(month=3, day=25),
                ),
                MovableSaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='vhod-gospoden-v-ierusalim',
                        title='Вход Господень в Иерусалим',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='33'),
                    movable_day_get=MovableDayGet(
                        cycle_num=CycleNum.cycle_3,
                        sunday_num=6,
                        abbr=MovableDayAbbr.sun
                    )
                ),
                MovableSaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='svetloe-hristovo-voskresenie-svjataja-pasha',
                        title='СВЕТЛОЕ ХРИСТОВО ВОСКРЕСЕНИЕ. СВЯТАЯ ПАСХА',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='33'),
                    movable_day_get=MovableDayGet(
                        cycle_num=CycleNum.cycle_1,
                        sunday_num=1,
                        abbr=MovableDayAbbr.sun
                    )
                ),
                MovableSaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='voznesenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Вознесение Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='33'),
                    movable_day_get=MovableDayGet(
                        cycle_num=CycleNum.cycle_1,
                        sunday_num=6,
                        abbr=MovableDayAbbr.thu
                    )
                ),
                MovableSaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='svjataja-pjatidesjatnitsa',
                        title='СВЯТАЯ ПЯТИДЕСЯТНИЦА',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='33'),
                    movable_day_get=MovableDayGet(
                        cycle_num=CycleNum.cycle_1,
                        sunday_num=8,
                        abbr=MovableDayAbbr.sun
                    )
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='svjatoe-preobrazhenie-gospoda-boga-i-spasa-nashego-isusa-hrista',
                        title='Святое Преображение Господа Бога и Спаса нашего Исуса Христа',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_hristovy,
                    saint_in=SaintCreate(slug='gospod-bog-i-spas-nash-isus-hristos'),
                    year_in=YearCreate(title='33'),
                    day_in=DayCreate(month=8, day=6),
                ),
            ]
        ),
        (
            SaintDataCreate(
                saint_in=SaintCreate(
                    slug='presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija',
                    name='Пресвятая Владычица наша Богородица и Приснодева Мария'
                )
            ), [
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='rozhdestvo-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii',
                        title='Рождество Пресвятой Владычицы нашей Богородицы и Приснодевы Марии',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_bogorodichny,
                    saint_in=SaintCreate(slug='presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija'),
                    year_in=YearCreate(title='5485 от Адама'),
                    day_in=DayCreate(month=9, day=8),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='vvedenie-v-tserkov-presvjatuju-vladychitsu-nashu-bogoroditsu',
                        title='Введение в Церковь Пресвятую Владычицу нашу Богородицу',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_bogorodichny,
                    saint_in=SaintCreate(slug='presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija'),
                    year_in=YearCreate(title='5492 от Адама'),
                    day_in=DayCreate(month=11, day=21),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='uspenie-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii',
                        title='Успение Пресвятой Владычицы нашей Богородицы и Приснодевы Марии',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_bogorodichny,
                    saint_in=SaintCreate(slug='presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija'),
                    year_in=YearCreate(title='57'),
                    day_in=DayCreate(month=8, day=15),
                )
            ]
        ),
        (
            SaintDataCreate(
                saint_in=SaintCreate(
                    slug='prorok-i-krestitel-ioann-predtecha',
                    name='Пророк, Предтеча и Креститель Господень Иоа́нн'
                ),
                face_sanctity_title=FaceSanctityTitle.prorok
            ), [
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='rozhdestvo-chestnogo-slavnogo-proroka-predtechi-i-krestitelja-gospodnja-ioanna',
                        title='Рождество честно́го славного Пророка, Предтечи и Крестителя Господня Иоанна',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_predtechevy,
                    saint_in=SaintCreate(slug='prorok-i-krestitel-ioann-predtecha'),
                    year_in=YearCreate(title='5499 от Адама'),
                    day_in=DayCreate(month=6, day=24),
                ),
                SaintHolidayCreate(
                    holiday_in=HolidayCreate(
                        slug='useknovenie-glavy-proroka-predtechi-i-krestitelja-gospodnja-ioanna',
                        title='Усекновение главы Пророка, Предтечи и Крестителя Господня Иоанна',
                    ),
                    holiday_category_title=HolidayCategoryTitle.prazdniki_predtechevy,
                    saint_in=SaintCreate(slug='prorok-i-krestitel-ioann-predtecha'),
                    year_in=YearCreate(title='30'),
                    day_in=DayCreate(month=8, day=29),
                )
            ]
        )
    ]
    for saint_data_in, saints_holidays_in in great_holidays:
        saint = create_saint(db, saint_data_in=saint_data_in)
        for saint_holiday_in in saints_holidays_in:
            if isinstance(saint_holiday_in, SaintHolidayCreate):
                holiday = create_saint_holiday(db, saint_holiday_in=saint_holiday_in)
            else:
                holiday = create_movable_saint_holiday(db, movable_saint_holiday_in=saint_holiday_in)

    saints_holiday_in = SaintsHolidayCreate(
        holiday_in=HolidayCreate(
            slug='slavnyh-i-vsehvalnyh-pervoverhovnyh-apostolov-petra-i-pavla',
            title='Славных и Всехвальных Первоверховных Апостолов Петра и Павла',
        ),
        # ТУТ НЕ УВЕРЕН, ВОЗМОЖНО СТОИТ ДОБАВИТЬ НОВУЮ КАТЕГОРИЮ ПРАЗДНИКИ СВЯТЫМ ВЕРХОВНЫМ АПОСТОЛАМ
        holiday_category_title=HolidayCategoryTitle.den_pamjati,
        saints_in=[
            SaintCreate(slug='petr-do-prizvanija-simon'),
            SaintCreate(slug='pavel-pervoverhovnyj-apostol'),
        ],
        year_in=YearCreate(title='65'),  # Вроде как правильно, источник: л.56 ЛЛС Том 2
        day_in=DayCreate(month=6, day=29),
    )
    holiday = create_saints_holiday(db, saints_holiday_in=saints_holiday_in)


def create_all_movable_saints_holidays(db: Session):
    movable_saints_holidays: list[MovableSaintHolidayCreateWithoutData | MovableSaintHolidayCreate] = [
        MovableSaintHolidayCreateWithoutData(
            movable_day_get=MovableDayGet(
                cycle_num=CycleNum.cycle_3,
                sunday_num=1,
                abbr=MovableDayAbbr.sat
            ),
            saint_slug='feodor-tiron'
        ),
        MovableSaintHolidayCreateWithoutData(
            movable_day_get=MovableDayGet(
                cycle_num=CycleNum.cycle_3,
                sunday_num=4,
                abbr=MovableDayAbbr.sun
            ),
            saint_slug='ioann-lestvichnik'
        ),
        MovableSaintHolidayCreateWithoutData(
            movable_day_get=MovableDayGet(
                cycle_num=CycleNum.cycle_3,
                sunday_num=5,
                abbr=MovableDayAbbr.sun
            ),
            saint_slug='marija-egipetskaja'
        ),
        MovableSaintHolidayCreate(
            holiday_in=HolidayCreate(
                slug='movable-den-pamjati-lazar-chetverodnevnyj',
                title='Воскрешение прав. Ла́заря',
            ),
            holiday_category_title=HolidayCategoryTitle.den_pamjati,
            saint_in=SaintCreate(slug='lazar-chetverodnevnyj'),
            year_in=YearCreate(title='33'),
            movable_day_get=MovableDayGet(
                cycle_num=CycleNum.cycle_3,
                sunday_num=6,
                abbr=MovableDayAbbr.sat
            )
        ),
    ]
    for movable_saint_holiday in movable_saints_holidays:
        if isinstance(movable_saint_holiday, MovableSaintHolidayCreateWithoutData):
            holiday_slug = HolidayCategoryTitle.den_pamjati.name.replace('_',
                                                                         '-') + '-' + movable_saint_holiday.saint_slug
            holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
            movable_holiday_slug = 'movable-' + holiday_slug
            movable_saint_holiday_in = MovableSaintHolidayCreate(
                holiday_in=HolidayCreate(title=holiday.title, slug=movable_holiday_slug),
                holiday_category_title=holiday.holiday_category.title,
                saint_in=SaintCreate(slug=movable_saint_holiday.saint_slug),
                year_in=YearCreate(title=holiday.year.title),
                movable_day_get=movable_saint_holiday.movable_day_get
            )
        else:
            movable_saint_holiday_in = movable_saint_holiday
        create_movable_saint_holiday(db, movable_saint_holiday_in=movable_saint_holiday_in)


def create_all_cathedrals_saints(db: Session):
    cathedrals_saints: list[SaintsHolidayCreate] = [
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-presvjatoj-bogoroditsy',
                title='Собор Пресвятой Богородицы',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            day_in=DayCreate(month=12, day=26),
            saints_in=[
                SaintCreate(slug='presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija')
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-svjatyh-i-vsehvalnyh-12-ti-apostolov',
                title='Собор Святых и Всехвальных 12-ти Апостолов',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            year_in=YearCreate(title='IV'),
            day_in=DayCreate(month=6, day=30),
            saints_in=[
                SaintCreate(slug='andrej-pervozvannyj'),
                SaintCreate(slug='petr-do-prizvanija-simon'),
                SaintCreate(slug='ioann-bogoslov'),
                SaintCreate(slug='iakov-zevedeev'),
                SaintCreate(slug='filipp-apostol'),
                SaintCreate(slug='varfolomej-nafanail'),
                SaintCreate(slug='matfej-levij'),
                SaintCreate(slug='iakov-alfeev'),
                SaintCreate(slug='iuda-iakovlev-levvej'),
                SaintCreate(slug='foma-didim-bliznec'),
                SaintCreate(slug='simon-zilot'),
                SaintCreate(slug='matfij'),
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-70-ti-apostolov',
                title='Собор 70-ти Апостолов',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            day_in=DayCreate(month=1, day=4),
            saints_in=[
                SaintCreate(slug='filimon-gazskij'), SaintCreate(slug='kriskent-galatijskij'),
                SaintCreate(slug='stefan-pervomuchenik'), SaintCreate(slug='tihik-kolofonskij'),
                SaintCreate(slug='kifa-ikonijskij-kolofonskij'), SaintCreate(slug='krisp-jeginskij'),
                SaintCreate(slug='lin'), SaintCreate(slug='siluan-solunskij-fessalonikijskij'),
                SaintCreate(slug='andronik-pannonijskij'), SaintCreate(slug='gaij-efesskij'),
                SaintCreate(slug='mark-evangelist'), SaintCreate(slug='trofim'),
                SaintCreate(slug='kliment'), SaintCreate(slug='sila-korinfskij'),
                SaintCreate(slug='iason-tarsijskij-kerkirskij'),
                SaintCreate(slug='flegont-marafonskij'), SaintCreate(slug='aristarh-apamejskij'),
                SaintCreate(slug='luka-evangelist'), SaintCreate(slug='ananija-damasskij'),
                SaintCreate(slug='sosfen-kolofonskij'),
                SaintCreate(slug='faddej-edesskij-bejrutskij'), SaintCreate(slug='filipp'),
                SaintCreate(slug='prohor-nikomidijskij'), SaintCreate(slug='timofej'),
                SaintCreate(slug='tit-apostol'), SaintCreate(slug='epenet-karfagenskij'),
                SaintCreate(slug='kesar-dirrahijskij'), SaintCreate(slug='pud'),
                SaintCreate(slug='ruf-fivskij'), SaintCreate(slug='erm-ermij-dalmatskij'),
                SaintCreate(slug='artema'), SaintCreate(slug='epafrodit-adriakskij'),
                SaintCreate(slug='patrov-neapolitanskij-i-puteolskij'),
                SaintCreate(slug='urvan-makedonskij'), SaintCreate(slug='erm-erma'),
                SaintCreate(slug='apollos-apellij-aleksandriec'), SaintCreate(slug='parmen'),
                SaintCreate(slug='arhipp-kolosskij'), SaintCreate(slug='dionisij-areopagit'),
                SaintCreate(slug='kuart-kvart'), SaintCreate(slug='lukij-luka'),
                SaintCreate(slug='varnava-iosia-mediolanskij-kiprskij'),
                SaintCreate(slug='olimp-olimpan'), SaintCreate(slug='timon-bostrijskij'),
                SaintCreate(slug='sosipatr-ikonijskij-kerkirskij'),
                SaintCreate(slug='alfej-kapernaumskij'), SaintCreate(slug='onisifor-kolofonskij'),
                SaintCreate(slug='asinkrit-girkanskij'), SaintCreate(slug='fortunat'),
                SaintCreate(slug='varsava-iust'), SaintCreate(slug='tertij-terentij'),
                SaintCreate(slug='karp-berijskij-makedonskij'),
                SaintCreate(slug='filolog-sinopskij'), SaintCreate(slug='simeon-niger'),
                SaintCreate(slug='stahij-vizantijskij'),
                SaintCreate(slug='epafras-kolosskij-i-ierapolskij'),
                SaintCreate(slug='iakov-brat-gospoden-po-ploti'), SaintCreate(slug='ahaik'),
                SaintCreate(slug='aristovul-vritanijskij-britanskij'),
                SaintCreate(slug='zina-zakonnik'), SaintCreate(slug='amplij-diospolskij'),
                SaintCreate(slug='nikanor'), SaintCreate(slug='evod-antiohijskij'),
                SaintCreate(slug='simeon-ierusalimskij'), SaintCreate(slug='narkiss-afinskij'),
                SaintCreate(slug='kliment-rimskij'), SaintCreate(slug='erast-paneadskij'),
                SaintCreate(slug='apellij-apelles'), SaintCreate(slug='onisim'),
                SaintCreate(slug='rodion-irodion-patrasskij'), SaintCreate(slug='kleopa'),
                SaintCreate(slug='kodrat-afinskij'), SaintCreate(slug='akila-geraklejskij'),
                SaintCreate(slug='agav'), SaintCreate(slug='mark-ioann-vivlejskij'),
                SaintCreate(slug='mark-apolloniadskij')
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='svjatyh-treh-svjatitelej-vasilija-velikogo-grigorija-bogoslova-i-ioanna-zlatoustogo',
                title='Поем службу Святых трех Святителей Васи́лия Великого, Григо́рия Богослова и Иоа́нна Златоустого, сотворенную от Святейшего Митрополита Евхаитскаго Кир Иоанн',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            year_in=YearCreate(title='после 1089'),  # НЕТОЧНО, ДАТУ ВЗЯЛ с azbyka
            day_in=DayCreate(month=1, day=30),
            saints_in=[
                SaintCreate(slug='vasilij-velikij'),
                SaintCreate(slug='grigorij-bogoslov'),
                SaintCreate(slug='ioann-zlatoust')
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-arhangela-gavriila',
                title='Собор Архангела Гаврии́ла',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            day_in=DayCreate(month=3, day=26),
            saints_in=[
                SaintCreate(
                    name='Архангел Гаврии́л',
                    slug='arhangel-gavriil'
                ),
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-arhangela-gavriila-drugoj',
                title='Собор Архангела Гаврии́ла',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            day_in=DayCreate(month=7, day=13),
            saints_in=[
                SaintCreate(
                    slug='arhangel-gavriil'
                ),
            ]
        ),
        SaintsHolidayCreate(
            holiday_in=HolidayCreate(
                slug='sobor-arhistratiga-mihaila-i-prochih-besplotnyh',
                title='Собор Архистратига Михаила и прочих бесплотных',
            ),
            holiday_category_title=HolidayCategoryTitle.cathedral_saints,
            day_in=DayCreate(month=11, day=8),
            year_in=YearCreate(title='IV'),  # НЕТОЧНО, ДАТУ ВЗЯЛ с azbyka
            saints_in=[
                SaintCreate(
                    name='Архангел Михаил, Архистратиг',
                    slug='arhangel-mihail-arhistratig'
                ),
                SaintCreate(
                    slug='arhangel-gavriil'
                )
            ]
        ),
    ]
    for saints_holiday_in in cathedrals_saints:
        holiday = create_saints_holiday(db, saints_holiday_in=saints_holiday_in)


def create_any_holidays(db: Session):
    holidays_data_in: list[HolidayDataCreate | SaintHolidayCreate] = [
        HolidayDataCreate(
            holiday_in=HolidayCreate(
                slug='svjatyh-mladentsev-ische-hrista-radi-izbiennyh-ot-iroda-v-vifleeme-14-tysjach',
                title='Святых младенцев ище Христа ради избиенных от Ирода в Вифлееме 14 тысяч',
            ),
            holiday_category_title=HolidayCategoryTitle.den_pamjati,
            year_in=YearCreate(title='5500 от Адама'),
            day_in=DayCreate(month=12, day=29),
        ),
        SaintHolidayCreate(
            holiday_in=HolidayCreate(
                slug='vospominanie-byvshego-chuda-v-honeh-kolossah-ot-arhistratiga-mihaila',
                title='Воспоминание бывшего чуда в Хо́нех (Коло́ссах) от Архистратига Михаила',
            ),
            holiday_category_title=HolidayCategoryTitle.den_pamjati,
            saint_in=SaintCreate(
                name='Архангел Михаил, Архистратиг',
                slug='arhangel-mihail-arhistratig'
            ),
            day_in=DayCreate(month=9, day=6),
            year_in=YearCreate(title='IV'),  # НЕТОЧНО, ДАТУ ВЗЯЛ с azbyka
        )
    ]
    for holiday_data_in in holidays_data_in:
        if isinstance(holiday_data_in, SaintHolidayCreate):
            holiday = create_saint_holiday(db, saint_holiday_in=holiday_data_in)
        else:
            holiday = create_holiday(db, holiday_data_in=holiday_data_in)
