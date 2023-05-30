import requests
import sqlalchemy as sa
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import schemas, enums, models, crud
from app.create import prepare
from .icon import create_icon


def create_all_icons(db: Session, *, session: requests.Session) -> None:
    saints = db.execute(
        sa.select(models.Saint).join(models.SaintsHolidays).join(models.Holiday).join(models.HolidayCategory)
        .filter(
            (models.HolidayCategory.title == enums.HolidayCategoryTitle.den_pamjati)
        )).scalars().all()
    icons_data_in: list[schemas.IconDataCreate] = prepare.get_saints_icons_data_in(session, saints=saints)
    for icon_data_in in icons_data_in:
        create_icon(db, icon_data_in=icon_data_in)


def create_all_gallerix_icons(db: Session, *, driver: WebDriver) -> None:
    saints = [
        # ('prorok-i-krestitel-ioann-predtecha', ['3773225357']),
        ('ioann-zlatoust', ['2045741110']),
        ('vasilij-velikij', ['250132640']),
        # ('arhangel-gavriil', ['422052305']),
        # ('pavel-pervoverhovnyj-apostol', ['2308381763']),
        # ('petr-do-prizvanija-simon', ['4270861525']),
        ('kirill-belozerskij', ['291252173']),
        ('nikolaj-mirlikijskij', ['138876558', '1641114475', '32594595']),
        ('ioann-lestvichnik', ['1299596441']),
    ]
    holidays = [
        ('Св.Борис и Глеб', ['548195762', '265120442', '2675078954']),
        ('simeon-stolpnik-antiokhijskij', ['4050548477']),
    ]
    great_holidays = [
        ('svjatoe-preobrazhenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['3884653972', '689602973']),
        ('blagoveschenie-presvjatoj-vladychitsy-nashej-bogoroditsy-i-prisnodevy-marii', ['3242162079']),
        ('sretenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['4077458721', '633727841', '3817190861']),
        # ('Зачатие Пресвятой Богородицы', ['1880856712']),
        ('izhe-po-ploti-rozhdestvo-gospoda-boga-i-spasa-nashego-isusa-hrista', ['37212762']),
        ('rozhdestvo-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii', ['3948181352']),
        ('voznesenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['3636723403']),
        ('svetloe-hristovo-voskresenie-svjataja-pasha', ['1185377134', '3258948338']),
    ]
    _ = [
        ('presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija',
         ['1848586563', '3356043925', '3040389732', '2126516406', '1363546008', '791746187', '7433219', '320510357',
          '1470889248', '2652240293', '1549471566']
         ),
        ('gospod-bog-i-spas-nash-isus-hristos',
         ['2548164891', '1835892864', '891996828', '4108380166', '2888014627']
         ),
    ]
    verived_gallerix_icons_ids___ = [
        ('Чудо от иконы Божией Матери – Знамение в битве между новгородцами и суздальцами', ['2030579737']),
    ]
    for holiday_slug, gallerix_icons_ids in great_holidays:
        for gallerix_icon_id in map(int, gallerix_icons_ids):
            __create_gallerix_icon(db, driver=driver, holiday_slug=holiday_slug, gallerix_icon_id=gallerix_icon_id)
    for saint_slug, gallerix_icons_ids in saints:
        holiday_slug: str = f'den-pamjati-{saint_slug}'
        for gallerix_icon_id in map(int, gallerix_icons_ids):
            __create_gallerix_icon(db, driver=driver, holiday_slug=holiday_slug, gallerix_icon_id=gallerix_icon_id)


def create_all_shm_icons(db: Session, *, driver: WebDriver) -> None:
    saints = [
        # ('prorok-i-krestitel-ioann-predtecha', ['1652552', '1652553', '1652551', '1651326', '1654238', '1650426']),
        ('ioann-zlatoust', ['1652338', '1649169', '1652576', '1652981']),
        ('vasilij-velikij', ['1651328', '1652307', '1650950']),
        ('grigorij-bogoslov', ['1652413']),
        # ('arhangel-gavriil', ['1650950', '1654239', '1650423', '1651722', '1653424', '1654247', '1654253']),
        # ('arhangel-mihail-arhistratig', ['1654240', '1655597']),
        # ('pavel-pervoverhovnyj-apostol', ['1649139']),
        # ('petr-do-prizvanija-simon', ['1650421', '1654259']),
        ('kirill-belozerskij', ['1650121', '1655030', '1651131']),
        ('nikolaj-mirlikijskij',
         ['1655698', '1652998', '1652555', '1652555', '1652607', '1654311', '5521034', '5521035']),
        # ('ioann-lestvichnik', ['']),
        ('ioann-bogoslov', ['1654252', '1654246', '5521023', '5521024']),
        # ('sergij-radonezhskij', ['? 1652337']),
        ('ilija-fesvitjanin', ['1650004', '1655313', '1652755', '1654258']),
        # ('simeon-bogopriimec', ['1655327']),
        ('simon-zilot', ['1649915']),
        ('ieremija-prorok', ['1652137', '1650513']),
        ('isaija-prorok', ['1652413']),
        ('malahija', ['1651330']),
        # ('leontij-rostovskij', ['5535006', '1649778']),
        ('matfej-levij', ['1654244', '1654250', '1652089']),
        ('luka-evangelist', ['1654245', '1654251']),
        ('mark-evangelist', ['1654249', '1652089']),
        ('afanasij-velikij', ['1654021', '1649778']),
        ('antonij-velikij', ['1650490']),
        # ('? evfrosinija-polotskaja-do-kreshhenija-knjazhna-predislava', ['? 5534077', '? 5534076']),
        # ('petr-moskovskij', ['? 1652910']),
        ('feodor-tiron', ['1652616']),
    ]
    holidays = [
        ('Св.Борис и Глеб', ['1650005', '', '']),
        ('simeon-stolpnik-antiokhijskij', ['']),
        ('Петр и Павел', ['1650480', '1650463', '1655334', '5521020']),
        ('Собор вселенских святителей', ['1649878', '1655576']),
        ('Равноапостольные Константин и Елена', ['1655507', '1654612']),
        ('', ['']),
    ]
    great_holidays = [
        ('svjatoe-preobrazhenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['1654667', '1654527']),
        ('blagoveschenie-presvjatoj-vladychitsy-nashej-bogoroditsy-i-prisnodevy-marii',
         ['1650629', '1652345', '1652413', '1654531']),
        ('sretenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['1654530']),
        # ('Зачатие Пресвятой Богородицы', ['']),
        ('izhe-po-ploti-rozhdestvo-gospoda-boga-i-spasa-nashego-isusa-hrista', ['1650001', '1652829', '1652770']),
        ('rozhdestvo-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii',
         ['1650525', '1653673', '1651321', '1654533', '1652906']),
        ('voznesenie-gospoda-boga-i-spasa-nashego-isusa-hrista', ['5534932']),
        ('svetloe-hristovo-voskresenie-svjataja-pasha', ['1655088', '1655704', '1654530', '1655088']),
    ]
    _ = [
        ('presvjataja-vladychitsa-nasha-bogoroditsa-i-prisnodeva-marija',
         ['5692788', '5692789', '5534338', '5534275', '5534276', '5534281', '5534282',
          '5534283', '5534284', '5535002', '5534594', '5534595', '5535951', '1654225', '5535952', '1651991', '1652906',
          '1653147',
          '1654097', '1650489', '1652973']
         ),
        ('gospod-bog-i-spas-nash-isus-hristos',
         ['1651718', '5533848', '1655064', '5535414', '5535413', '1652890', '1650889', '1649718', '1653665', '1650437',
          '1652595',
          '1651831', '1652218', '1655072', '1655071', '1654970', '1655502'
          ]
         ),
    ]
    verived_gallerix_icons_ids___ = [
        ('Чудо от иконы Божией Матери – Знамение в битве между новгородцами и суздальцами', ['']),
    ]
    for holiday_slug, shm_icons_ids in great_holidays:
        for shm_icon_id in map(int, shm_icons_ids):
            __create_shm_icon(db, driver=driver, holiday_slug=holiday_slug, shm_icon_id=shm_icon_id)
    for saint_slug, shm_icons_ids in saints:
        holiday_slug: str = f'den-pamjati-{saint_slug}'
        for shm_icon_id in map(int, shm_icons_ids):
            __create_shm_icon(db, driver=driver, holiday_slug=holiday_slug, shm_icon_id=shm_icon_id)


def __create_gallerix_icon(db: Session, *, driver: WebDriver, holiday_slug: str, gallerix_icon_id: int) -> None:
    icon_data_in = prepare.get_gallerix_icon_data_in(driver, holiday_slug=holiday_slug,
                                                     gallerix_icon_id=gallerix_icon_id)
    create_icon(db, icon_data_in=icon_data_in)


def __create_shm_icon(db: Session, *, driver: WebDriver, holiday_slug: str, shm_icon_id: int) -> None:
    if not crud.icon.get_by_shm_id(db, shm_id=shm_icon_id):
        icon_data_in = prepare.get_shm_icon_data_in(driver, holiday_slug=holiday_slug, shm_icon_id=shm_icon_id)
        create_icon(db, icon_data_in=icon_data_in)
