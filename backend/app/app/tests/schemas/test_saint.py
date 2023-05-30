from app.schemas.saint.saint import __SaintBase


def test_saint_base():
    saint_base = __SaintBase(slug='test')
    assert saint_base.name is None
