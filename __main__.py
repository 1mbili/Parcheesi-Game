import sys
from src.entities.game import Game


def main():
    """
    Starts the game
    :return:
    """
    return Game.start_game(rounds_limit=555)


if __name__ == "__main__":
    sys.exit(main())
