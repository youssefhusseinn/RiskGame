import random

from Country import *


class USGame():

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
        c23 = Country(23)
        c24 = Country(24)
        c25 = Country(25)
        c26 = Country(26)
        c27 = Country(27)
        c28 = Country(28)
        c29 = Country(29)
        c30 = Country(30)
        c31 = Country(31)
        c32 = Country(32)
        c33 = Country(33)
        c34 = Country(34)
        c35 = Country(35)
        c36 = Country(36)
        c37 = Country(37)
        c1.neighbors = {c2, c4}
        c2.neighbors = {c1, c3, c4, c5}
        c3.neighbors = {c2, c5, c9}
        c4.neighbors = {c1, c2, c5, c6, c7, c8}
        c5.neighbors = {c2, c3, c4, c8, c9}
        c6.neighbors = {c4, c7, c10, c11}
        c7.neighbors = {c4, c6, c8, c11, c12, c13}
        c8.neighbors = {c4, c5, c7, c9, c13, c14}
        c9.neighbors = {c3, c5, c8, c13, c14}
        c10.neighbors = {c6, c11, c18}
        c11.neighbors = {c6, c7, c10, c12, c18, c19}
        c12.neighbors = {c7, c11, c13, c15, c19, c20}
        c13.neighbors = {c7, c8, c9, c12, c14, c15, c16}
        c14.neighbors = {c8, c9, c13, c16, c17}
        c15.neighbors = {c12, c13, c16, c20}
        c16.neighbors = {c13, c14, c15, c17, c20, c21}
        c17.neighbors = {c14, c16, c21, c22}
        c18.neighbors = {c10, c11, c19, c23, c24}
        c19.neighbors = {c11, c12, c18, c20, c23, c25}
        c20.neighbors = {c12, c15, c16, c19, c21, c25, c28, c32}
        c21.neighbors = {c16, c17, c20, c22, c32, c34}
        c22.neighbors = {c17, c21, c34}
        c23.neighbors = {c18, c19, c24, c25}
        c24.neighbors = {c23, c25, c26, c27}
        c25.neighbors = {c19, c20, c23, c26, c28}
        c26.neighbors = {c24, c25, c27, c28}
        c27.neighbors = {c24, c26, c28, c29}
        c28.neighbors = {c20, c25, c26, c27, c29, c31, c32}
        c29.neighbors = {c27, c28, c30}
        c30.neighbors = {c29}
        c31.neighbors = {c28, c32, c35, c36}
        c32.neighbors = {c20, c21, c28, c31, c33, c34, c35}
        c33.neighbors = {c32, c34, c35, c37}
        c34.neighbors = {c21, c22, c32, c33}
        c35.neighbors = {c31, c32, c36, c37}
        c36.neighbors = {c31, c35}
        c37.neighbors = {c33, c35}
        self.countries = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
                          c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37]

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
