"""
Module for Game class
"""
from entities.dice import Dice
from entities.player import Player
from entities.board import Board
from entities.pawn import Pawn
PLAYERS = {"Red": 0,
           "Blue": 10,
           "Yellow": 20,
           "Green": 30
           }


class Game:
    """Main for Game Class"""

    def __init__(self, player_num=4):
        self.dice = Dice(223)
        self.player_num = player_num
        self.player_round = 0
        players = []
        for key, item in PLAYERS.items():
            players.append(Player(color=key, starting_point=item))
        self.board = Board(players)

    def move(self) -> None:
        """Make move in the game"""
        result = self.dice.throw()
        self.board.update(result, self.player_round)
        while result == 6:
            result = self.dice.throw()
            self.board.update(result, self.player_round)

        self.player_round = (self.player_round + 1) % 4


board = Board(PLAYERS)
red_pawn = Pawn("red")
board.fields[1].move_pawn(red_pawn)
board.fields[1].move_pawn(red_pawn)
field = board.fields[1]
for i in field.pawns:
    print(i)
print(board)
