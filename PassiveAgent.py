from Agent import *

class PassiveAgent(Agent):
    def attack(self):
        self.takeTurn()
        return True

    # This agent places all of its bonus armies to the territory with the fewest armies, and doesn’t make any attacks.
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        print(country)
        amount = self.calcBonusTroops()
        print(amount)
        country.numOfTroops= country.numOfTroops +amount

    # choose the country with minimum troops
    def chooseCountryToAddTroops(self) :
        country = None
        mintroops = 10e6
        for c in self.countries:
            if c.numOfTroops < mintroops:
                country = c
                mintroops = c.numOfTroops
        return country
