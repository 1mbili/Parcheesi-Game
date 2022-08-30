"""
Module for Board class
"""
from entities.field import Field
from entities.pawn import Pawn

CELL_NUM = 40


class Board:
    """Main Class representing Parcheesi board"""

    def __init__(self, players):
        """
        :param players: Dict containing {player: starting_point} -> {str: int}
        """
        self.player_number = len(players)
        self.fields = []
        self.players = players
        for _ in range(CELL_NUM):
            self.fields.append(Field())

    def update(self, dice_result, player_turn) -> None:
        """
        Method representing one player move
        :param dice_result: Number thrown by the dice
        :param player_turn: Number of the player
        """
        active_player = self.players[player_turn]
        if (pawn_position := active_player.get_further_pawn()) == -1:
            if dice_result not in [1, 6]:
                return
            pawn = Pawn(color=active_player.color)
            other_pawns = self.fields[active_player.starting_position].add_pawn(pawn)
            self.fix_pawns_in_home(other_pawns)

    def fix_pawns_in_home(self, pawns) -> None:
        """
        Adds beaten pawns to players House:
        :param pawns: list of beaten pawns
        """
        for pawn in pawns:
            color = pawn.color
            self.players[color].return_pawn()
