import pytest
from pydantic import ValidationError

from app.schemas.manuscript.manuscript import ManuscriptCreateAny, ManuscriptBase


@pytest.mark.parametrize('manuscript_code, manuscript_neb_slug', [
    ('foo', 'foo'),
    ('foo', None),
    (None, 'foo')
])
def test_schema_manuscript_create_any(manuscript_code: str | None, manuscript_neb_slug: str | None) -> None:
    manuscript_in = ManuscriptCreateAny(code=manuscript_code, neb_slug=manuscript_neb_slug)
    assert manuscript_in


def test_schema_manuscript_create_any_bad() -> None:
    with pytest.raises(ValidationError) as e:
        ManuscriptCreateAny(title='foo', code_title='foo')
    assert e.type is ValidationError


@pytest.mark.parametrize('manuscript_code', [
    'EEA307AE-85DA-440A-80C2-46BD1D262ECE'
    '14CB689B-8344-49F0-9DD6-0AAE09460BE0'
    '59014138-46CC-4335-9E3C-9F903FD854A3',
    'f-37-187',
    'f-304iii-21'
])
def test_manuscript_code(manuscript_code: str) -> None:
    assert ManuscriptBase(code=manuscript_code)
