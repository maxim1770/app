import re

import requests

from app.create.prepare.base_collect import verify_saint_slug


def __verify_saints_slugs(session: requests.Session, *, saints_slugs: str) -> list[str]:
    saints_slugs: list[str] = saints_slugs.split('-')
    verified_saints_slugs: list[str] = []
    while saints_slugs:
        k: int = 0
        while not verify_saint_slug(session, saint_slug='-'.join(saints_slugs[:k + 1])):
            k += 1
        verified_saints_slugs.append('-'.join(saints_slugs[:k + 1]))
        saints_slugs: list[str] = saints_slugs[k + 1:]
    return verified_saints_slugs


if __name__ == '__main__':
    s = 'Сщмчч.\n    Акепси́ма, епи'
    ss = 'Сщмчч.\n   Акепси́ма, епи'

    for i in [s, ss]:
        i = i.replace('\n', '')
        i = re.sub(r'\s{2,}', ' ', i)
        print(i)
        print(' '.join(i.split()))

    # kesarijskie  kappadokijskie
    # kesarijskaja- kappadokijskaja
