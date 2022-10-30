from src.entities.game import Game


def test_simple_game_round_count():
    game = Game()
    for i in range(5):
        game.move()
    assert game.round == 5


def test_perform_game():
    game = Game(seed=123)
    result = game.start_game(355)
    assert result == 0


def test_perform_game_too_small_game_limit():
    game = Game(seed=123)
    result = game.start_game(6)
    assert result == -1
