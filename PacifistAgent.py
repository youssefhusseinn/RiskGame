from Agent import *


class PacifistAgent(Agent):
    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)
        self.attack()

    def attack(self):
        (attackerCountry, defenderCountry) = self.getOpponentCountryWithMinimumTroops()
        if attackerCountry is None:
            return
        defenderCountry.agent = self
        defenderCountry.numOfTroops = attackerCountry.numOfTroops - 1
        attackerCountry.numOfTroops = 1

    # choose the country with minimum troops
    def chooseCountryToAddTroops(self) -> Country:
        country = None
        mintroops = 10e6
        for c in self.countries.keys():
            if self.countries[c] < mintroops:
                country = c
                mintroops = self.countries[c]
        return country

    def getOpponentCountryWithMinimumTroops(self) -> (Country, Country):
        mylist = list([Country])
        myset = set([Country])
        minimumval = 10e6
        maximumval = 1
        attacker = None
        defender = None
        for country in self.countries:
            myset.add(country)
            mylist.append(country)
        for country in mylist:
            for neighbor in country.neighbors:
                if neighbor not in myset:
                    if maximumval <= self.countries[country] and minimumval >= neighbor.getNumberOfTroops():
                        maximumval = self.countries[country]
                        minimumval = neighbor.getNumberOfTroops()
                        attacker = country
                        defender = neighbor
        return attacker, defender