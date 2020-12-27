from Agent import *
from US_STATE import *
import copy
class MinimaxAgent(Agent):

    def __init__(self, type, color):
        super().__init__(type, color)
        self.bonus_country = self.attack_country = self.defend_country = None

    def takeTurn(self, countries):
        #initialize state
        #intitialState = Node(US_STATE.countries, self)

        self.attack(countries)



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
        if newCountries == None:
            return

        self.countries.clear()
        opponent.countries.clear()
        for c in newCountries:
            if c.ownerboolean is True:
                mp[c.id].owner = self
                self.countries.append(c)
            else:
                mp[c.id].owner = opponent
                opponent.countries.append(mp[c.id])
            mp[c.id].numOfTroops = c.numOfTroops

        b = mp[self.bonus_country]
        a = mp[self.attack_country]
        d = mp[self.defend_country]


        use_timer = False
        if use_timer:

            t = threading.Timer(3, self.setTroops, args=(

            d, a, b, d.numOfTroops, a.numOfTroops,
            b.numOfTroops))
            t.start()
            b.numOfTroops = str(b.numOfTroops) + ' B'
            a.numOfTroops = str(a.numOfTroops) + 'A'
            d.numOfTroops = str(d.numOfTroops) + "D"


    def decision(self, state) -> [Country]:
        (child, x) = self.maximize(state, 0, -1e9, 1e9)
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


    def maximize(self, state, depth, alpha, beta) -> ([Country], int):
        # evaluate heuristic of state
        stateVal = self.heuristic(state)
        if depth == 2:
            return (state, stateVal)
        (maxState, maxVal) = (None, -1e9)
        bonus = self.calcBonusTroops()
        done = False
        for bonusCountry in state:
            if done:
                break
            if bonusCountry.owner == self:
                bonusCountry.numOfTroops += bonus
                for c in state:
                    if done:
                        break
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
                                (newstate, utility) = self.minimize(state, depth+1, alpha, beta)

                                if utility > maxVal:
                                    maxVal = utility
                                    maxState = copy.deepcopy(state)
                                    self.attack_country = c.id
                                    self.defend_country = neighbor.id
                                    self.bonus_country = bonusCountry.id


                                c.numOfTroops = attackerTroops
                                neighbor.numOfTroops = defenderTroops
                                neighbor.owner = defenderOwner
                                neighbor.ownerboolean = False
                                self.removeCountry(neighbor)
                                defenderOwner.countries.append(neighbor)

                                if maxVal >= beta:
                                    done = True
                                if done:
                                    break
                                if maxVal > alpha:
                                    alpha = maxVal
                bonusCountry.numOfTroops -= bonus
        return (maxState, maxVal)


    def minimize(self, state, depth, alpha, beta) -> ([Country], int):
        # evaluate heuristic of state
        stateVal = self.heuristic(state)
        if depth == 2:
            return (state, stateVal)
        (minState, minVal) = (None, 1e9)
        bonus = self.calcBonusTroops()
        done = False
        for bonusCountry in state:
            if done:
                break
            if bonusCountry.owner != self:
                bonusCountry.numOfTroops += bonus
                for c in state:
                    if done:
                        break
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
                                (newstate, utility) = self.maximize(state, depth+1, alpha, beta)

                                if utility < minVal:
                                    minVal = utility
                                    minState = copy.deepcopy(state)


                                c.numOfTroops = attackerTroops
                                neighbor.numOfTroops = defenderTroops
                                neighbor.owner = defenderOwner
                                neighbor.ownerboolean = True
                                c.owner.removeCountry(neighbor)
                                defenderOwner.countries.append(neighbor)

                                if minVal <= alpha:
                                    done = True
                                if done:
                                    break
                                if minVal < beta:
                                    beta = minVal
                bonusCountry.numOfTroops -= bonus
        return (minState, minVal)

    def setTroops(self, d,a,b, dnum, anum, bnum):
        d.numOfTroops = dnum
        a.numOfTroops = anum
        b.numOfTroops = bnum

    def chooseCountryToAddTroops(self) -> Country:
        pass