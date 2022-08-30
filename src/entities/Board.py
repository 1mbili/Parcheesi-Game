from Field import Field
from Pawn import Pawn
CELL_NUM = 40


class Board:

    def __init__(self, players):
        self.player_number = len(players)
        self.fields = []
        self.players = players
        for _ in range(CELL_NUM):
            self.fields.append(Field())

    def move(self, dice_result, player_turn):
        pass

red_pawn = Pawn("red")
board = Board(3)
board.fields[1].add_pawn(red_pawn)
board.fields[1].add_pawn(red_pawn)

field = board.fields[1]
for i in field.pawns:
    print(i)
print(board)
