"""
Module for Game class
"""
from entities.dice import Dice
from entities.player import Player
from entities.board import Board

PLAYERS = {"Red": 0,
           "Blue": 10,
           "Yellow": 20,
           "Green": 30
           }


class Game:
    """Main for Game Class"""

    def __init__(self, player_num=4, seed=223):
        self.dice = Dice(seed)
        self.player_num = player_num
        self.round = 0
        players = []
        for key, item in PLAYERS.items():
            players.append(Player(color=key, starting_point=item))
        self.board = Board(players)

    def move(self) -> None:
        """Make move in the game"""
        result = self.dice.throw()
        self.board.update(result, self.round)
        while result == 6:
            result = self.dice.throw()
            self.board.update(result, self.round)
        self.round += 1


if __name__ == "__main__":
    game = Game(seed=123)
    for i in range(506):
        print(i)
        if i == 209:
            print(i == 27)
        game.move()
    print(game.board)
