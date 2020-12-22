from Agent import *


class PacifistAgent(Agent):

    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)
        self.attack()

    def attack(self):
        (attackerCountry, defenderCountry) = self.getOpponentCountryWithMinimumTroops()
        if attackerCountry is None or attackerCountry not in self.countries:
            return

        defenderCountry.owner.removeCountry(defenderCountry)
        defenderCountry.owner = self
        defenderCountry.numOfTroops = attackerCountry.numOfTroops - 1
        attackerCountry.numOfTroops = 1

    # choose the country with minimum troops
    def chooseCountryToAddTroops(self) -> Country:
        country = None
        mintroops = 10e6
        for c in self.countries:
            if c.numOfTroops < mintroops:
                country = c
                mintroops = c.numOfTroops
        return country

    def getOpponentCountryWithMinimumTroops(self) -> (Country, Country):
        mylist = []
        myset = set([Country])
        minimumval = 10e6
        maximumval = 1
        attacker = None
        defender = None
        # for country in self.countries:
        #     myset.add(country)
        #     mylist.append(country)
        for country in self.countries:
            for neighbor in country.neighbors:
                if neighbor not in self.countries:
                    if maximumval <= country.numOfTroops and minimumval >= neighbor.numOfTroops:
                        maximumval = country.numOfTroops
                        minimumval = neighbor.numOfTroops
                        attacker = country
                        defender = neighbor
        return attacker, defender