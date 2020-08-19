class Inning:

    def __init__(self):

        self.home_actions = []
        self.away_actions = []
        self.text_log = []

        # outs
        self.outs: int = 0

        # scoring
        self.home_runs = 0
        self.away_runs = 0

        # hits
        self.home_hits: int = 0
        self.away_hits: int = 0

        # errors
        self.home_errors: int = 0
        self.away_errors: int = 0
