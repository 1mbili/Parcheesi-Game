import pytest
from src.entities.field import Field, NoPawnFoundException
from src.entities.pawn import Pawn


def test_no_pawn_exception():
    field = Field()
    with pytest.raises(NoPawnFoundException):
        field.take_pawn("red")


def test_add_pawn_to_field():
    field = Field()
    red_pawn = Pawn("red")
    field.move_pawn(red_pawn)
    assert red_pawn in field


def test_pawn_representation():
    field = Field()
    red_pawn = Pawn("red")
    field.move_pawn(red_pawn)
    assert f"{red_pawn}" in repr(field)


def test_take_pawn():
    field = Field()
    red_pawn = Pawn("red")
    field.move_pawn(red_pawn)
    taken_pawn = field.take_pawn("red")
    assert taken_pawn == red_pawn


def test_beat_pawn_on_field():
    field = Field()
    red_pawn = Pawn("red")
    blue_pawn = Pawn("blue")
    field.move_pawn(red_pawn)
    field.move_pawn(red_pawn)
    beaten_pawns = field.move_pawn(blue_pawn)
    assert blue_pawn in field.pawns
    assert red_pawn not in field.pawns
    assert [red_pawn, red_pawn] == beaten_pawns
