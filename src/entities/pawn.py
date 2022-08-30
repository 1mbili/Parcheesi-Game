"""
Module for Pawn class
"""


class Pawn:
    """Class representing Parcheesi pawn"""

    def __init__(self, color: str):
        self.color = color

    def __repr__(self) -> str:
        """Return representation of a class"""
        return f"Pawn: {self.color}"

    def __str__(self) -> str:
        """Return representation of a class"""
        return f"Pawn: {self.color}"
