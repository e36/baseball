class Team:

    def __init__(self, name: str, abbreviation: str, year: int):

        self.name: str = name
        self.abbreviation: str = abbreviation
        self.year: int = year

        # should these be dicts instead?
        # example: {uuid: Player}
        self.pitchers = []
        self.batters = []
