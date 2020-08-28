from typing import List, Dict

from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PlayerActionEnum import PlayerActionEnum
from baseball.objects.Player import Player


class Batter(Player):

    def __init__(self, name: str, positions: List[PlayerPositionEnum]):

        super().__init__(name, positions)

        # stats
        self.innings_played: float = 0.0
        self.hits: int = 0
        self.walks: int = 0
        self.hitbypitch: int = 0
        self.strikeouts: int = 0
        self.singles: int = 0
        self.doubles: int = 0
        self.triples: int = 0
        self.homeruns: int = 0

