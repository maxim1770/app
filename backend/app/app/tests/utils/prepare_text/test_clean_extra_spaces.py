import pytest

from app import utils


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    (' fsdf  fsdf', 'fsdf fsdf'),
    (' fsf      sdf', 'fsf sdf'),
    ('Привет как  дела ', 'Привет как дела'),
])
def test_clean_extra_spaces(some_str, cleaned_some_str) -> None:
    assert utils.clean_extra_spaces(some_str) == cleaned_some_str


@pytest.mark.parametrize('some_str, cleaned_some_str', [
    ('Привет ,', 'Привет,'),
    ('   fsf   ,  fsdf , fsdf   ', 'fsf, fsdf, fsdf'),
])
def test_clean_extra_spaces_bad(some_str, cleaned_some_str) -> None:
    assert utils.clean_extra_spaces(some_str) != cleaned_some_str


def test_clean_extra_spaces_removes_extra_spaces():
    input_text = "   This    is    a   test   sentence.   "
    expected_output = "This is a test sentence."
    assert utils.clean_extra_spaces(input_text) == expected_output


def test_clean_extra_spaces_handles_empty_string():
    input_text = ""
    expected_output = ""
    assert utils.clean_extra_spaces(input_text) == expected_output


def test_clean_extra_spaces_handles_single_space():
    input_text = " "
    expected_output = ""
    assert utils.clean_extra_spaces(input_text) == expected_output


def test_clean_extra_spaces_handles_no_extra_spaces():
    input_text = "This is a test sentence."
    expected_output = "This is a test sentence."
    assert utils.clean_extra_spaces(input_text) == expected_output


def test_clean_extra_spaces_handles_tabs_and_newlines():
    input_text = "  \tThis \n is \t a test \n sentence. \t  "
    expected_output = "This is a test sentence."
    assert utils.clean_extra_spaces(input_text) == expected_output
