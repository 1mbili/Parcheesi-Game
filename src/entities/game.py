"""
Module for Game class
"""

from src.entities.dice import Dice
from src.entities.player import Player
from src.entities.board import Board
from src.entities.board import NoAvailablePlayerMoveException
PLAYERS = ("RED", "BLUE",  "YELLOW", "GREEN")


class EndGameException(Exception):
    """
    Class for handling end game state exception
    """


class Game:
    """Main for Game Class"""

    def __init__(self, player_num=4, seed=223):
        self.dice = Dice(seed)
        self.player_num = player_num
        self.round = 0
        players = []
        for color in PLAYERS:
            players.append(Player(color=color))
        self.board = Board(players)

    def move(self) -> None:
        """Make move in the game"""
        result = self.dice.throw()
        print(f"Throw {result}")
        try:
            self.board.update(result, self.round)
            while result == 6:
                result = self.dice.throw()
                print(f"Throw {result}")
                self.board.update(result, self.round)
        except NoAvailablePlayerMoveException as err:
            raise EndGameException("GAME ENDED") from err
        self.round += 1


def start_game(rounds_limit: int) -> int:
    """
    Starts game
    :param rounds_limit: Limit how many round game can do
    :return: Code if game finished successfully
    """
    game = Game(seed=3222)
    for i in range(rounds_limit):
        try:
            game.move()
            print(game.board)

        except EndGameException as err:
            return 0
    print(game.board)
    return -1
