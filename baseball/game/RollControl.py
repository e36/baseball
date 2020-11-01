import random


class RollControl:

    def __init__(self):

        self.first_roll: int = None
        self.second_roll: int = None
        self.third_roll: int = None

    def roll(self):

        self.first_roll = self.roll_first_roll()
        self.second_roll = self.roll_second_roll()
        self.third_roll = self.roll_third_roll()

        print(f"Rolling: First roll={self.first_roll}, second roll={self.second_roll}, third roll={self.third_roll}")

    def roll_first_roll(self):

        return random.randint(1, 6)

    def roll_second_roll(self):

        return random.randint(1, 6) + random.randint(1, 6)

    def roll_third_roll(self):

        return random.randint(1, 20)
