# -*- coding: utf-8 -*-
# Inheritance example

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print self.name, "constructed"

    def party(self):
        self.x = self.x+1
        print self.name, "party count", self.x

class FootballFan(PartyAnimal):
    point = 0
    def touchdown(self):
        self.points = self.point+7
        self.party()
        print self.name, "points", self.points

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()

