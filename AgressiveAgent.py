from Agent import *
from Country import *


class AgressiveAgent(Agent):
    # This agent places all of its bonus armies to the territory with the most armies
    # and greedily attempts to attack territories with most armies that he can attack
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        self.countries[country] += amount
        self.attack()

    def chooseCountryToAddTroops(self) -> Country:
        country = None
        maxTroops = int(-1e6)
        for c in self.countries.keys():
            if self.countries[c] > maxTroops:
                maxTroops = self.countries[c]
                country = c
        return country


    def attack(self):
        attackedSoFar = set()
        canAttack = True
        while canAttack:
            numberOfTroopsOfNeighborWithMaxTroops = 0
            neighborWithMaxTroops = None
            attackingCountry = None
            canAttack = False
            for country in self.countries:
                for neighbor in country.neighbors:
                    if neighbor not in self.countries:
                        if neighbor.getNumberOfTroops() < country.getNumberOfTroops()-1: #Found one to attack
                            if numberOfTroopsOfNeighborWithMaxTroops < neighbor.getNumberOfTroops():
                                numberOfTroopsOfNeighborWithMaxTroops = neighbor.getNumberOfTroops()
                                neighborWithMaxTroops = neighbor
                                attackingCountry = country

            if attackingCountry and neighborWithMaxTroops and neighborWithMaxTroops not in attackedSoFar:
                canAttack = True
                neighborWithMaxTroops.agent.countries[neighborWithMaxTroops] = self.countries[attackingCountry] - numberOfTroopsOfNeighborWithMaxTroops - 1
                self.countries[attackingCountry] = 1
                self.countries[neighborWithMaxTroops] = neighborWithMaxTroops.getNumberOfTroops()
                attackedSoFar.add(neighborWithMaxTroops)





        """""
        countryWithMaxTroops = None
        maxTroops = 0
        for c in self.countries:
            if self.countries[c] > maxTroops:
                countryWithMaxTroops = c
                maxTroops = self.countries[c]

        while True:
            neighborWithLeastTroops = None
            minTroops = int(1e6)
            for neighbor in countryWithMaxTroops.neighbors:
                    if 
        """""
