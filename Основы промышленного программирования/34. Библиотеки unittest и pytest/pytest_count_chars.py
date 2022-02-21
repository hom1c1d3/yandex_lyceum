import pytest
from yandex_testing_lesson import count_chars


def test_empty_string():
    assert count_chars("") == {}


def test_just_string():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}


def test_white_spaces():
    assert count_chars(" \t\n \n\t ") == {' ': 3, '\t': 2, '\n': 2}


def test_wrong_type_non_iterable():
    with pytest.raises(TypeError):
        count_chars(42)


def test_wrong_type_iterable():
    with pytest.raises(TypeError):
        count_chars(['a', 'b', 'c'])
