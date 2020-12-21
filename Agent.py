from Country import *


class Agent:

    def __init__(self):
        self.countries = []
        #self.color = BLACK



    def takeTurn(self):
        amount = self.calcBonusTroops()
        self.addTroops(amount)
        self.attack()

    def calcBonusTroops(self) -> int:
        numberOfCountries = len(self.countries)
        return max(3, numberOfCountries // 3)

    def attack(self):
        # depends on each agent.. every agent has his own attacking algorithm
        pass

    def addTroops(self, amount):
        country = self.chooseCountryToAddTroops()
        country.addTroops(amount)

    def chooseCountryToAddTroops(self) -> Country:
        # depends on each agent... every agent has his own choosing algorithm
        pass
