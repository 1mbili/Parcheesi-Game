class Player:

    def __init__(self, color, starting_point):
        self.free_pawns = 4
        self.color = color
        self.starting_point = starting_point

    def return_pawn(self):
        self.free_pawns += 1

    def rolled_start(self):
        self.free_pawns -= 1
