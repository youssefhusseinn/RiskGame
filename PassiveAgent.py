import ctypes

from Agent import *
import threading
class PassiveAgent(Agent):


    # This agent places all of its bonus armies to the territory with the fewest armies, and doesn’t make any attacks.
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        if country is None:
            ctypes.windll.user32.MessageBoxW(0, "NO MORE ATTACKS", "ALERT", 1)
            return
        use_timer=False
        if use_timer:

            old_num=country.numOfTroops
            t = threading.Timer(1, self.setTroopsBonus,args=(country,old_num,self.calcBonusTroops()))
            t.start()
            country.numOfTroops = str(country.numOfTroops) + "B"
        else:
            amount = self.calcBonusTroops()
            country.numOfTroops = country.numOfTroops + amount



    # choose the country with minimum troops
    def chooseCountryToAddTroops(self):
        country = None
        mintroops = 10e6
        for c in self.countries:
            if c.numOfTroops < mintroops:
                country = c
                mintroops = c.numOfTroops
        return country
    def setTroopsBonus(self,country,old_num,amount):
        country.numOfTroops=old_num+amount
