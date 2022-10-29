import pytest
from src.entities.player import Player
from src.entities.Enums import Player_starting


@pytest.fixture
def player_ingame():
    player = Player("BLUE")
    player.house = [0, 1, 0, 0]
    player.free_pawns = 1
    player.pawns_position = [15, 39, -1]
    return player


def test_simple():
    player = Player("RED")
    assert player.color == "RED"
    assert player.house == [0, 0, 0, 0]
    assert player.starting_point == Player_starting.RED.value
    assert player.free_pawns == 4
    assert player.pawns_position == [-1, -1, -1, -1]

