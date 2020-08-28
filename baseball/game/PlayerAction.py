from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PlayerActionEnum import PlayerActionEnum
from baseball.enums.PlayModifierEnum import PlayModifierEnum
from typing import List


class PlayerAction:

    def __init__(self, playaction: PlayerActionEnum, target: PlayerPositionEnum):

        self.action_type: PlayerActionEnum = playaction
        self.target: PlayerPositionEnum = target
        self.modifiers: List[PlayModifierEnum] = []

        # these will be used if there are multiple actions for a given roll
        self.roll_start: int = 0
        self.roll_end: int = 0
