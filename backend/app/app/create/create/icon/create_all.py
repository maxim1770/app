import requests
import sqlalchemy as sa
from selenium.webdriver.chrome.webdriver import WebDriver
from sqlalchemy.orm import Session

from app import schemas, enums, models, crud
from app.create import prepare
from .icon import create_icon


def create_all_icons(db: Session, *, session: requests.Session, driver: WebDriver) -> None:
    _create_all_pravicon_icons(db, session=session)
    _create_other_pravicon_icons(db, session=session)
    _create_all_gallerix_icons(db, driver=driver)
    _create_all_shm_icons(db, driver=driver)


def _create_all_pravicon_icons(db: Session, *, session: requests.Session) -> None:
    saints = db.execute(
        sa.select(models.Saint).join(models.SaintHolidayAssociation).join(models.Holiday).join(models.HolidayCategory)
        .filter(
            (models.HolidayCategory.title == enums.HolidayCategoryTitle.den_pamjati)
        )).scalars().all()
    icons_data_in: list[schemas.IconDataCreate] = prepare.get_saints_icons_data_in(session, saints=saints)
    for icon_data_in in icons_data_in:
        create_icon(db, icon_data_in=icon_data_in)


def _create_other_pravicon_icons(db: Session, *, session: requests.Session) -> None:
    great_holidays = [
        ('izhe-po-ploti-rozhdestvo-gospoda-boga-i-spasa-nashego-isusa-hrista', 417),
        ('izhe-po-ploti-obrezanie-gospoda-boga-i-spasa-nashego-isusa-hrista', 462),
        ('svjatoe-bogojavlenie-gospoda-boga-i-spasa-nashego-isusa-hrista', 406),
        ('sretenie-gospoda-boga-i-spasa-nashego-isusa-hrista', 433),
        ('blagoveschenie-presvjatoj-vladychitsy-nashej-bogoroditsy-i-prisnodevy-marii', [750, 27, 28, 29, 4022]),
        ('svjatoe-preobrazhenie-gospoda-boga-i-spasa-nashego-isusa-hrista', 413),
        ('svetloe-hristovo-voskresenie-svjataja-pasha', 394),
        ('vhod-gospoden-v-ierusalim', 397),
        ('voznesenie-gospoda-boga-i-spasa-nashego-isusa-hrista', 393),
        ('perenesenie-iz-edessy-v-konstantinopol-nerukotvorennogo-obraza-ubrusa-gospoda-isusa-hrista-952', 429),

        ('rozhdestvo-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii', 280),
        ('vvedenie-v-tserkov-presvjatuju-vladychitsu-nashu-bogoroditsu', 51),
        ('uspenie-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii', [337, 340]),
        ('sobor-presvjatoj-bogoroditsy', 300),
        ('pokrov-presvjatoj-vladychicy-nashej-bogorodicy-i-prisnodevy-marii', 257),
        ('polozhenie-chestnoj-rizy-presvjatoj-bogorodicy-vo-vlaherne', 262),
        ('polozhenie-chestnogo-pojasa-presvjatoj-bogorodicy', 584),
        (
            'sretenie-vladimirskoj-ikony-presvjatoj-bogorodicy-prazdnestvo-ustanovleno-v-pamjat-spasenija-moskvy-ot-nashest',
            [4023, 548, 58]
        ),
        ('znamenie-presvjatoj-bogorodicy-byvshee-v-novgorode-velikom-v-1178-godu', [117, 121, 196]),

        ('rozhdestvo-chestnogo-slavnogo-proroka-predtechi-i-krestitelja-gospodnja-ioanna', 1966),
    ]
    any_ = [
        ('vozdvizhenie-chestnogo-i-zhivotvorjashchego-kresta-gospodnja', 392, 415),
        ('zachatie-prav-annoju-presvjatoj-bogorodicy', 112),
        ('den-pamjati-anna-mat-presvjatoj-bogorodicy', 1205),
    ]
    cathedrals = [
        ('sobor-arhistratiga-mihaila-i-prochih-besplotnyh', [718, 450, 712, 713, 714, 715, 716, 717]),
        ('sobor-arhangela-gavriila', 449),
        ('sobor-svjatyh-i-vsehvalnyh-12-ti-apostolov', 1244),
        ('sobor-70-ti-apostolov', 1245),
    ]
    other_pravicon_saints_ids: list[str | int] = [
        ('ermionija', 1802),
        ('den-pamjati-avgustin-blazhennyj', 1005),
        ('den-pamjati-agapit-i-rimskij', 1039),
        ('den-pamjati-akepsim-naessonskij-anisskij-i-iosif-persidskij-presviter-i-aifal-persidskij', 1079),
        ('den-pamjati-ammon-ammun-nitrijskij', 1142),
        (
            'den-pamjati-konstantin-ammorejskij-frigijskij-i-aetij-ammorejskij-frigijskij-i-feofil-ammorejskij-frigijskij-i-feodor-ammorejskij-frigijskij',
            1143
        ),
        ('den-pamjati-amfilohij-ikonijskij', 1149),
        ('den-pamjati-andrej-kritskij-svjatitel', 1183),
        ('den-pamjati-andronik-antiohijskij-i-afanasija-tavenskaja', 1193),
        ('den-pamjati-antonij-velikij', 1215),
        ('den-pamjati-arefa-negranskij', 1247),
        (
            'den-pamjati-ksenofont-konstantinopolskij-i-marija-konstantinopolskaja-i-arkadij-konstantinopolskij-i-ioann-konstantinopolskij-palestinskij',
            1257),
        ('den-pamjati-artemij-antiohijskij', 1277),
        ('den-pamjati-archil-ii-iverskij-i-luarsab-ii-kartalinskij', 1283),
        ('den-pamjati-varlaam-indijskij-i-ioasaf-indijskij-i-avenir-indijskij', 1359),
        ('den-pamjati-vasilij-velikij', 1384),
        ('svjatyh-treh-svjatitelej-vasilija-velikogo-grigorija-bogoslova-i-ioanna-zlatoustogo', 1465),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            1471
        ),
        ('den-pamjati-gemell-paflagonjanin', 1495),
        ('den-pamjati-genovefa-parizhskaya', 1501),
        ('den-pamjati-georgij-antiohijskij-pisidijskij', 1502),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            1506),
        ('den-pamjati-epifanij-kiprskij-i-german-konstantinopolskij', 1534),
        ('den-pamjati-grigorij-akragantijskij', 1559),
        ('den-pamjati-grigorij-armjanskij', 1560),
        ('den-pamjati-grigorij-bogoslov', 1561),
        ('den-pamjati-grigorij-dvoeslov', 1562),
        ('den-pamjati-grigorij-handztijskij-gruzinskij', 1579),
        ('den-pamjati-david-solunskij-fessalonikijskij', 1589),
        ('den-pamjati-evpsihij-kesarijskij-kappadokijskij', 1705),
        ('den-pamjati-evsevij-sirijskij', 1708),
        # ('Елена равноап.', 1767),
        # ('Константин равноап.', 2199),
        ('den-pamjati-epifanij-kiprskij-i-german-konstantinopolskij', 1790),
        ('den-pamjati-efrem-sirin', 1815),
        ('den-pamjati-zosima-palestinskij-otshelnik', 1836),
        ('den-pamjati-zotik-siropitatel', 1841),
        ('den-pamjati-iakov-postnik', 1852),
        ('den-pamjati-ieronim-stridonskij', 1887),
        ('den-pamjati-ilarion-gruzin', 1898),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            1927
        ),
        ('den-pamjati-ioann-damaskin', 1937),
        ('den-pamjati-drugoj-ioann-zlatoust', 1942),
        ('den-pamjati-ioann-kolov', 1947),
        (
            'den-pamjati-ksenofont-konstantinopolskij-i-marija-konstantinopolskaja-i-arkadij-konstantinopolskij-i-ioann-konstantinopolskij-palestinskij',
            1949
        ),
        ('den-pamjati-ioann-kushchnik', 1952),
        ('den-pamjati-ioann-lestvichnik', 1953),
        ('den-pamjati-ioann-milostivyj', 1955),
        ('den-pamjati-kleopatra-palestinskaja-i-ioann-palestinskij-voin', 1961),
        ('den-pamjati-ioann-egipetskij-pustynnik', 1969),
        ('den-pamjati-drugoj-ioann-hozevit', 1987),
        ('den-pamjati-isaak-sirin-ninevijskij', 2061),
        ('den-pamjati-isihij-horivit', 2080),
        ('den-pamjati-iustinian-i-upravda-i-feodora-grecheskaja-carica', 2105),
        ('den-pamjati-dada-persidskij-i-gaveddaj-gavdelas-persidskij-i-kazdoja-persidskaja', 2109),
        (
            'den-pamjati-konstantin-ammorejskij-frigijskij-i-aetij-ammorejskij-frigijskij-i-feofil-ammorejskij-frigijskij-i-feodor-ammorejskij-frigijskij',
            2112
        ),
        ('den-pamjati-kelestin-i-rimskij', 2131),
        ('den-pamjati-kirill-konstantin-filosof', 2167),
        ('den-pamjati-kliment-ankirskij-mnogostradalnyj-i-agafangel-rimljanin', 2182),
        ('den-pamjati-kolumban-ljuksejskij', 2188),
        ('den-pamjati-kosma-maiumskij', 2219),
        (
            'den-pamjati-ksenofont-konstantinopolskij-i-marija-konstantinopolskaja-i-arkadij-konstantinopolskij-i-ioann-konstantinopolskij-palestinskij',
            2237
        ),
        ('den-pamjati-lazar-konstantinopolskij', 2253),
        ('den-pamjati-lev-i', 2260),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            2271
        ),
        ('den-pamjati-liverij-rimskij', 2281),
        ('den-pamjati-makarij-aleksandrijskij-novyj-gradskij', 2313),
        ('den-pamjati-makrina-kappadokijskaja', 2335),
        ('den-pamjati-marina-berijskaja-makedonskaja-i-kira-berijskaja-makedonskaja', 2360),
        (
            'den-pamjati-ksenofont-konstantinopolskij-i-marija-konstantinopolskaja-i-arkadij-konstantinopolskij-i-ioann-konstantinopolskij-palestinskij',
            2368
        ),
        ('den-pamjati-mark-afinjanin-frakijskij', 2375),
        ('den-pamjati-mark-nitrijskij-egipetskij-kellijskij', 2379),
        ('den-pamjati-markian-konstantinopolskij-chtec-i-martirij-konstantinopolskij', 2389),
        ('den-pamjati-maron-sirijskij', 2392),
        ('den-pamjati-martin-i-rimskij', 2393),
        ('den-pamjati-martin-milostivyj-turskij', 2395),
        ('den-pamjati-martinian-kesarijskij-palestinskij', 2398),
        ('den-pamjati-melanija-rimljanynja', 2423),
        ('den-pamjati-moisej-murin', 2478),
        ('den-pamjati-nikita-gotfskij', 2523),
        ('den-pamjati-nikolaj-mirlikijskij', 2565),
        ('den-pamjati-nil-postnik', 2580),
        ('den-pamjati-nina-prosvetitelnica-gruzii', 2585),
        ('den-pamjati-onufrij-velikij', 2605),
        ('den-pamjati-pavel-fivejskij', 2641),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            2670
        ),
        ('den-pamjati-parfenij-lampsakijskij', 2672),
        ('den-pamjati-patapij-fivskij', 2673),
        ('den-pamjati-patrikiy-irlandskiy', 2675),
        ('den-pamjati-pahomij-velikij-egipetskij-fivaidskij', 2682),
        ('den-pamjati-pelagija-antiohijskaja', 2686),
        ('den-pamjati-petr-afonskij', 2693),
        ('den-pamjati-drugoj-petr-galatijskij', 2698),
        (
            'den-pamjati-manuil-adrianopolskij-i-georgij-develtskij-i-petr-adrianopolskij-i-leontij-leon-nikejskij-i-sionij-adrianopolskij',
            2707
        ),
        ('den-pamjati-pimen-velikij', 2719),
        ('den-pamjati-roman-sladkopevec', 2793),
        ('den-pamjati-savva-osvjashchennyj', 2812),
        ('den-pamjati-ioann-savvait-i-sergij-savvait-i-patrikij-savvait', 2822),
        ('den-pamjati-silvestr-i', 2886),
        ('den-pamjati-avdelaj-selevkijskij-i-ananija-selevkijskij', 2892),
        ('den-pamjati-simeon-palestinskij-i-ioann-palestinskij-spostnik', 2896),
        ('den-pamjati-simeon-stolpnik-divnogorets', 2900),
        ('den-pamjati-simeon-stolpnik-antiokhijskij-i-marfa-kappadokijskaja', 2901),
        ('den-pamjati-stefan-novyj', 2956),
        ('den-pamjati-stefan-savvait', 2962),
        ('den-pamjati-taisija-egipetskaja', 2974),
        ('den-pamjati-falassij-sirijskij-i-limnij-sirijskij-i-varadat-sirijskij', 3030),
        ('den-pamjati-feodor-aleksandrijskij', 3046),
        ('den-pamjati-feodor-nachertannyj', 3057),
        ('den-pamjati-iustinian-i-upravda-i-feodora-grecheskaja-carica', 3081),
        ('den-pamjati-feodosij-velikij-kinoviarh', 3085),
        ('den-pamjati-feofan-nikejskij', 3124),
        ('den-pamjati-feofan-ispovednik-sigrianskij', 3126),
        ('den-pamjati-filaret-milostivyj', 3143),
        ('den-pamjati-hariton-ispovednik', 3188),
        # ('X-XVII')
        ('den-pamjati-onufrij-percovskij-i-avksentij-percovskij', 1018),
        ('den-pamjati-avraamij-bolgarskij-vladimirskij', 1023),
        ('den-pamjati-avramij-galichskij-chuhlomskoj', 1024),
        ('den-pamjati-agapit-pecherskij', 1038),
        ('den-pamjati-adrian-poshehonskij-jaroslavskij', 1067),
        ('den-pamjati-aleksandr-peresvet-i-andrej-osljabja', 1086),
        ('den-pamjati-aleksij-moskovskij', 1125),
        ('den-pamjati-ammon-pecherskij', 1141),
        ('den-pamjati-anastasij-pecherskij', 1158),
        ('den-pamjati-anatolij-pecherskij-i-anatolij-pecherskij-zatvornik', 1172),
        ('den-pamjati-angelina-serbskaja-brankovich', 1174),
        (
            'den-pamjati-kliment-ohridskij-velichskij-bolgarskij-i-naum-ohridskij-i-savva-ohridskij-i-gorazd-ohridskij-i-angeljar-ohridskij',
            1175
        ),
        ('den-pamjati-aleksandr-peresvet-i-andrej-osljabja', 1177),
        ('den-pamjati-andrej-rublev', 1180),
        ('den-pamjati-andrej-konstantinopolskij', 1181),
        ('obretenie-moschej-andrej-smolenskij', 1188),
        ('den-pamjati-andronik-moskovskij-i-savva-moskovskij', 1195),
        ('den-pamjati-anna-kashinskaja', 1202),
        ('den-pamjati-arefa-pecherskij-i-sisoj-pecherskij-zatvornik-i-feofil-pecherskij-zatvornik', 1248),
        ('den-pamjati-arsenij-komelskij', 1264),
        ('den-pamjati-arsenij-novgorodskij', 1266),
        ('den-pamjati-arsenij-pecherskij-i-pimen-pecherskij', 1268),
        ('den-pamjati-afanasij-serpuhovskij', 1291),
        ('den-pamjati-lazar-muromskij-murmanskij-olonetskij-i-afanasij-muromskij-murmanskij-olonetskij', 1296),
        ('den-pamjati-afanasij-pecherskij-zatvornik', 1303),
        ('den-pamjati-boris-v-kreshchenii-mihail-bolgarskij', 1325),
        ('den-pamjati-varlaam-pinezhskij', 1358),
        ('den-pamjati-varlaam-keretskij', 1360),
        ('den-pamjati-varsonofij-tverskoj-episkop', 1374),
        ('den-pamjati-vasilij-spaso-kubenskij-kamenskij', 1388),
        ('den-pamjati-vasilij-moskovskij', 1392),
        ('den-pamjati-vasilij-rjazanskij', 1401),
        ('den-pamjati-vasilij-vsevolodovich-jaroslavskij-i-konstantin-vsevolodovich-jaroslavskij', 1407),
        ('den-pamjati-veniamin-pecherskij', 1422),
        ('den-pamjati-vladimir-jaroslavich-novgorodskij', 1449),
        ('den-pamjati-vel-kn-vladimir-v-kreshchenii-vasilij', 1450),
        ('den-pamjati-vsevolod-v-kreshchenii-gavriil-novgorodskij', 1464),
        ('den-pamjati-prohor-pshinskij-i-gavriil-lesnovskij', 1475),
        ('den-pamjati-ioann-svjatogorec-iverskij-afonskij-i-gavriil-svjatogorets-iverskij-afonskij', 1478),
        ('den-pamjati-gennadij-kostromskoj-ljubimogradskij', 1499),
        ('den-pamjati-georgij-jurij-vsevolodovich-vladimirskij', 1504),
        ('den-pamjati-georgij-svjatogorets-iverskij-afonskij', 1516),
        ('den-pamjati-gerasim-velikopermskij-ustvymskij', 1525),
        ('den-pamjati-german-kazanskij-i-svijazhskij', 1533),
        ('obretenie-moschej-german-soloveckij', 1536),
        ('den-pamjati-gerontij-moskovskij-i-vseja-rossii', 1540),
        (
            'den-pamjati-kliment-ohridskij-velichskij-bolgarskij-i-naum-ohridskij-i-savva-ohridskij-i-gorazd-ohridskij-i-angeljar-ohridskij',
            1553
        ),
        ('den-pamjati-grigorij-palama-solunskij-fessalonikijskij', 1571),
        ('den-pamjati-grigorij-pelshemskij', 1572),
        ('den-pamjati-david-iv-vozobnovitel', 1590),
        # ('dimitrij-donskoj', 1620),
        ('den-pamjati-dimitrij-priluckij', 1624),
        ('den-pamjati-dionisij-pecherskij-shchepa', 1641),
        ('den-pamjati-dosifej-verhneostrovskij', 1667),
        ('den-pamjati-stefan-miljutin-i-dragutin-v-inochestve-feoktist-serbskij-i-elena-serbskaja', 1669),
        ('den-pamjati-evfimij-novyj-svjatogorets-iverskij-afonskij', 1736),
        ('den-pamjati-evfimij-pecherskij-i-lavrentij-pecherskij', 1738),
        ('den-pamjati-evfimij-sjanzhemskij-vologodskij', 1741),
        ('den-pamjati-evfrosin-pskovskij-spaso-eleazarovskij-i-serapion-pskovskij-spaso-eleazarovskij', 1746),
        ('den-pamjati-evfrosinija-v-miru-feodulija-suzdalskaja', 1753),
        ('den-pamjati-stefan-miljutin-i-dragutin-v-inochestve-feoktist-serbskij-i-elena-serbskaja', 1768),
        ('den-pamjati-elladij-pecherskij-i-onisim-pecherskij', 1778),
        ('den-pamjati-efrem-perekomskij-novgorodskij', 1812),
        ('den-pamjati-iakov-borovichskij', 1847),
        ('den-pamjati-iakov-zheleznoborovskij-i-iakov-bryleevskij', 1849),
        ('den-pamjati-ioann-v-inochestve-ignatij-uglichskij', 1876),
        ('den-pamjati-igor-v-kreshchenii-georgij-chernigovskij-i-kievskij', 1881),
        ('den-pamjati-ilarion-pecherskij', 1899),
        ('perenesenie-moschej-ilarion-meglinskij', 1900),
        ('den-pamjati-ioann-vlasatyj-milostivyj-rostovskij', 1934),
        ('den-pamjati-feodor-varjag-i-ioann-pecherskij-kievskij', 1946),
        ('den-pamjati-ioann-kukuzel', 1951),
        ('den-pamjati-ioann-novgorodskij', 1959),
        ('den-pamjati-ioann-svjatogorec-iverskij-afonskij-i-gavriil-svjatogorets-iverskij-afonskij', 1976),
        ('den-pamjati-ioann-serbskij-i-stefan-serbskij-brankovich-i-angelina-serbskaja-brankovich', 1978),
        ('den-pamjati-ioann-novyj-sochavskij', 1980),
        ('den-pamjati-ioann-ustjuzhskij-blazhennyj', 1985),
        ('den-pamjati-ioasaf-kamenskij-spasokubenskij', 1998),
        ('den-pamjati-ioasaf-snetogorskij', 2001),
        ('den-pamjati-iona-moskovskij-i-vseja-rusi', 2012),
        ('den-pamjati-iona-velikopermskij', 2015),
        ('den-pamjati-mark-pskovo-pecherskij-i-iona-pskovo-pecherskij', 2019),
        ('den-pamjati-iosif-volockij-volokolamskij', 2023),
        ('den-pamjati-nikita-nifont-alfanov-i-kirill-alfanov-i-nikifor-alfanov-i-kliment-alfanov-i-isaakij-alfanov',
         2068),
        ('den-pamjati-isidor-tverdislov-rostovskij', 2075),
        ('obretenie-moschej-iulianija-olshanskaja', 2095),
        ('den-pamjati-grigorij-avnezhskij-i-kassian-avnezhskij', 2127),
        ('den-pamjati-kassian-komelskij-i-lavrentij-komelskij', 2128),
        ('den-pamjati-kassian-uglichskij-grek', 2129),
        ('den-pamjati-kiprian-moskovskij', 2145),
        ('den-pamjati-kirill-novoezerskij-novgorodskij', 2162),
        ('den-pamjati-nikita-nifont-alfanov-i-kirill-alfanov-i-nikifor-alfanov-i-kliment-alfanov-i-isaakij-alfanov',
         2165),
        ('den-pamjati-kirill-chelmogorskij', 2169),
        (
            'den-pamjati-kliment-ohridskij-velichskij-bolgarskij-i-naum-ohridskij-i-savva-ohridskij-i-gorazd-ohridskij-i-angeljar-ohridskij',
            2184),
        ('den-pamjati-nikita-nifont-alfanov-i-kirill-alfanov-i-nikifor-alfanov-i-kliment-alfanov-i-isaakij-alfanov',
         2185),
        ('den-pamjati-konstantin-kievskij-i-vseja-rossii', 2196),
        ('den-pamjati-vasilij-vsevolodovich-jaroslavskij-i-konstantin-vsevolodovich-jaroslavskij', 2201),
        ('den-pamjati-lavrentij-kaluzhskij', 2245),
        ('den-pamjati-kassian-komelskij-i-lavrentij-komelskij', 2246),
        ('den-pamjati-evfimij-pecherskij-i-lavrentij-pecherskij', 2247),
        ('den-pamjati-lavrentij-pecherskij-turovskij', 2248),
        ('obretenie-moschej-leontij-rostovskij', 2278),
        ('den-pamjati-longin-pecherskij', 2287),
        ('den-pamjati-luka-elladskij', 2292),
        ('den-pamjati-ljudmila-cheshskaja', 2310),
        ('den-pamjati-makarij-moskovskij', 2325),
        ('den-pamjati-makarij-pecherskij-diakon', 2328),
        ('den-pamjati-maksim-moskovskij', 2343),
        ('den-pamjati-mardarij-pecherskij', 2355),
        ('den-pamjati-mark-evgenik', 2377),
        ('den-pamjati-mark-pskovo-pecherskij-i-iona-pskovo-pecherskij', 2381),
        ('den-pamjati-martirij-pecherskij-i-martirij-pecherskij-zatvornik', 2403),
        ('den-pamjati-martirij-pecherskij-i-martirij-pecherskij-zatvornik', 2404),
        ('den-pamjati-mihail-kievskij-i-vseja-rusi', 2460),
        ('den-pamjati-mihail-klopskij', 2461),
        ('den-pamjati-mihail-jaroslavich-tverskoj', 2471),
        ('den-pamjati-mihail-chernigovskij-i-feodor-chernigovskij', 2472),
        ('den-pamjati-moisej-pecherskij', 2481),
        ('den-pamjati-nikandr-pskovskij', 2518),
        (
            'den-pamjati-nikita-nifont-alfanov-i-kirill-alfanov-i-nikifor-alfanov-i-kliment-alfanov-i-isaakij-alfanov',
            2521
        ),
        ('den-pamjati-nikita-pecherskij-novgorodskij-zatvornik', 2527),
        (
            'den-pamjati-nikita-nifont-alfanov-i-kirill-alfanov-i-nikifor-alfanov-i-kliment-alfanov-i-isaakij-alfanov',
            2534
        ),
        ('den-pamjati-nikola-svjatosha', 2542),
        ('den-pamjati-nikolaj-kochanov', 2551),
        ('den-pamjati-nikolaj-sallos-pskovskij', 2557),
        ('den-pamjati-nifont-pecherskij-novgorodskij', 2589),
        ('den-pamjati-oleg-v-inochestve-vasilij-romanovich-brjanskij', 2593),
        ('den-pamjati-elladij-pecherskij-i-onisim-pecherskij', 2600),
        ('den-pamjati-onufrij-malskij', 2608),
        ('den-pamjati-onufrij-pecherskij-i-onisim-pecherskij', 2609),
        ('den-pamjati-pavel-komelskij-obnorskij', 2628),
        ('den-pamjati-paraskeva-petka', 2664),
        ('den-pamjati-pakhomij-nerekhtskij-sypanovskij-kostromskoj', 2684),
        ('den-pamjati-gerasim-velikopermskij-ustvymskij-i-pitirim-velikopermskij-i-iona-velikopermskij', 2690),
        ('den-pamjati-petr-bolgarskij', 2694),
        ('den-pamjati-stefan-kazanskij-i-petr-kazanskij', 2701),
        ('den-pamjati-petr-moskovskij', 2708),
        ('den-pamjati-kuksha-pecherskij-i-pimen-pecherskij-postnik', 2724),
        ('den-pamjati-pitirim-velikopermskij', 2726),
        ('den-pamjati-prokopiy-sazavskiy', 2763),
        ('den-pamjati-prokopij-ustjuzhskij', 2765),
        ('den-pamjati-prohor-pshinskij-i-gavriil-lesnovskij', 2771),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
        ('',),
    ]
    icons_data_in: list[schemas.IconDataCreate] = prepare.get_other_saints_icons_data_in(
        session,
        pravicon_saints_ids=other_pravicon_saints_ids
    )
    for icon_data_in in icons_data_in:
        create_icon(db, icon_data_in=icon_data_in)


