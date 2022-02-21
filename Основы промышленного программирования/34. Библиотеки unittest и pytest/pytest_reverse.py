import pytest
from yandex_testing_lesson import reverse  # будет доступна


def test_empty_string():
    assert reverse("") == ""


def test_single_symbol():
    assert reverse("a") == "a"


def test_palindrome():
    assert reverse("хакер в реках") == "хакер в реках"


def test_just_string():
    assert reverse("just string") == "gnirts tsuj"


def test_wrong_type_non_iterable():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type_iterable():
    with pytest.raises(TypeError):
        reverse([1, 2, 3, 4])