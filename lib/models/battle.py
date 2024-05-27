from models.__init__ import CURSOR, CONN
from models.character import Character
import json

class Battle():

    all = {}

    def __init__(self, aggressor, defender, location):
        self.aggressor = aggressor
        self.defender = defender
        self.location = location

    @property
    def aggressor(self):
        return self._aggressor
    
    @aggressor.setter
    def aggressor(self, aggressor):
        if isinstance(aggressor, Character):
            self._aggressor = aggressor
        else:
            raise ValueError("Aggressor must be an instance of the Character class")
        
    @property
    def defender(self):
        return self._defender
    
    @defender.setter
    def defender(self, defender):
        if isinstance(defender, Character):
            self._defender = defender
        else:
            raise ValueError("Defender must be an instance of the Character class")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str):
            self._location = location
        else:
            raise ValueError("Location must be a string")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS battles (
            id INTEGER PRIMARY KEY,
            aggressor TEXT,
            defender TEXT,
            location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS battles;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, aggressor, defender, location):
        battle = cls(aggressor, defender, location)
        sql = """
            INSERT INTO battles (aggressor, defender, location)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (aggressor, defender, location))
        CONN.commit()
        battle.id = CURSOR.lastrowid
        cls.all[battle.id] = battle
        return battle