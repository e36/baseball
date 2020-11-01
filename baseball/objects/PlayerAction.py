from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PlayerActionEnum import PlayerActionEnum
from baseball.enums.PlayModifierEnum import PlayModifierEnum
from typing import List


class PlayerAction:

    def __init__(self, action_text: str='', action_id: int= 0):

        self.action_text = action_text

        # if there is an id from an already existing action
        self.action_id = action_id

        self.action_type: PlayerActionEnum = PlayerActionEnum.NULL
        self.target: PlayerPositionEnum = PlayerPositionEnum.Null
        self.modifiers: List[PlayModifierEnum] = []

        # main player roll to get to this action or actions
        self.first_roll: int = 0

        # this is the main roll number for the action
        self.second_roll: int = 0

        # these will be used if there are multiple actions for a given roll
        self.third_roll_start: int = 0
        self.third_roll_end: int = 0

    def is_within_third_roll(self, roll: int) -> bool:
        """
        If roll_start != 0 and roll_end != 0, and roll_start <= roll <= roll_end, then return true
        Otherwise return false
        :param roll:
        :return:
        """

        retval: bool = False

        if (self.third_roll_start > 0) and (self.third_roll_end > 0):
            if self.third_roll_start < self.third_roll_end:
                if (self.third_roll_start <= roll) and (roll <= self.third_roll_end):
                    retval = True

        return retval

    def __str__(self):
        return f"PlayerAction: rolls: {self.first_roll}|{self.second_roll}|{self.third_roll_start} - " \
               f"{self.third_roll_end}, action: {self.action_type.value}, target: {self.target.value}," \
               f"modifiers: {self.modifiers}"
