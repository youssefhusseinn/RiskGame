from Agent import *
from Node import *
from US_STATE import *
class MinimaxAgent(Agent):

    def takeTurn(self):
        #initialize state
        intitialState = Node(US_STATE.countries, self)
        self.attack(intitialState)

    def attack(self, state):
        #countryToAddTroops = self.chooseCountryToAddTroops()
        #countryToAddTroops.addTroops(amount)
        amount = state.calcBonus()
        for countryBonus in self.countries:
            for countryAttack in self.countries
                countryBonus.addTroops(amount)
                self.performAttack()
                bestChoice = self.maximize(self.countries)
                #country.numOfTroops -= amount

    def performAttack(self, countryAttack):
        for

    def chooseCountryToAddTroops(self) -> Country:
        pass
