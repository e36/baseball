import uuid
from typing import List, Dict, Optional
from baseball.objects.PlayerAttribute import PlayerAttribute
from baseball.objects.PlayerAction import PlayerAction


class Player:

    def __init__(self, first_name: str, last_name: str, player_id: int=0, unique_id: str='', year: int=0):

        # db row id
        self.player_id = player_id

        # unique UUID to keep track of players of different years and teams
        self.unique_id = unique_id

        # player stuff
        self.first_name = first_name
        self.last_name = last_name
        self.year: int = year

        # position and other attribute info, like bunting
        self.attributes: List[PlayerAttribute] = []

        # actions
        # {roll number: list of PlayerActionEnum}
        # it's a list because we could have multiple actions for a given roll, so you'd have to roll an additional die
        self.action_data: Dict[int, Dict[int, List[PlayerAction]]] = dict()

    def generate_unique_id(self):
        """
        We might not need a unique uuid if we're using database rows, but hang onto this for now
        :return:
        """

        self.unique_id = uuid.uuid4().hex

    def add_action(self, first_roll: int, action: PlayerAction):

        # look for the first roll list
        if first_roll not in self.action_data.keys():
            self.action_data[first_roll] = dict()

        # init this list if it doesn't exist
        if action.second_roll not in self.action_data[first_roll].keys():
            self.action_data[first_roll][action.second_roll] = []

        action.first_roll = first_roll

        self.action_data[first_roll][action.second_roll].append(action)

    def get_actions(self, first_roll: int, second_roll: int, third_roll: int=0) -> Optional[PlayerAction]:
        """
        Looks for an action based on
        :param first_roll:
        :param second_roll:
        :param third_roll:
        :return:
        """

        alist = self.action_data[first_roll][second_roll]

        # if there are more than one then we need to look at the third roll
        if len(alist) > 1:
            for action in alist:
                if action.is_within_third_roll(third_roll):
                    return action
        elif len(alist) == 1:
            return alist[0]
        else:
            return None


