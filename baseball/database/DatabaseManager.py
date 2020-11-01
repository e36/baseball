import sqlite3
from baseball.config.config import DATABASE_PATH
from sqlite3 import Cursor, Connection


class DatabaseManager:

    def __init__(self):

        self.connection: Connection = sqlite3.connect(DATABASE_PATH)
        self.cursor: Cursor = self.connection.cursor()

    def connect(self):

        self.connection = sqlite3.connect(DATABASE_PATH)

    def get_cursor(self):

        self.cursor = self.connection.cursor()

    def commit(self):

        self.connection.commit()

    def close(self):

        self.connection.close()

