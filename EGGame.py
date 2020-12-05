import random

from Country import *
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)

class EGGame():
    attack =[]

    def __init__(self):
        ## self.agents = [agent1, agent2]
        """"


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
    """


    def attacking(self):
        self.attack[0].label = "10"
        self.attack[0].color = DARKRED
        self.attack[1].label = "5"
        self.attack[1].color = DARKBLUE


    def addelements(self, country):
        if country not in self.attack:
            self.attack.append(country)
        else:
            return    
        if len(self.attack) == 2:
            self.attacking()
        if len(self.attack) >= 2:
            self.attack.clear()
