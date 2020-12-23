from Agent import *
from Country import *


class AgressiveAgent(Agent):
    # This agent places all of its bonus armies to the territory with the most armies
    # and greedily attempts to attack territories with most armies that he can attack
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)
        self.attack()

    def chooseCountryToAddTroops(self) -> Country:
        country = None
        maxTroops = int(-1e6)
        for c in self.countries.keys():
            if self.countries[c] > maxTroops:
                maxTroops = self.countries[c]
                country = c
        return country

    def attack(self,countries):
        print("waslt la attack el aggresive")
        return True

    def attackold(self):
        print("waslt ll aggresive")

        #attackedSoFar = set()
        #canAttack = True
        #while canAttack:

        numberOfTroopsOfNeighborWithMaxTroops = 0
        neighborWithMaxTroops = None
        attackingCountry = None
        canAttack = False
        for country in self.countries:
            for neighbor in country.neighbors:
                if neighbor not in self.countries:
                    if neighbor.numOfTroops < country.numOfTroops-1: #Found one to attack
                        if numberOfTroopsOfNeighborWithMaxTroops < neighbor.numOfTroops:
                            numberOfTroopsOfNeighborWithMaxTroops = neighbor.numOfTroops
                            neighborWithMaxTroops = neighbor
                            attackingCountry = country

        if attackingCountry and neighborWithMaxTroops and neighborWithMaxTroops:
                #not in attackedSoFar:
            #canAttack = True
            #neighborWithMaxTroops.agent.countries[neighborWithMaxTroops] = self.countries[attackingCountry] - numberOfTroopsOfNeighborWithMaxTroops - 1
            neighborWithMaxTroops.owner.countries[neighborWithMaxTroops] = self.countries[attackingCountry] - 1
            self.countries[attackingCountry] = 1
            self.countries[neighborWithMaxTroops] = neighborWithMaxTroops.getNumberOfTroops()
            #attackedSoFar.add(neighborWithMaxTroops)
