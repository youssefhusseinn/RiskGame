from Agent import *
import ctypes


class PassiveAgent(Agent):
    def attack(self,countries):
        self.takeTurn(countries)
        return True

    # This agent places all of its bonus armies to the territory with the fewest armies, and doesn’t make any attacks.
    def takeTurn(self,countries):
        country = self.chooseCountryToAddTroops(countries)
        if(country == None):
            ctypes.windll.user32.MessageBoxW(0, "NO MORE POSSIBLE MOVES", "ALERT", 1)
            return
        amount = self.calcBonusTroops()
        country.numOfTroops= country.numOfTroops +amount

    # choose the country with minimum troops
    def chooseCountryToAddTroops(self,countries) :
        country = None
        mintroops = 10e6
        for c in countries:
            if c.numOfTroops < mintroops and c.owner==self :
                country = c
                mintroops = c.numOfTroops
        return country
