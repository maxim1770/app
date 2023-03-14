from app.schemas.saint.saint import SaintBase


def test_saint_base():
    saint_base = SaintBase(slug='test')
    assert saint_base.name is None
