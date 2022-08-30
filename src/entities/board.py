from entities.field import Field
CELL_NUM = 40


class Board:

    def __init__(self, players):
        self.player_number = len(players)
        self.fields = []
        self.players = players
        for _ in range(CELL_NUM):
            self.fields.append(Field())

    def move(self, dice_result, player_turn):
        pass

