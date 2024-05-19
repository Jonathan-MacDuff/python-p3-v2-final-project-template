#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.hero import Hero

def reset_database():
    Hero.drop_table()
    Hero.create_table()

    Hero.create("Deadpool", "Earth", ["Healing Factor", "Ninja Skills"])
    Hero.create("Spider-Man", "Manhattan", ["Strength", "Webbing", "Agility"])
    Hero.create("Daredevil", "Manhattan", ["Senses"])

reset_database()
ipdb.set_trace()
