import json
from baseball.objects.Team import Team


def write_team(filename: str, team: Team):
    """
    Creates a big JSON thing to be written to a file
    :param filename:
    :param team:
    :return:
    """

    json_dict = dict()

    # initial data
    json_dict['team'] = {
        'name': team.name,
        'abbreviation': team.abbreviation,
        'year': team.year,
        'players': []
    }

    # loop through
    for pitcher in team.pitchers:
        pass

    for batter in team.batters:
        pass