# lib/models/villain.py
import json
from models.__init__ import CURSOR, CONN


class Villain:

    all = {}

    def __init__(self, name, location, abilities=[], id=None):
        self.id = id
        self.name = name
        self.location = location
        self.abilities = abilities

    def __repr__(self):
        return f'<Villain {self.id}: {self.name}, {self.location}, {self.abilities}>'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string")
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str):
            self._location = location
        else:
            raise ValueError("Location must be a string")
        
    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, abilities):
        if isinstance(abilities, list):
            for ability in abilities:
                if not isinstance(ability, str):
                    raise ValueError("Each ability must be a string")
            self._abilities = abilities
        else:
            raise ValueError("Abilities must be a list of strings")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS villains (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            abilities TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS villains;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, location, abilities):
        villain = cls(name, location, abilities)
        abilities_str = json.dumps(abilities)
        sql = """
            INSERT INTO villains (name, location, abilities)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (name, location, abilities_str))
        CONN.commit()
        villain.id = CURSOR.lastrowid
        Villain.all[villain.id] = villain
        return villain
    
    def update(self):
        sql = """
            UPDATE villains
            SET name = ?, location = ?, abilities = ?
            WHERE id = ?
        """
        abilities_str = json.dumps(self.abilities)
        CURSOR.execute(sql, (self.name, self.location, abilities_str, self.id,))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM villains
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del Villain.all[self.id]
        self.id = None
