import random
from  AgressiveAgent import *
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
class US_STATE:
    def __init__(self,agent1,agent2):
        self.agent1 = agent1
        self.agent2 = agent2
    c1 = Country("us1")
    c2 = Country( "us2")
    c3 = Country( "us3")
    c4 = Country("us4")
    c5 = Country("us5")
    c6 = Country("us6")
    c7 = Country("us7")
    c8 = Country("us8")
    c9 = Country("us9")
    c10 = Country("us10")
    c11 = Country("us11")
    c12 = Country("us12")
    c13 = Country("us13")
    c14 = Country("us14")
    c15 = Country("us15")
    c16 = Country("us16")
    c17 = Country("us17")
    c18 = Country("us18")
    c19 = Country("us19")
    c20 = Country("us20")
    c21 = Country("us21")
    c22 = Country("us22")
    c23 = Country("us23")
    c24 = Country("us24")
    c25 = Country("us25")
    c26 = Country("us26")
    c27 = Country("us27")
    c28 = Country("us28")
    c29 = Country("us29")
    c30 = Country("us30")
    c31 = Country("us31")
    c32 = Country("us32")
    c33 = Country("us33")
    c34 = Country("us34")
    c35 = Country("us35")
    c36 = Country("us36")
    c37 = Country("us37")
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
    amountofattackingtroops=0


    attackingCountries=[]  # carry the attaching to and from country

    turn=False   #false for agent 1  -----------    true for agent 2
    countries=[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10,
               c11, c12, c13, c14, c15,c16,c17, c18,
               c19, c20, c21, c22, c23, c24, c25, c26,
               c27, c28, c29,c30, c31,c32, c33, c34, c35, c36, c37]



    def addToCurrentCountries(self,country):
        if country not in self.attackingCountries:
            self.attackingCountries.append(country)
        if len(self.attackingCountries) ==2:
            print(self.attackingCountries)
            if (not self.turn and self.agent1.type == "HUMAN") or (self.turn and self.agent2.type == "HUMAN"):
                 self.updateStatehuman()
        if len(self.attackingCountries) >=2:
            self.attackingCountries.clear()

    def doAttack(self):
        if (not self.turn and self.agent1.type != "HUMAN") or (self.turn and self.agent2.type != "HUMAN"):
            self.updateStateAI()




    def initializeState(self):
        available_countries = [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9, self.c10,
                               self.c11, self.c12, self.c13, self.c14, self.c15, self.c16, self.c17, self.c18, self.c19,
                               self.c20, self.c21, self.c22, self.c23, self.c24, self.c25, self.c26, self.c27, self.c28, self.c29,
                               self.c30, self.c31, self.c32, self.c33, self.c34, self.c35, self.c36, self.c37]
        redTroops = 40
        blueTroops = 40

        canAddRed = True
        canAddBlue = True

        while canAddRed or canAddBlue:
            # redTroops
            if canAddRed:
                if available_countries.__len__() != 0:
                    country = random.choice(available_countries)
                    available_countries.remove(country)
                    country.owner=self.agent1
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
                    country.owner=self.agent2
                    self.agent2.addCountry(country)
                    blueTroops -= 1
                else:
                    country = random.choice(self.agent2.countries)
                    blueTroops -= 1
                country.addTroops(1)
                if blueTroops == 0:
                    canAddBlue = False
    def updateStateAI(self):
        if self.turn:
            if self.agent2.attack():
                self.turn = False
        else:
            if self.agent1.attack():
                self.turn = True

    def updateStatehuman(self):
        #self.agent1.ca
        if self.turn:
            if self.agent2.attack(self.attackingCountries[0],self.attackingCountries[1],self.amountofattackingtroops):
                self.turn = False
        else:
            if self.agent1.attack(self.attackingCountries[0],self.attackingCountries[1],int(self.amountofattackingtroops)):
                self.turn = True
