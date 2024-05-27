from models.__init__ import CURSOR, CONN
from models.character import Character
import json

class Battle():

    all = {}

    def __init__(self, aggressor_id, defender_id, location):
        self.aggressor_id = aggressor_id
        self.defender_id = defender_id
        self.location = location

    @property
    def aggressor_id(self):
        return self._aggressor_id
    
    @aggressor_id.setter
    def aggressor_id(self, aggressor_id):
        character = Character.find_by_id(aggressor_id)
        if isinstance(character, Character):
            self._aggressor_id = aggressor_id
        else:
            raise ValueError("Aggressor_id must reference an instance of the Character class")
        
    @property
    def defender_id(self):
        return self._defender_id
    
    @defender_id.setter
    def defender_id(self, defender_id):
        character = Character.find_by_id(defender_id)
        if isinstance(character, Character):
            self._defender_id = defender_id
        else:
            raise ValueError("Defender_id must reference an instance of the Character class")
        
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
            aggressor_id INT,
            defender_id INT,
            location TEXT,
            victor TEXT
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
    def create(cls, aggressor_id, defender_id, location):
        battle = cls(aggressor_id, defender_id, location)
        victor = Character.who_wins(aggressor_id, defender_id)
        sql = """
            INSERT INTO battles (aggressor_id, defender_id, location, victor)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (aggressor_id, defender_id, location, victor))
        CONN.commit()
        battle.id = CURSOR.lastrowid
        cls.all[battle.id] = battle
        return battle