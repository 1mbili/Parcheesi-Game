"""
Module for Board class
"""
from entities.field import Field
from entities.pawn import Pawn
from entities.player import Player
CELL_NUM = 40


class Board:
    """Main Class representing Parcheesi board"""

    def __init__(self, players):
        """
        :param players: Dict containing {player: starting_point}
        """
        self.player_number = len(players)
        self.fields = [Field() for _ in range(CELL_NUM)]
        self.players = players

    def update(self, dice_result, player_turn) -> None:
        """
        Method representing one player move
        :param dice_result: Number thrown by the dice
        :param player_turn: Number of the player
        """
        active_player = self.players[player_turn]
        pawn_position = active_player.get_further_pawn()
        if pawn_position == -1:
            if dice_result in [1, 6]:
                pawn = Pawn(color=active_player.color)
                other_pawns = self.fields[active_player.starting_position].move_pawn(pawn)
                self.fix_pawns_in_home(other_pawns)
        else:
            self.move_pawn(pawn_position, active_player, dice_result)

    def move_pawn(self, position: int, player: Player, to_move: int) -> None:
        """
        Moves pawn in the Field
        :param position: position of the pawn
        :param player: player which is the move
        :param to_move: number of points from dice
        """
        self.fields[position].take_pawn(player.color)
        pawn = Pawn(color=player.color)
        new_position = (position + to_move) % 40
        if position < player.starting_point <= new_position or position > new_position > player.starting_point:
            in_house_position = new_position - player.starting_point
            if in_house_position < 4 and player.house[in_house_position] == 0:
                player.house[in_house_position] = 1
            else:
                self.fields[position].move_pawn(pawn)
        else:
            pawn = Pawn(color=player.color)
            other_pawns = self.fields[new_position].move_pawn(pawn)
        self.fix_pawns_in_home(other_pawns)

    def fix_pawns_in_home(self, pawns) -> None:
        """
        Adds beaten pawns to players House:
        :param pawns: list of beaten pawns
        """
        for pawn in pawns:
            color = pawn.color
            self.players[color].return_pawn()

    def __repr__(self) -> str:
        """
        :return: fields of board representation
        """
        result_str = ""
        for i, j in enumerate(self.fields):
            result_str += f"Field nr. {i}: {j}\n"
        return result_str
