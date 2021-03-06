from Country import *
BLUE = (9, 5, 101)
WHITE = (255, 255, 255, 0)
BLACK = (0, 0, 0)
DARKRED = (229, 12, 22)
DARKBLUE = (2, 8, 126)

class Agent:

    def __init__(self, type, color):
        self.countries = []
        #self.countriesIDs=[]
        self.color = color
        self.type = type
        self.bonusTroops = 0

    def addCountry(self, country):
        self.countries.append(country)
        #self.countriesIDs.append(country.id)

    def takeTurn(self):
        amount = self.calcBonusTroops()
        self.addTroops(amount)
        self.attack()

    def removeCountry(self, country: Country):
        id = country.id
        for c in self.countries:
            if c.id == id:
                self.countries.remove(c)
                break
        #self.countries.remove(country)
#        self.countriesIDs.remove(country.id)
    def calcBonusTroops(self):
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
