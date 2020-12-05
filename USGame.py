import random

from Country import *

DARKRED=(229,12,22)
DARKBLUE=(2,8,126)

class USGame():
    attack =[]


    def __init__(self):
       ## self.agents = [agent1, agent2]
       """"

    def splitCountriesFixed(self):
        for i in range(0, 19):
            self.agents[0].countries[self.countries[i]] = 1
        for i in range(19, 37):
            self.agents[1].countries[self.countries[i]] = 1
        print(self.agents[0].countries)
        print()
        print(self.agents[1].countries)

    def splitCountriesRandomly(self):
        agentcount = [0, 0]
        for country in self.countries:
            if agentcount[0] <= 19 and agentcount[1] < 19:
                x = random.choice(range(0, 2))
                self.agents[x].countries.add(country)
                agentcount[x] += 1
            elif agentcount[0] < 19:
                self.agents[0].countries.add(country)
                agentcount[0] += 1
            else:
                self.agents[1].countries.add(country)
                agentcount[1] += 1


"""
    def attacking(self):
        self.attack[0].label="10"
        self.attack[0].color=DARKRED
        self.attack[1].label="5"
        self.attack[1].color=DARKBLUE


    def addelements(self,country):
        self.attack.append(country)
        if len(self.attack) ==2:
            self.attacking()
        if len(self.attack)>=2:
            self.attack.clear()

# map = {
#         1: [2, 4],
#         2: [1, 3, 4, 5],
#         3: [2, 5, 9],
#         4: [1, 2, 5, 6, 7, 8],
#         5: [2, 3, 4, 8, 9],
#         6: [4, 7, 10, 11],
#         7: [4, 6, 8, 11, 12, 13],
#         8: [4, 5, 7, 9, 13, 14],
#         9: [3, 5, 8, 13, 14],
#         10: [6, 11, 18],
#         11: [c6, c7, c10, c12, c18, c19],
#         12: [c7, c11, c13, c15, c19, c20],
#         13: [c7, c8, c9, c12, c14, c15, c16],
#         14: [c8, c9, c13, c16, c17],
#         15: [c12, c13, c16, c20],
#         16: [c13, c14, c15, c17, c20, c21],
#         17: [c14, c16, c21, c22],
#         18: [c10, c11, c19, c23, c24],
#         19: [c11, c12, c18, c20, c23, c25],
#         20: [c12, c15, c16, c19, c21, c25, c28, c32],
#         21: [c16, c17, c20, c22, c32, c34],
#         22: [c17, c21, c34],
#         23: [c18, c19, c24, c25],
#         24: [c23, c25, c26, c27],
#         25: [c19, c20, c23, c26, c28],
#         26: [c24, c25, c27, c28],
#         27: [c24, c26, c28, c29],
#         28: [c20, c25, c26, c27, c29, c31, c32],
#         29: [c27, c28, c30],
#         30: [c29],
#         31: [c28, c32, c35, c36],
#         32: [c20, c21, c28, c31, c33, c34, c35],
#         33: [c32, c34, c35, c37],
#         34: [c21, c22, c32, c33],
#         35: [c31, c32, c36, c37],
#         36: [c31, c35],
#         37: [c33, c35]
#     }
