import logging

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from app.api import deps

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # logging.info(get_verived_gallerix_icons_ids(driver))

    verived_gallerix_icons_ids = ['4065281575', '3258948338', '1549471566', '2652240293', '683371191', '89790019',
                                  '1470889248', '320510357',
                                  '7433219', '2888014627', '3636723403', '1185377134', '1574648303', '3445892191',
                                  '3948181352', '2622703614',
                                  '157467796', '791746187', '1299596441', '182849785', '4108380166', '1103802229',
                                  '2675078954', '265120442',
                                  '4050548477', '1641114475', '138876558', '2016272895', '4283582178', '291252173',
                                  '37212762', '548195762',
                                  '689602973', '3817190861', '1363546008', '2126516406', '1880856712', '3040389732',
                                  '891996828', '1488068390',
                                  '633727841', '2030579737', '3242162079', '3356043925', '2823729773', '1835892864',
                                  '3410998130', '1428891343',
                                  '1380377288', '3158868964', '573314629', '3424810857', '3139782651', '3923029146',
                                  '4077458721', '2548164891',
                                  '1848586563', '3884653972', '4270861525', '2308381763', '422052305', '250132640',
                                  '2045741110', '3773225357']
