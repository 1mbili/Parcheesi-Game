from Field import Field
from Pawn import Pawn
CELL_NUM = 40


class Board:

    def __init__(self, player_number):
        self.player_number = player_number
        self.fields = []
        for _ in range(CELL_NUM):
            self.fields.append(Field())


red_pawn = Pawn("red")
board = Board(3)
board.fields[1].add_pawn(red_pawn)
board.fields[1].add_pawn(red_pawn)

field = board.fields[1]
print(field)
