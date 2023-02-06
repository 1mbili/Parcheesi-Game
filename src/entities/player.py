"""
Module for Player class
"""
from src.entities.enums import PlayerStarting


class OutOfPawnsException(Exception):
    """
    Class for handling no pawns available to move exception
    """


class Player:
    """Class for player in Parchessi"""

    def __init__(self, color):
        self.free_pawns = 4
        self.house = [0 for _ in range(4)]
        self.color = color
        self.starting_point = getattr(PlayerStarting, color).value
        self.pawns_position = [-1 for _ in range(4)]

    def return_pawn(self, position: int) -> None:
        """
        Return pawn to hand
        :param position: position on field of the pawn
        """
        self.free_pawns += 1
        self.pawns_position.remove(position)
        self.pawns_position.append(-1)

    def pick_pawn_from_hand(self) -> int:
        """Place pawn on board"""
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

    def get_selected_furthest_pawn(self, select: int) -> int:
        """
        Return n-th selected further pawn
        :param select: numer of pawn to take
        :return:index of selected pawn
        """
        res = 0
        indexes = self.pawns_position.copy()
        for _ in range(select):
            try:
                res = self.get_further_pawn_index()
                self.pawns_position.remove(res)
            except OutOfPawnsException as err:
                raise err
        self.pawns_position = indexes
        return res

    def get_further_pawn_index(self) -> int:
        """Return index of most further pawn"""
        if not self.pawns_position:
            raise OutOfPawnsException
        max_index = self.pawns_position[0]
        for position in self.pawns_position[1:]:
            if max_index == -1 and position > -1:
                max_index = position
            elif self.starting_point > position > max_index:
                max_index = position
            elif position >= self.starting_point and self.starting_point <= max_index < position:
                max_index = position
        return max_index

    def try_move_in_house(self, dice_result: int) -> bool:
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
        Check if player have pawns available to move
        :return: Bool if any available pawn exists
        """
        return len(self.pawns_position) > 0

    def __repr__(self):
        return f"Player {self.color}, positions: {self.pawns_position}, " \
               f"house: {self.house}, free: {self.free_pawns}\n"

    def try_move_pawn_to_house(self, position, new_position):
        if position < self.starting_point <= new_position or position > new_position >= self.starting_point:
            in_house_position = new_position - self.starting_point
            if in_house_position < 4 and self.house[in_house_position] == 0:
                self.move_to_house(in_house_position, position)
                return True
        return False


