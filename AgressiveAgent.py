from Agent import *


class AgressiveAgent(Agent):
    def takeTurn(self):
        super().takeTurn()

    def chooseCountryToAddTroops(self) -> Country:
        return super().chooseCountryToAddTroops()

    def attack(self):
        super().attack()