from models.__init__ import CURSOR, CONN
from models.character import Character

class Battle():

    def __init__(self, aggressor_id, defender_id, location, id=None):
        self.id = id
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
            raise ValueError("Aggressor must be an existing Character")
        
    @property
    def defender_id(self):
        return self._defender_id
    
    @defender_id.setter
    def defender_id(self, defender_id):
        character = Character.find_by_id(defender_id)
        if isinstance(character, Character):
            self._defender_id = defender_id
        else:
            raise ValueError("Defender must be an existing Character")
        
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
    def create(cls, aggressor_id, defender_id, location):
        sql = """
            INSERT INTO battles (aggressor_id, defender_id, location)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (aggressor_id, defender_id, location))
        CONN.commit()
        id = CURSOR.lastrowid
        return cls.find_by_id(id)
    
    @classmethod
    def instance_from_db(cls, row):
        return cls(row[1], row[2], row[3], id=row[0])
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM battles
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM battles
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update(self):
        sql = """
            UPDATE battles
            SET aggressor_id = ?, defender_id = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.aggressor_id, self.defender_id, self.location, self.id,))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM battles
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None
