from baseball.objects.LineUp import LineUp
from baseball.objects.Player import Player
from typing import Dict, List


class Team:

    def __init__(self, name: str, abbreviation: str, year: int):

        self.name: str = name
        self.abbreviation: str = abbreviation
        self.year: int = year

        # should these be dicts instead?
        # example: {uuid: Player}
        self.players: Dict[int, Player] = []

        # these lists will keep track of which users are pitchers and batters
        # we'll store the player id here
        self.pitchers: List[int] = []
        self.batters: List[int] = []

        # lineup
        self.lineup: LineUp = None

