from Pawn import Pawn


class Field:

    def __init__(self):
        self.pawns = []

    def add_pawn(self, new_pawn: Pawn):
        self.pawns.append(new_pawn)

    def __repr__(self):
        return f"{self.pawns}"

    def __str__(self):
        return f"{self.pawns}"

