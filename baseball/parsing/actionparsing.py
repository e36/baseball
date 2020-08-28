from baseball.enums.PlayerActionEnum import PlayerActionEnum
"""
For parsing card information
"""


def parse_card_action(text: str):

    # convert to lower
    text = text.lower()

    # find out if the string contains any of the allowed actions
    for i in PlayerActionEnum.__members__.values():
        if i.value in text:
            print(f"{i.value} exists in {text}!")
            break
