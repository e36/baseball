from baseball.objects.Team import Team
from baseball.objects.Inning import Inning
from typing import Dict


class Game:

    def __init__(self, hometeam: Team, awayteam: Team):

        # innings
        self.current_inning: int = 0

        # we can use this for a while game_active to keep the game going
        self.game_active = False

        # scoring
        self.home_runs = 0
        self.away_runs = 0

        # hits
        self.home_hits: int = 0
        self.away_hits: int = 0

        # errors
        self.home_errors: int = 0
        self.away_errors: int = 0

        # team stuff
        self.home_team: Team = hometeam
        self.away_team: Team = awayteam

        # inning data {inning number: Inning()}
        self.innings: Dict[int, Inning] = dict()

    def start(self):

        self.game_active = True

        print("Play Ball!")

    def new_inning(self):

        self.current_inning += 1
        self.innings[self.current_inning] = Inning()

    def get_current_inning(self) -> Inning:

        return self.innings[self.current_inning]

    def play_inning(self):

        inning: Inning = self.get_current_inning()

        
