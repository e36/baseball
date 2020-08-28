import uuid
from typing import List, Dict
from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PlayerActionEnum import PlayerActionEnum


class Player:

    def __init__(self, name: str, positions: List[PlayerPositionEnum]):

        # each player gets a unique ID
        self.id = uuid.uuid4().int

        # player stuff
        self.name = name
        self.positions: List[PlayerPositionEnum] = positions

        # actions
        # {roll number: list of PlayerActionEnum}
        # it's a list because we could have multiple actions for a given roll, so you'd have to roll an additional die
        self.action_data: Dict[int, Dict[int, List[PlayerActionEnum]]] = dict()

    def add_action(self, first_roll: int, second_roll: int, action: PlayerActionEnum):

        # init this list if it doesn't exist
        if second_roll not in self.action_data[first_roll].keys():
            self.action_data[first_roll][second_roll] = []

        self.action_data[first_roll][second_roll].append(action)

    def get_actions(self, first_roll: int, second_roll: int) -> List[PlayerActionEnum]:

        return self.action_data[first_roll][second_roll]

