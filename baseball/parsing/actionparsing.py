from baseball.enums.PlayerActionEnum import PlayerActionEnum
from baseball.enums.PlayerPositionEnum import PlayerPositionEnum
from baseball.enums.PlayModifierEnum import PlayModifierEnum
from baseball.objects.PlayerAction import PlayerAction
from baseball.config.constants import FIELD_POSITIONS_PLAYERPOSITIONENUM
import re
"""
For parsing card information
"""


def parse_card_action(card_action: str) -> PlayerAction:

    # this is the action that will be returned
    action = PlayerAction(card_action.upper())

    # find the main roll
    action = get_main_roll(action)

    # find out if the string contains any of the allowed actions
    action = get_main_play_action(action)

    # get a target position, if there is one
    action = get_position_in_parentheses(action)

    # get any modifiers
    action = get_modifiers(action)

    # get any secondary roll info
    action = get_third_roll(action)

    return action


def get_main_roll(action: PlayerAction) -> PlayerAction:
    """
    Gets the initial roll: e.g., 12-Flyout(RF) will return 12
    Return 0 if nothing
    :param action:
    :return:
    """

    # get roll number
    pattern = re.compile(r'^\d*-')
    match = pattern.search(action.action_text)
    if match:
        # save the roll information, and remove that substring from the text
        match_text = match.group()
        action.second_roll = int(match_text.replace('-', ''))
        action.action_text = action.action_text[:match.start()] + action.action_text[match.end():]
        print(f"Found roll {action.second_roll}")
    else:
        # action.isvalid = False
        # action.main_roll = 0
        # we don't necessarily want to invalidate this, we may need to set this independently, like
        # in the case of multiple options for a given roll
        print("No roll information found.")

    return action


def get_main_play_action(action: PlayerAction) -> PlayerAction:
    """
    Gets the main play, e.g., FLYOUT or SINGLE
    :param action:
    :return:
    """

    print("Searching for main play")

    # find out if the string contains any of the allowed actions
    for i in PlayerActionEnum:
        if i.value in action.action_text:
            print(f"\tFound {i.value}!")
            action.action_type = i
            action.action_text = action.action_text.replace(i.value, '')
            break

    return action


def get_position_in_parentheses(action: PlayerAction) -> PlayerAction:
    """
    Looks for a position in parentheses
    Ex: 10-GROUNDBALL(SS)A will return PlayerPositionEnum.ShortStop
    :param action:
    :return:
    """

    print('Searching for target position')

    # return value
    ret_enum = PlayerPositionEnum.Null

    pattern = re.compile('\(\w+\)')
    match = pattern.search(action.action_text)
    if match:
        # look in field positions list, and match them up with PlayerPositionEnum
        # strip out the parentheses
        match_text = match.group()
        print(f"\tFound position {match_text}")
        match_text = match_text.strip('(')
        match_text = match_text.strip(')')
        if match_text in FIELD_POSITIONS_PLAYERPOSITIONENUM.keys():
            action.target = FIELD_POSITIONS_PLAYERPOSITIONENUM[match_text]
            action.action_text = action.action_text.replace(f'({match_text})', '')

    return action


def get_modifiers(action: PlayerAction) -> PlayerAction:
    """
    Looks for modifiers, like *, **, and WITH INJURY
    :param action:
    :return:
    """
    print("Searching for modifiers")
    print(action.action_text)

    action.modifiers = []

    # now loop through the rest
    for modifier in PlayModifierEnum:
        if modifier.value in action.action_text:
            print(f"\tAdding modifier: {modifier}")
            action.modifiers.append(modifier)
            action.action_text = action.action_text.replace(modifier.value, '')
            print(action.action_text)

    return action


def get_third_roll(action: PlayerAction) -> PlayerAction:
    """
    Looks for a third roll, in the case where there could be multiple actions:
    e.g., 10- TRIPLE 1-4 DOUBLE 5-20
    :param action:
    :return:
    """

    print("Looking for third roll information")

    pattern = re.compile('\d+-\d+')
    match = pattern.search(action.action_text)

    # if we've got something
    if match:
        match_text = match.group()
        print(f'\tFound {match_text}')

        # it's always going to be x-x, so split along the hyphen
        rolls = match_text.split('-')
        action.third_roll_start = int(rolls[0])
        action.third_roll_end = int(rolls[1])

    return action
