from models.__init__ import CURSOR, CONN
import json

class Battle():

    all = {}

    def __init__(self, aggressor, defender, location):
        self.aggressor = aggressor
        self.defender = defender
        self.location = location