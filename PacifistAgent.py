from Agent import *
import threading

class PacifistAgent(Agent):

    def takeTurn(self):
        country = self.chooseCountryToAddTroops()
        amount = self.calcBonusTroops()
        country.addTroops(amount)
        self.attack(country)

    def attack(self,country):
        (attackerCountry, defenderCountry) = self.getOpponentCountryWithMinimumTroops()
        if attackerCountry is None or attackerCountry not in self.countries:
            return
        use_timer=True
        if use_timer:
            num_to = defenderCountry.numOfTroops
            num_from = attackerCountry.numOfTroops
            num_troops=country.numOfTroops
            t = threading.Timer(3, self.setTroops, args=(defenderCountry, attackerCountry, num_to, num_from,country,num_troops))
            t.start()
            country.numOfTroops= str(attackerCountry.numOfTroops) + 'B'
            attackerCountry.numOfTroops = str(attackerCountry.numOfTroops) + 'A'
            defenderCountry.numOfTroops = str(defenderCountry.numOfTroops) + "D"
        else:
            defenderCountry.owner.removeCountry(defenderCountry)
            defenderCountry.owner = self
            self.countries.append(defenderCountry)
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

    def setTroops(self, country_to, country_from, num_to, num_from,country,numoftroops):
        country.numOfTroops=numoftroops
        country_to.numOfTroops = num_to
        country_from.numOfTroops = num_from
        country_to.owner.removeCountry(country_to)
        country_to.owner = self
        self.countries.append(country_to)
        country_to.numOfTroops = country_from.numOfTroops - 1
        country_from.numOfTroops = 1
