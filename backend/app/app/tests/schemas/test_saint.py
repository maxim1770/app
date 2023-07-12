from app.schemas.saint.saint import SaintCreate


def test_saint_in():
    saint_in = SaintCreate(slug='test')
    assert saint_in.name is None
