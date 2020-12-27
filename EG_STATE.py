import random
from AgressiveAgent import *

BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)
import Country
from Country import *
import Agent
from Agent import *
import Human
from Human import *


class EG_STATE:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    c1 = Country("eg1")
    c2 = Country("eg2")
    c3 = Country("eg3")
    c4 = Country("eg4")
    c5 = Country("eg5")
    c6 = Country("eg6")
    c7 = Country("eg7")
    c8 = Country("eg8")
    c9 = Country("eg9")
    c10 = Country("eg10")
    c11 = Country("eg11")
    c12 = Country("eg12")
    c13 = Country("eg13")
    c14 = Country("eg14")
    c15 = Country("eg15")
    c16 = Country("eg16")
    c17 = Country("eg17")
    c18 = Country("eg18")
    c19 = Country("eg19")
    c20 = Country("eg20")
    c21 = Country("eg21")
    c22 = Country("eg22")
    c1.neighbors = [c2, c3, c7, c8]
    c2.neighbors = [c1, c3, c4, c19, c20, c21, c22]
    c3.neighbors = [c1, c2, c4, c5, c6, c7, c10, c13]
    c4.neighbors = [c2, c3, c5, c18, c19]
    c5.neighbors = [c3, c4, c6, c18]
    c6.neighbors = [c3, c5]
    c7.neighbors = [c1, c3, c8, c9, c10]
    c8.neighbors = [c1, c7]
    c9.neighbors = [c7, c10, c11]
    c10.neighbors = [c3, c7, c9, c11, c12, c13]
    c11.neighbors = [c9, c10, c12]
    c12.neighbors = [c10, c11, c13, c14, c15]
    c13.neighbors = [c3, c5, c10, c12, c15, c18]
    c14.neighbors = [c12, c15, c16]
    c15.neighbors = [c12, c13, c14, c16, c17, c18]
    c16.neighbors = [c14, c15, c17]
    c17.neighbors = [c15, c16]
    c18.neighbors = [c4, c5, c13, c15, c19, c20, c21, c22]
    c19.neighbors = [c2, c4, c18, c20]
    c20.neighbors = [c2, c18, c19, c21]
    c21.neighbors = [c2, c18, c20, c22]
    c22.neighbors = [c2, c18, c21]
    amountofattackingtroops = 0

    attackingCountries = []  # carry the attaching to and from country

    turn = False  # false for agent 1  -----------    true for agent 2
    countries = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
                 c11, c12, c13, c14, c15, c16, c17, c18,
                 c19, c20, c21, c22
                ]

    def addToCurrentCountries(self, country):
        if country not in self.attackingCountries:
            self.attackingCountries.append(country)
        if len(self.attackingCountries) == 2:
            if (not self.turn and self.agent1.type == "HUMAN") or (self.turn and self.agent2.type == "HUMAN"):
                self.updateStatehuman()
        if len(self.attackingCountries) >= 2:
            self.attackingCountries.clear()

    def doAttack(self):
        if (not self.turn and self.agent1.type != "HUMAN") or (self.turn and self.agent2.type != "HUMAN"):
            self.updateStateAI()

    def initializeState(self):

        available_countries = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9,
                               self.c10,
                               self.c11, self.c12, self.c13, self.c14, self.c15, self.c16, self.c17, self.c18, self.c19,
                               self.c20, self.c21, self.c22]
        redTroops = 20
        blueTroops = 20

        canAddRed = True
        canAddBlue = True

        while canAddRed or canAddBlue:
            # redTroops
            if canAddRed:
                if available_countries.__len__() != 0:
                    country = random.choice(available_countries)
                    available_countries.remove(country)
                    country.owner = self.agent1
                    self.agent1.addCountry(country)
                    redTroops -= 1
                else:
                    country = random.choice(self.agent1.countries)
                    redTroops -= 1
                country.addTroops(1)
                if redTroops == 0:
                    canAddRed = False
            # blueTroops
            if canAddBlue:

                if available_countries.__len__() != 0:
                    country = random.choice(available_countries)
                    available_countries.remove(country)
                    country.owner = self.agent2
                    self.agent2.addCountry(country)
                    blueTroops -= 1
                else:
                    country = random.choice(self.agent2.countries)
                    blueTroops -= 1
                country.addTroops(1)
                if blueTroops == 0:
                    canAddBlue = False

    def updateStateAI(self):
        if (self.turn and (self.agent2.type == "MINIMAX" or self.agent2.type == "ASTAR")):
            self.agent2.takeTurn(self.countries)
            self.turn = False
            self.checkEndGame()


        elif (not self.turn and (self.agent1.type == "MINIMAX" or self.agent1.type == "ASTAR")):
            self.agent1.takeTurn(self.countries)
            self.turn = True
            self.checkEndGame()


        elif self.turn:
            self.agent2.takeTurn()
            self.turn = False
            self.checkEndGame()



        else:
            self.agent1.takeTurn()
            self.turn = True
            self.checkEndGame()

    def updateStatehuman(self):
        if self.turn:
            self.agent2.bonusTroops = self.agent2.calcBonusTroops()
            if self.agent2.attack(self.attackingCountries[0], self.attackingCountries[1], self.amountofattackingtroops):
                self.turn = False
                self.checkEndGame()
            else:
                ctypes.windll.user32.MessageBoxW(0, "PLEASE SELECT VALID ATTACK !", 1)
                self.agent2.bonusTroops = 0


        else:
            self.agent1.bonusTroops = self.agent1.calcBonusTroops()
            if self.agent1.attack(self.attackingCountries[0], self.attackingCountries[1],
                                  int(self.amountofattackingtroops)):
                self.turn = True
                self.checkEndGame()
            else:
                ctypes.windll.user32.MessageBoxW(0, "PLEASE SELECT VALID ATTACK !", 1)
                self.agent1.bonusTroops = 0

    def checkEndGame(self):
        if len(self.agent1.countries) == 0:
            ctypes.windll.user32.MessageBoxW(0, "PLAYER 2 WINS", "ALERT", 1)
            self.restart()
        if len(self.agent2.countries) == 0:
            ctypes.windll.user32.MessageBoxW(0, "PLAYER 1 WINS", "ALERT", 1)
            self.restart()

    def restart(self):
        for c in self.agent1.countries:
            c.numOfTroops = 0
        for c in self.agent2.countries:
            c.numOfTroops = 0
        self.agent1.countries.clear()
        self.agent2.countries.clear()
        self.agent1.bonusTroops = 0
        self.agent2.bonusTroops = 0

        self = EG_STATE(self.agent1, self.agent2)
        self.initializeState()
