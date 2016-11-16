# -*- coding: utf-8 -*-
# example 1 Chapter 14 - Simple Python Objects

class PartyAnimal:

    x = 0

    def party(self):
        self.x = self.x + 1
        print 'So far', self.x

an = PartyAnimal()
an.party()
an.party()
an.party()
