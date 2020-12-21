from Agent import *


class PassiveAgent(Agent):
    # This agent places all of its bonus armies to the territory with the fewest armies, and doesn’t make any attacks.
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)

    # choose the country with minimum troops
    def chooseCountryToAddTroops(self) -> Country:
        country = None
        mintroops = 10e6
        for c in self.countries.keys():
            if self.countries[c] < mintroops:
                country = c
                mintroops = self.countries[c]
        return country
