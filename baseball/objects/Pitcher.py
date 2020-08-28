from typing import List, Dict

from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PitcherTypeEnum import PitcherTypeEnum
from baseball.enums.PlayerActionEnum import PlayerActionEnum
from baseball.objects.Player import Player


class Pitcher(Player):

    def __init__(self, name: str, positions: List[PlayerPositionEnum], pitcher_type: List[PitcherTypeEnum]):

        super().__init__(name, positions)

        # stats
        self.innings_pitched: float = 0.0
        self.strikes: int = 0
        self.balls: int = 0
        self.walks: int = 0
        self.hits: int = 0

        # starter or relief pitcher, or both
        self.pitcher_type: List[PitcherTypeEnum] = pitcher_type

