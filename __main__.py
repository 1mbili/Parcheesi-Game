import sys
from src.entities.game import start_game


def main():
    """
    Starts the game
    :return:
    """
    return start_game(rounds_limit=555)


if __name__ == "__main__":
    sys.exit(main())
