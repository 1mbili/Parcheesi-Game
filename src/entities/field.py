"""
Module for Field class
"""
from entities.pawn import Pawn


class Field:
    """Class representing field on a board"""

    def __init__(self):
        self.pawns = []

    def add_pawn(self, new_pawn: Pawn) -> list:
        """
        Adds pawn to a field and checks other pawns
        :param new_pawn: Pawn to add to the field
        :return: list of Pawn that are in other color then added
        """
        other_pawns = []
        self.pawns = [pawn if pawn.color == new_pawn.color else other_pawns.append(pawn)
                      for pawn in self.pawns]

        self.pawns.append(new_pawn)
        return other_pawns

    def __repr__(self) -> str:
        """Probably to remove"""
        return f"{self.pawns}"

    def __str__(self) -> str:
        """Probably to remove"""
        return f"{self.pawns}"
