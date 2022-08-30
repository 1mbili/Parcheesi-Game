"""
Module for Dice class
"""
import random


class Dice:
    """Class representing dice"""

    def __init__(self, seed: int):
        """
        :param seed: seed for random number generator
        """
        random.seed = seed
        self.seed = seed

    @staticmethod
    def throw() -> int:
        """
        :return: Return number between 1 and 6
        """
        return random.randint(1, 6)

    def __repr__(self) -> str:
        """
        :return: Return class representation
        """
        return f"Dice seed is {self.seed}"
