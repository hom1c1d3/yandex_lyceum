import pytest
from yandex_testing_lesson import Rectangle


def test_init_wrong_type():
    with pytest.raises(TypeError):
        Rectangle("a", "b")


def test_init_wrong_format():
    with pytest.raises(ValueError):
        Rectangle(-1, -2)


def test_area():
    rect = Rectangle(2, 4)
    assert rect.get_area() == 8


def test_zero_area():
    rect = Rectangle(0, 0)
    assert rect.get_area() == 0


def test_perimeter():
    rect = Rectangle(2, 4)
    assert rect.get_perimeter() == 12
