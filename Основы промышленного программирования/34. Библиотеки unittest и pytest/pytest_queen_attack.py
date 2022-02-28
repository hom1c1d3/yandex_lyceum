import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_position_out_of_board():
    with pytest.raises(ValueError):
        is_under_queen_attack("i8", "h8")
        is_under_queen_attack("h9", "h8")


def test_position_wrong_format():
    with pytest.raises(ValueError):
        is_under_queen_attack("H8", "h8")
        is_under_queen_attack("h 8", "h8")
        is_under_queen_attack("88", "h8")
        is_under_queen_attack("abc", "h8")


def test_position_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack((8, 8), "h8")
        is_under_queen_attack(64, "h8")


def test_queen_position_out_of_board():
    with pytest.raises(ValueError):
        is_under_queen_attack("h8", "i8")
        is_under_queen_attack("h8", "h9")


def test_queen_position_wrong_format():
    with pytest.raises(ValueError):
        is_under_queen_attack("h8", "H8")
        is_under_queen_attack("h8", "h 8")
        is_under_queen_attack("h8", "88")
        is_under_queen_attack("h8", "abc")


def test_queen_position_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack("h8", (8, 8))
        is_under_queen_attack("h8", 64)


def test_queen_can_beat_same_cell():
    assert is_under_queen_attack("a1", "a1")


def test_queen_can_beat():
    assert is_under_queen_attack("a1", "h8")


def test_queen_can_not_beat():
    assert not is_under_queen_attack("a1", "g8")
