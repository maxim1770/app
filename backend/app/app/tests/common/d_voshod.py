import logging

import requests

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
from datetime import time, datetime

from app import const
from app.api import deps

if __name__ == '__main__':
    session: requests.Session = next(deps.get_session())
    datetime_: datetime = datetime.now()
    datetime_ = datetime_.replace(year=datetime_.year + const.NUM_OFFSET_YEARS)
    __sunset_hour, __sunset_minute = const.DAY_SUNSETS[datetime_.month][datetime_.day]
    _sunset_time = time(hour=__sunset_hour, minute=__sunset_minute)
    if datetime_.time() > _sunset_time:
        datetime_ = datetime_.replace(day=datetime_.day + 1)
