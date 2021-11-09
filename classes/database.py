import sqlite3

from classes.config import config as Config

class Database:
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect(f"{Config.get('database', 'name')}.db")
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
    
    def execute(self, query: str) -> None:
        self.cursor.execute(query)
        self.connection.commit()

    def fetchall(self, query: str):
        self.cursor.execute(query)
        print(self.cursor.fetchall())
