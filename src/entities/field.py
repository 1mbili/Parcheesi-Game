"""
Module for Field class
"""
from entities.pawn import Pawn


class NoPawnFoundException(Exception):
    """
    Exception for no pawn in field
    """


class Field:
    """Class representing field on a board"""

    def __init__(self):
        self.pawns = []

    def take_pawn(self, color: str) -> Pawn:
        """
        Remove pawn from Field
        :return: Pawn from field
        """
        print(self.pawns)
        if self.pawns and self.pawns[-1].color == color:
            return self.pawns.pop()
        raise NoPawnFoundException(f"No {color} pawns on the field")

    def move_pawn(self, new_pawn: Pawn) -> list:
        """
        Adds pawn to a field and checks other pawns
        :param new_pawn: Pawn to add to the field
        :return: list of Pawn that are in other color then added
        """
        other_pawns = []
        for pawn in self.pawns:
            if pawn.color != new_pawn.color:
                self.pawns.remove(pawn)
                other_pawns.append(pawn)
        self.pawns.append(new_pawn)
        return other_pawns

    def __repr__(self) -> str:
        """Field representation"""
        return f"{self.pawns}"

