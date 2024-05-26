#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.character import Character

def reset_database():
    Character.drop_table()
    Character.create_table()

    Character.create("Deadpool", "Earth", ["Healing Factor", "Ninja Skills"])
    Character.create("Spider-Man", "Manhattan", ["Strength", "Webbing", "Agility"])
    Character.create("Daredevil", "Manhattan", ["Senses"])

reset_database()
ipdb.set_trace()
