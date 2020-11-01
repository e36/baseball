import sqlite3
from sqlite3 import Connection
from baseball.config.config import DATABASE_PATH
from baseball.objects.Player import Player
from baseball.objects.PlayerAttribute import PlayerAttribute
from baseball.objects.PlayerAction import PlayerAction
from baseball.utils.utils import convert_enum_list_to_delimited_string
from typing import Dict, List


def save_player_to_database(player: Player) -> Player:
    """
    Takes a player and saves them and their data to the database.  Returns the new player (row) id if successful.
    :param player:
    :return:
    """

    # TODO: Implement updating player information for a player that already exists.

    conn = sqlite3.connect(DATABASE_PATH)
    cur = conn.cursor()

    # check to see if the player already exists.  If they do, then return 0 for now.

    print("Inserting new player.")
    # insert the new player data
    player = insert_new_player(conn, player)

    # insert the player actions
    if len(player.action_data) > 0:
        player = insert_new_player_actions(conn, player)

    # wrap things up
    conn.commit()
    conn.close()
    return player


def insert_new_player(connection: Connection, player: Player) -> Player:
    """
    Inserts new player information into the database.  This is just the player object info.
    Call save_player_to_database to save the entire object hierarchy
    :param connection: sqlite3 connection
    :param player: Player object
    :return: New rowid or 0
    """

    cursor = connection.cursor()

    # check to see if the player already exists
    # TODO if they do, we should just load the data maybe?  How would we know that we want to do that instead of overwrite?
    p_data = (player.unique_id,)
    cursor.execute("SELECT id FROM player WHERE unique_id=?", p_data)

    retdata = cursor.fetchone()
    if retdata and len(retdata) == 1:
        print(f"Player already exists!  Found id={retdata[0]} for unique id={player.unique_id}")
        player.player_id = retdata[0]
        return player
    else:
        print(f"Inserting new player {player.unique_id} {player.first_name} {player.last_name}")
        # insert the player information
        data = (player.first_name, player.last_name, player.unique_id, player.year)
        cursor.execute("INSERT INTO player (first_name, last_name, unique_id, year) VALUES (?,?,?,?)", data)

        # get the row id
        player.player_id = cursor.lastrowid
        print(f"Assigning id={player.player_id}")

    connection.commit()

    return player


def insert_new_player_attributes(connection: Connection, player: Player):

    cursor = connection.cursor()

    attribute: PlayerAttribute

    for attribute in player.attributes:

        data = (attribute.attribute.value, attribute.value, player.player_id)

        cursor.execute("INSERT INTO player_attributes (attribute_name, attribute_value, player_id) VALUES (?,?,?)", data)

    connection.commit()

    return player


def insert_new_player_actions(connection: Connection, player_id: int, action_data: Dict[int, Dict[int, List[PlayerAction]]]):
    """
    Inserts all of the player actions
    :param connection:
    :param player_id:
    :param action_data:
    :return: Returns the player object, with player actions having new row IDs
    """

    # TODO handle updating existing action data.  Right now this is assuming new data only

    cursor = connection.cursor()

    action: PlayerAction = None

    for action_main_roll in action_data.keys():
        for action_second_roll in action_data[action_main_roll].keys():
            for action in action_data[action_main_roll][action_second_roll]:

                # skip if we have an action_id, it implies that it's in the db already
                if action.action_id != 0:
                    continue

                modifier_string = convert_enum_list_to_delimited_string(action.modifiers)
                data = (player_id, action.first_roll, action.second_roll, action.third_roll_start,
                        action.third_roll_end, action.action_type.value, action.target.value, modifier_string)
                cursor.execute("""INSERT INTO player_actions (player_id, first_roll, second_roll, third_roll_start, third_roll_end,
                                action_type, target, modifiers) VALUES (?,?,?,?,?,?,?,?)""", data)

                # save the row id to the action
                action.action_id = cursor.lastrowid

    connection.commit()

    return True
