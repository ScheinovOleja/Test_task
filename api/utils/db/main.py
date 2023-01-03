import sqlite3

from api.data.config import db_path


class Database:
    def __init__(self):
        self.db_file = db_path
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
