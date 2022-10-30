import pytest
from src.entities.player import Player
from src.entities.enums import PlayerStarting


# Red starting point - 0
@pytest.fixture
def player_red():
    player = Player("RED")
    player.house = [0, 1, 0, 0]
    player.free_pawns = 0
    player.pawns_position = [0, 39, 1]
    return player


# Green starting point - 0
@pytest.fixture
def player_finished_game():
    player = Player("GREEN")
    player.house = [1, 1, 1, 1]
    player.free_pawns = 0
    player.pawns_position = []
    return player


# Blue starting point - 10
@pytest.fixture
def player_blue():
    player = Player("BLUE")
    player.house = [0, 1, 0, 0]
    player.free_pawns = 1
    player.pawns_position = [15, 39, -1]
    return player


# Green starting point - 0
@pytest.fixture
def player_green():
    player = Player("GREEN")
    player.house = [0, 1, 0, 0]
    player.free_pawns = 1
    player.pawns_position = [15, 39, -1]
    return player


def test_simple():
    player = Player("RED")
    assert player.color == "RED"
    assert player.house == [0, 0, 0, 0]
    assert player.starting_point == PlayerStarting.RED.value
    assert player.free_pawns == 4
    assert player.pawns_position == [-1, -1, -1, -1]


def test_correct_free_pawns(player_blue):
    assert player_blue.has_free_pawns() is True


def test_simple_move_to_house(player_blue):
    player_blue.move_to_house(3, 39)
    assert player_blue.pawns_position == [15, -1]
    assert player_blue.house == [0, 1, 0, 1]


def test_get_further_pawn(player_blue):
    further = player_blue.get_further_pawn()
    assert further == 39


def test_get_further_not_max_index_is_further(player_green):
    further = player_green.get_further_pawn()
    assert further == 15


def test_get_further_pawn_before_house(player_red):
    further = player_red.get_further_pawn()
    assert further == 39


def test_finished_game(player_finished_game):
    further = player_finished_game.get_further_pawn()
    assert further == -2


def test_further_pawn_in_starting_point():
    player = Player("GREEN")
    player.pick_pawn_from_hand()
    further = player.get_further_pawn()
    assert further == player.starting_point


def test_move_in_house(player_blue):
    assert player_blue.move_in_house(2) is True


def test_move_in_house_no_place(player_blue):
    assert player_blue.move_in_house(4) is False


def test_return_pawn(player_blue):
    player_blue.return_pawn(15)
    assert player_blue.pawns_position == [39, -1, -1]
    assert player_blue.free_pawns == 2


def test_move_pawn(player_blue):
    player_blue.move_pawn_loc(15, 18)
    assert all(pawn in [39, 18, -1] for pawn in player_blue.pawns_position)


def test_pick_pawn_from_hand(player_blue):
    player_blue.pick_pawn_from_hand()
    assert player_blue.free_pawns == 0
    assert all(pawn in [39, 15, 10] for pawn in player_blue.pawns_position)


def test_no_pawn_to_pick_from_hand(player_finished_game):
    pick_return_code = player_finished_game.pick_pawn_from_hand()
    assert pick_return_code == 0
