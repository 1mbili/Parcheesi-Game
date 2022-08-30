import random


class Dice:

    def __init__(self, seed: int):
        random.seed = seed

    @staticmethod
    def throw():
        return random.randint(1, 6)
