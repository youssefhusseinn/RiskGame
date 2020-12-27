from Agent import *
from Country import *
import threading

class AgressiveAgent(Agent):
    # This agent places all of its bonus armies to the territory with the most armies
    # and greedily attempts to attack territories with most armies that he can attack
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)
        self.attack(country)

    def chooseCountryToAddTroops(self) -> Country:
        country = None
        maxTroops = int(-1e6)
        for c in self.countries:
            if c.numOfTroops > maxTroops:
                maxTroops = c.numOfTroops
                country = c
        return country

    def attack(self,countrytroops):
        numberOfTroopsOfNeighborWithMaxTroops = 0
        neighborWithMaxTroops = None
        attackingCountry = None
        for country in self.countries:
            for neighbor in country.neighbors:
                if neighbor not in self.countries:
                    if neighbor.numOfTroops < country.numOfTroops - 1: #Found one to attack
                        if numberOfTroopsOfNeighborWithMaxTroops < neighbor.numOfTroops:
                            numberOfTroopsOfNeighborWithMaxTroops = neighbor.numOfTroops
                            neighborWithMaxTroops = neighbor
                            attackingCountry = country

        if attackingCountry and neighborWithMaxTroops:
            use_timer=True
            if use_timer:

                num_to=neighborWithMaxTroops.numOfTroops
                num_from=attackingCountry.numOfTroops
                numtroops=countrytroops.numOfTroops
                t = threading.Timer(3, self.setTroops,args=(neighborWithMaxTroops, attackingCountry, num_to, num_from,countrytroops,numtroops))
                t.start()
                countrytroops.numOfTroops= str(countrytroops.numOfTroops) + 'B'
                attackingCountry.numOfTroops = str(attackingCountry.numOfTroops) + 'A'
                neighborWithMaxTroops.numOfTroops = str(neighborWithMaxTroops.numOfTroops) + "D"
            else:
                neighborWithMaxTroops.owner.removeCountry(neighborWithMaxTroops)
                neighborWithMaxTroops.numOfTroops = attackingCountry.numOfTroops - 1
                attackingCountry.numOfTroops = 1
                neighborWithMaxTroops.owner = self
                self.countries.append(neighborWithMaxTroops)


    def setTroops(self,country_to,country_from,num_to,num_from,country,troops):
        country.numOfTroops=troops
        country_to.numOfTroops=num_to
        country_from.numOfTroops=num_from
        country_to.owner.removeCountry(country_to)
        country_to.numOfTroops = country_from.numOfTroops - 1
        country_from.numOfTroops = 1
        country_to.owner = self
        self.countries.append(country_to)

