# lib/models/character.py
from models.__init__ import CURSOR, CONN


class Character:

    all = {}

    def __init__(self, name, location, abilities, id=None):
        self.id = id
        self.name = name
        self.location = location
        self.abilities = abilities

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
        if isinstance(abilities, str):
            self._abilities = abilities
        else:
            raise ValueError("Abilities must be a string")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS characters (
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
            DROP TABLE IF EXISTS characters;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, name, location, abilities):
        character = cls(name, location, abilities)
        sql = """
            INSERT INTO characters (name, location, abilities)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (name, location, abilities))
        CONN.commit()
        character.id = CURSOR.lastrowid
        cls.all[character.id] = character
        return character
    
    @classmethod
    def instance_from_db(cls, row):
        character = cls.all.get(row[0])
        if character:
            character.name = row[1]
            character.location = row[2]
            character.abilities = row[3]
        else:
            character = cls(row[1], row[2], row[3], id=row[0])
            cls.all[character.id] = character
        return character
            
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM characters
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM characters
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM characters
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def update(self):
        sql = """
            UPDATE characters
            SET name = ?, location = ?, abilities = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.abilities, self.id,))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM characters
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del Character.all[self.id]
        self.id = None