def _create_all_gallerix_icons(db: Session, *, driver: WebDriver) -> None:
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


def _create_all_shm_icons(db: Session, *, driver: WebDriver) -> None:
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
         ['1655698', '1652998', '1652555', '1652607', '1654311', '5521034', '5521035']),
        # ('ioann-lestvichnik', ['']),
        ('ioann-bogoslov', ['1654252', '1654246']),
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
        ('svetloe-hristovo-voskresenie-svjataja-pasha', ['1655088', '1655704', '1654530']),
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
    if icon := crud.icon.get_by_gallerix_id(db, gallerix_id=gallerix_icon_id):
        holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
        crud.icon.create_holiday_association(
            db,
            db_obj=icon,
            holiday=holiday,
            icon_holiday_association_in=schemas.IconHolidayAssociationCreate()
        )
    else:
        icon_data_in = prepare.get_gallerix_icon_data_in(
            driver,
            holiday_slug=holiday_slug,
            gallerix_icon_id=gallerix_icon_id
        )
        create_icon(db, icon_data_in=icon_data_in)


def __create_shm_icon(db: Session, *, driver: WebDriver, holiday_slug: str, shm_icon_id: int) -> None:
    if icon := crud.icon.get_by_shm_id(db, shm_id=shm_icon_id):
        holiday = crud.holiday.get_by_slug(db, slug=holiday_slug)
        crud.icon.create_holiday_association(
            db,
            db_obj=icon,
            holiday=holiday,
            icon_holiday_association_in=schemas.IconHolidayAssociationCreate()
        )
    else:
        icon_data_in = prepare.get_shm_icon_data_in(driver, holiday_slug=holiday_slug, shm_icon_id=shm_icon_id)
        create_icon(db, icon_data_in=icon_data_in)
