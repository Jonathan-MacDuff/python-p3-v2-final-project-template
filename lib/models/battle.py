from models.__init__ import CURSOR, CONN
import json

class Battle():

    all = {}

    def __init__(self, hero, villain, location):
        self.hero = hero
        self.villain = villain
        self.location = location