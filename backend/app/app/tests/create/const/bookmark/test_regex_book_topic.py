import pytest

from app.create.const import BookRegex


@pytest.mark.parametrize('book_topic', [
    'Слово о Покаянии',
    'Поучение от Патерика',
    'Слово-история',
    'Слово ioann-zlatoust о Добродетели',
    'Слово ioann-zlatoust о Труде, и о Царствии Небесном',
    'Слово о Царствии Небесном, и о муке бесконечной',
    'Слово от Патерика о Царствии Небесном, и о муке бесконечной',
])
def test_regex_book_topic(book_topic: str) -> None:
    assert BookRegex.TOPIC.match(book_topic)[0] == book_topic


@pytest.mark.parametrize('book_topic', [
    'Слово ',
    'Слово от Патерика ioann-lestvichnik',
    'Слово о Послушании grigorij-bogoslov',
    'Слово о Послушании от Патерика',
    'Слово о efrem-sirin',
])
def test_regex_book_topic_bad(book_topic: str) -> None:
    assert BookRegex.TOPIC.match(book_topic) is None
