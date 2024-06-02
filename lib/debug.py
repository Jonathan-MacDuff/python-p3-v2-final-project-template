#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.character import Character
from models.battle import Battle

def reset_database():
    Character.drop_table()
    Character.create_table()
    Battle.drop_table()
    Battle.create_table()

    Character.create("Deadpool", "Earth", "Healing Factor, Ninja Skills")
    Character.create("Spider-Man", "Manhattan", "Strength, Webbing, Agility")
    Character.create("Daredevil", "Manhattan", "Senses")
    Battle.create(1, 2, "Manhattan")
    Battle.create(1, 3, "Manhattan")

reset_database()
ipdb.set_trace()
