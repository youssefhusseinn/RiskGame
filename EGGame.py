import random

from Country import *


class EGGame():

    def __init__(self, agent1, agent2):
        self.agents = [agent1, agent2]
        c1 = Country(1)
        c2 = Country(2)
        c3 = Country(3)
        c4 = Country(4)
        c5 = Country(5)
        c6 = Country(6)
        c7 = Country(7)
        c8 = Country(8)
        c9 = Country(9)
        c10 = Country(10)
        c11 = Country(11)
        c12 = Country(12)
        c13 = Country(13)
        c14 = Country(14)
        c15 = Country(15)
        c16 = Country(16)
        c17 = Country(17)
        c18 = Country(18)
        c19 = Country(19)
        c20 = Country(20)
        c21 = Country(21)
        c22 = Country(22)

        c1.neighbors = {c2, c3, c7, c8}
        c2.neighbors = {c1, c3, c4, c19, c20, c21, c22}
        c3.neighbors = {c1, c2, c4, c5, c6, c7, c10, c13}
        c4.neighbors = {c2, c3, c5, c18, c19}
        c5.neighbors = {c3, c4, c6, c18}
        c6.neighbors = {c3, c5}
        c7.neighbors = {c1, c3, c8, c9, c10}
        c8.neighbors = {c1, c7}
        c9.neighbors = {c7, c10, c11}
        c10.neighbors = {c3, c7, c9, c11, c12, c13}
        c11.neighbors = {c9, c10, c12}
        c12.neighbors = {c10, c11, c13, c14, c15}
        c13.neighbors = {c3, c5, c10, c12, c15, c18}
        c14.neighbors = {c12, c15, c16}
        c15.neighbors = {c12, c13, c14, c16, c17, c18}
        c16.neighbors = {c14, c15, c17}
        c17.neighbors = {c15, c16}
        c18.neighbors = {c4, c5, c13, c15, c19, c20, c21, c22}
        c19.neighbors = {c2, c4, c18, c20}
        c20.neighbors = {c2, c18, c19, c21}
        c21.neighbors = {c2, c18, c20, c22}
        c22.neighbors = {c2, c18, c21}

        self.countries = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                          c21, c22]

    def splitCountriesFixed(self):
        for i in range(0, 11):
            self.agents[0].countries[self.countries[i]] = 1
        for i in range(11, 22):
            self.agents[1].countries[self.countries[i]] = 1
        print(self.agents[0].countries)
        print()
        print(self.agents[1].countries)

    def splitCountriesRandomly(self):

        agentcount = [0, 0]
        for country in self.countries:
            if agentcount[0] <= 11 and agentcount[1] < 11:
                x = random.choice(range(0, 2))
                self.agents[x].countries.add(country)
                agentcount[x] += 1
            elif agentcount[0] <= 11:
                self.agents[0].countries.add(country)
                agentcount[0] += 1
            else:
                self.agents[1].countries.add(country)
                agentcount[1] += 1
