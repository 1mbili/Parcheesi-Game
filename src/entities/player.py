"""
Module for Player class
"""


class Player:
    """Class for player in Parchessi"""

    def __init__(self, color, starting_point):
        self.free_pawns = 4
        self.color = color
        self.starting_point = starting_point
        self.pawns_position = [-1 for i in range(4)]

    def return_pawn(self) -> None:
        """Increase pawn number in House"""
        self.free_pawns += 1

    def rolled_start(self):
        """Remove pawn from house"""
        self.free_pawns -= 1

    def get_further_pawn(self):
        """Return index of most further pawn"""
        max_index = 0
        for position in self.pawns_position:
            if self.starting_point > position > max_index:
                max_index = position
        if max_index != 0:
            return max_index
        return max(self.starting_point)
