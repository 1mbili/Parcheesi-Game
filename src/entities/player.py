"""
Module for Player class
"""
from src.entities.Enums import Player_starting


class Player:
    """Class for player in Parchessi"""

    def __init__(self, color):
        self.free_pawns = 4
        self.house = [0 for _ in range(4)]
        self.color = color
        self.starting_point = getattr(Player_starting, color).value
        self.pawns_position = [-1 for i in range(4)]

    def return_pawn(self, position: int) -> None:
        """
        Return pawn to hand
        :param position: position on field of the pawn
        """
        self.free_pawns += 1
        self.pawns_position.remove(position)
        self.pawns_position.append(-1)

    def has_pawns_in_hand(self):
        """Remove pawn from hand"""
        if self.free_pawns == 0:
            return 0
        self.free_pawns -= 1
        self.pawns_position.remove(-1)
        self.pawns_position.append(self.starting_point)
        return 1

    def move_pawn_loc(self, src: int, dest: int) -> None:
        """
        Change pawn position
        :param src: previous pawn position
        :param dest: actual pawn position
        """
        self.pawns_position.remove(src)
        self.pawns_position.append(dest)

    def get_selected_pawn(self, select: int) -> int:
        """
        Return n-th selected further pawn
        :param select: numer of pawn to take
        :return:index of selected pawn
        """
        indexes = self.pawns_position.copy()
        for _ in range(select):
            if (res := self.get_further_pawn()) == -2:
                return -2
            self.pawns_position.remove(res)
        self.pawns_position = indexes
        return res

    def check_selected_pawn(self, select: int) -> int:
        """
        Return n-th selected further pawn
        :param select: numer of pawn to take
        :return:index of selected pawn
        """
        indexes = self.pawns_position.copy()
        for _ in range(select):
            if (res := self.get_further_pawn()) == -2:
                return 0
        return res

    def get_further_pawn(self) -> int:
        """Return index of most further pawn"""
        max_index = -2
        for position in self.pawns_position:
            if self.starting_point > position > max_index:
                max_index = position
            elif (position >= self.starting_point or max_index == -2) and position > max_index:
                max_index = max(position, max_index)
        return max_index

    def move_in_house(self, dice_result: int) -> bool:
        """
        Checks if pawn can be moved inside house
        :param dice_result: number of fields on dice
        :return: bool if operation was possible
        """
        for i, pos in enumerate(self.house):
            if pos == 1 and i + dice_result <= 3 and self.house[i + dice_result] == 0:
                self.house[i + dice_result] = 1
                self.house[i] = 0
                return True
        return False

    def move_to_house(self, in_house_position: int, position: int) -> None:
        """
        Moves pawn to house
        :param in_house_position: position in house that pawn will go
        :param position: position of the pawn before move
        """
        self.house[in_house_position] = 1
        self.pawns_position.remove(position)

    def has_free_pawns(self) -> bool:
        """
        Check if player have pawns avalible to move
        :return: Bool if any avalible pawn exists
        """
        return len(self.pawns_position) > 0

    def __repr__(self):
        return f"Player {self.color}, positions: {self.pawns_position}, house: {self.house}, free: {self.free_pawns}\n"
