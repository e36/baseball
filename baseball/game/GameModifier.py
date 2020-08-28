# used to pass messages (modifiers) bacck to the game from other areas, like the field


class GameModifier:

    def __init__(self, modifier, payload):

        self.modifier = modifier
        self.payload = payload
