from Country import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)

class Agent:

    def __init__(self,type,color):
        self.countries = []
        self.color = color
        self.type=type

    def addCountry(self,country):
        self.countries.append(country)

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
