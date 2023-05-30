import logging

from selenium.webdriver.chrome.webdriver import WebDriver

from app.create.prepare.icon._get_verived_shm_icons_ids import get_verived_shm_icons_ids

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    a = get_verived_shm_icons_ids(driver)
    logging.info(a)

    verived_shm_icons_ids = ['1650005', '5692788', '5692789', '1652337', '1654240', '1654239', '1650001', '1650004',
                             '1650949',
                             '1650525', '1651718', '1652338', '1652307', '5521020', '5521023', '5521024', '1649915',
                             '1654122', '1650661',
                             '1652590', '1655597', '1651166', '1651329', '1649842', '1652552', '1652553', '1652551',
                             '1653673', '1654125',
                             '1655562', '1649797', '1650060', '1650775', '1651290', '1651325', '1651326', '1651327',
                             '1651328', '1651330',
                             '1651694', '1651696', '1651697', '1651712', '1652136', '1652137', '1652983', '1653356',
                             '1653426', '1653427',
                             '1652595', '1652608', '1654238', '1654254', '1654256', '1654259', '1654534', '1654612',
                             '1655502', '1655704',
                             '5534081', '5534082', '1654255', '1652616', '1655507', '1650003', '1654260', '1649169',
                             '1650950', '1650424',
                             '1650425', '1650423', '1650421', '1650422', '1650426', '1650437', '1650629', '1652207',
                             '1655698', '1651695',
                             '1652629', '1653665', '1653662', '1653741', '1653936', '1654123', '1654865', '1654970',
                             '1655071', '1655072',
                             '1655086', '1655313', '1655334', '1655441', '1648931', '1648768', '1649055', '1649056',
                             '1649057', '1649058',
                             '1649059', '1649060', '1649061', '1649062', '1649139', '1649718', '1649778', '1649998',
                             '1649999', '1650000',
                             '1650092', '1650069', '1650420', '1650439', '1650457', '1650463', '1650491', '1650513',
                             '1650801', '1650534',
                             '1650665', '1650889', '1651019', '1651178', '1651083', '1651131', '1651294', '1651320',
                             '1651321', '1651322',
                             '1651372', '1651717', '1651722', '1651723', '1651752', '1652013', '1652020', '1652217',
                             '1652218', '1652345',
                             '1652413', '1652558', '1652561', '1652575', '1652576', '1652581', '1652617', '1652620',
                             '1652625', '1652628',
                             '1652720', '1652755', '1652758', '1652964', '1652807', '1652808', '1652829', '1652890',
                             '1652907', '1652944',
                             '1652946', '1652948', '1652949', '1652950', '1652952', '1652957', '1652972', '1652981',
                             '1652998', '1653045',
                             '1653113', '1653123', '1653150', '1653378', '1653424', '1653425', '1652436', '1652555',
                             '1652557', '1652607',
                             '1652606', '1653440', '1654129', '1654235', '1654244', '1654246', '1654245', '1654247',
                             '1654248', '1654249',
                             '1654250', '1654251', '1654253', '1654252', '1654258', '1654261', '1654262', '1654304',
                             '1654525', '1654526',
                             '1654528', '1654527', '1654531', '1654530', '1654533', '1654532', '1655409', '1655696',
                             '117767', '1650480',
                             '5534076', '5534077', '5534083', '5534084', '5534338', '5520957', '5520958', '5535413',
                             '5535414', '5534275',
                             '5534276', '5534281', '5534282', '5534283', '5534284', '5535002', '5534594', '5534595',
                             '5534932', '5580872',
                             '1654021', '5691816', '1652775', '5535951', '1654225', '1653780', '1652770', '5691817',
                             '5535952', '1652768',
                             '1655064', '1655088', '1655337', '1655480', '1655576', '1649878', '1651341', '1651991',
                             '1652906', '1653147',
                             '1652910', '1654311', '1654492', '1654667', '1655657', '5520952', '5533848', '1651990',
                             '1655327', '1655765',
                             '1654097', '1654951', '1655030', '1649947', '1650489', '1650496', '1650121', '1650474',
                             '1650478', '1650490',
                             '1650951', '1651981', '1652953', '1652954', '1652089', '1654541', '1655699', '1655838',
                             '5521034', '5521035',
                             '5535006', '5535007', '1652973', '1650454', '1651831']

    # for tag in get_verived_shm_icons_ids(driver):
    #     url = 'https://catalog.shm.ru/' + tag['href']
    #     driver.get(url)
    #     year_title = BeautifulSoup(driver.page_source, 'lxml').find(
    #         lambda tag: tag.name == 'div' and 'Датировка' == tag.text
    #     ).next_sibling.text.replace('Читать далее', '')
    #     try:
    #         prepared_year_title: str = PrepareYearTitle(year_title).year_title
    #         year_in = schemas.YearCreate(title=prepared_year_title)
    #     except ValueError as e:
    #         pass
    #     else:
    #         logging.info(year_in)
