"""
Module for Dice class
"""
from random import Random


class Dice:
    """Class representing dice"""

    def __init__(self, seed_num: int):
        """
        :param seed: seed for random number generator
        """
        self.random = Random(seed_num)

    def throw(self) -> int:
        """
        :return: Return number between 1 and 6
        """
        return self.random.randint(1, 6)

    def __repr__(self) -> str:
        """
        :return: Return class representation
        """
        return f"Dice seed is {self.random.seed}"
