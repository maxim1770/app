import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # path = Path(r"..\\..\\..\\data\\img\\manuscripts\\nlr\\sof\\50d07a48-b72e-4372-b020-ad5baf59f797\\5.webp")
    # print(str(path).split('manuscripts'))

    a = 'Кондак den-pamjati-drugoj-sergij-radonezhskij'
    # print(int(a[a.find('глас') + 4:].strip()[0]))
    print(a.split()[1].strip())

