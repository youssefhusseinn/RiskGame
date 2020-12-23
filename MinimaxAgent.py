from Agent import *
from Node import *
from US_STATE import *
class MinimaxAgent(Agent):

    def takeTurn(self):
        #initialize state
        #intitialState = Node(US_STATE.countries, self)

        self.attack(US_STATE.countries)



    def attack(self, state):
        opponent = None
        mp = {}
        for c in state:
            mp[c.id] = c
            if c.owner == self:
                c.ownerboolean = True
            else:
                c.ownerboolean = False
                opponent = c.owner

        newCountries = self.decision(state)

        self.countries.clear()
        opponent.countries.clear()
        for c in newCountries:
            if c.ownerboolean is True:
                mp[c.id].owner = self
                self.countries.append(c)
            else:
                mp[c.id].owner = opponent
                opponent.countries.append(c)
            mp[c.id].numOfTroops = c.numOfTroops

    def decision(self, state) -> [Country]:
        (child, x) = self.maximize(state, 0)
        return child

    def heuristic(self, state: [Country]):
        attacking = 0
        defending = 0

        for c in state:
            if c.owner == self:
                for n in c.neighbors:
                    if n.owner != self and c.numOfTroops - 1 > n.numOfTroops:
                        attacking += 1
            else:
                for n in c.neighbors:
                    if n.owner == self and c.numOfTroops - 1 <= n.numOfTroops:
                        defending += 1

        return attacking+defending


    def maximize(self, state, depth) -> ([Country], int):
        # evaluate heuristic of state
        stateVal = self.heuristic(state)
        if depth == 2:
            return (state, stateVal)
        (maxState, maxVal) = (None, -1e9)
        bonus = self.calcBonusTroops()
        broke1 = False
        for bonusCountry in state:
            if bonusCountry.owner == self:
                bonusCountry.numOfTroops += bonus

                for c in state:
                    if c.owner == self:
                        for neighbor in c.neighbors:
                            if neighbor.owner != self and neighbor.numOfTroops < c.numOfTroops - 1:
                                attackerTroops = c.numOfTroops
                                defenderTroops = neighbor.numOfTroops
                                defenderOwner = neighbor.owner
                                defenderOwner.removeCountry(neighbor)
                                self.countries.append(neighbor)
                                neighbor.owner = self
                                neighbor.numOfTroops = attackerTroops - 1
                                c.numOfTroops = 1
                                neighbor.ownerboolean = True
                                (newstate, utility) = self.minimize(state, depth+1)

                                if utility > maxVal:
                                    maxVal = utility
                                    maxState = copy.deepcopy(state)


                                c.numOfTroops = attackerTroops
                                neighbor.numOfTroops = defenderTroops
                                neighbor.owner = defenderOwner
                                neighbor.ownerboolean = False
                                self.removeCountry(neighbor)
                                defenderOwner.countries.append(neighbor)

                bonusCountry.numOfTroops -= bonus
        return (maxState, maxVal)


    def minimize(self, state, depth) -> ([Country], int):
        # evaluate heuristic of state
        stateVal = self.heuristic(state)
        if depth == 2:
            return (state, stateVal)
        (minState, minVal) = (None, 1e9)
        bonus = self.calcBonusTroops()
        for bonusCountry in state:
            if bonusCountry.owner != self:
                bonusCountry.numOfTroops += bonus
                for c in state:
                    if c.owner != self:
                        for neighbor in c.neighbors:
                            if neighbor.owner == self and neighbor.numOfTroops < c.numOfTroops - 1:
                                attackerTroops = c.numOfTroops
                                defenderTroops = neighbor.numOfTroops
                                defenderOwner = neighbor.owner
                                defenderOwner.removeCountry(neighbor)
                                c.owner.countries.append(neighbor)
                                neighbor.owner = c.owner
                                neighbor.numOfTroops = attackerTroops - 1
                                c.numOfTroops = 1
                                neighbor.ownerboolean = False
                                (newstate, utility) = self.maximize(state, depth+1)

                                if utility < minVal:
                                    minVal = utility
                                    minState = copy.deepcopy(state)


                                c.numOfTroops = attackerTroops
                                neighbor.numOfTroops = defenderTroops
                                neighbor.owner = defenderOwner
                                neighbor.ownerboolean = True
                                c.owner.removeCountry(neighbor)
                                defenderOwner.countries.append(neighbor)
                bonusCountry.numOfTroops -= bonus
        return (minState, minVal)


    def chooseCountryToAddTroops(self) -> Country:
        pass