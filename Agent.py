from Country import *

class Agent:

    def __init__(self):
        self.color = None
        self.countries = dict(Country,int)

    def takeTurn(self):
        amount = self.calcBonusTroops()
        self.addTroops(amount)


    def calcBonusTroops(self) -> int:
        numberOfCountries = len(self.countries)
        return max(3, numberOfCountries // 3)

    def attack(self):
        #depends on each agent.. every agent has his own attacking algorithm
        pass

    def addTroops(self, amount):
        while amount > 0:
            country = self.chooseCountryToAddTroops()
            self.countries[country] += 1
            amount -= 1

    def chooseCountryToAddTroops(self) -> Country:
        # depends on each agent... every agent has his own choosing algorithm
        pass

    def chooseCountryForAttacking(self) -> Country:
        # depends on each agent... every agent has his own choosing algorithm
        pass