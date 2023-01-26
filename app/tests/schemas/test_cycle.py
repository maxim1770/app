from hypothesis import given, strategies as st

from app import schemas

"""
Думаю что неплохая штука - hypothesis
для тестирования pydantic
Неплохо например тестируем что при создании abbr, abbr_ru так же создается
а другие поля, пока что не тестируем, и hypothesis остальные поля создает автоматически сам рандомно

читать документацию hypothesis, чтобы понять как все правильно делать/писать

"""


@given(st.builds(schemas.CycleCreate))
def test_property(instance) -> None:
    assert 0 < instance.num


@given(st.builds(schemas.CycleCreate, num=st.integers(1, 3)))
def test_with_discount(instance) -> None:
    assert 1 <= instance.num <= 3


@given(st.from_type(schemas.CycleCreate))
def test_me(cycle: schemas.CycleCreate) -> None:
    assert isinstance(cycle, schemas.CycleCreate)
