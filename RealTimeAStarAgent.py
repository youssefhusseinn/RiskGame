import operator

from Agent import *
from heapq import *
from copy import *
from random import *
from Node import *
from US_STATE import *



class RealTimeAStarAgent(Agent):

    def __init__(self, type, color):
        super().__init__(type, color)
        self.cost = 0

    def takeTurn(self, countries):
        self.attack(countries)
        self.cost += 2

    def attack(self, countries):
        opponent = None
        mp = {}
        for c in countries:
            mp[c.id] = c
            if c.owner == self:
                c.ownerboolean = True
            else:
                c.ownerboolean = False
                opponent = c.owner

        newCountries = self.real_time_a_star_search(countries)
        if newCountries is None:
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

    def real_time_a_star_search(self, countries: [Country]) -> [Country]:
        curNode = Node(countries, None)
        h = {}
        nodesExpanded = 1
        number_child = 0
        while not curNode.isGoal():
            if nodesExpanded>=5000:
               # print(nodesExpanded)
                print(number_child)
                return curNode.path_to_root().countries
            pq = []
            heapify(pq)
            dakhal = False
            nodesExpanded += 1
            for neighbor in curNode.generateChildren():
                number_child += 1
                dakhal = True
                if neighbor.encodedState in h.keys():
                    neighbor.parent = h[neighbor.encodedState].parent
                    neighbor.heuristic = h[neighbor.encodedState].heuristic
                    neighborCost = h[neighbor].heuristic + 1
                else:
                    neighborCost = neighbor.heuristic + 1
                x = random.random()
                heappush(pq, (neighborCost, x, neighbor))
            if not dakhal:
                #print(nodesExpanded)
                print(number_child)
                return curNode.path_to_root().countries
            if len(pq) > 0:
                temp = heappop(pq)[2]
            if len(pq) > 0:
                h[curNode.encodedState] = heappop(pq)[0]
            curNode = temp
        firstNode = curNode.path_to_root()
        #print(nodesExpanded)
        print(number_child)
        if firstNode is None:
            return None
        else:
            return curNode.path_to_root().countries

    def heuristic(self, state) -> int:
        enemyCountries = 0
        enemyTroops = 0
        for c in state:
            if c.ownerboolean == False:
                enemyCountries += 1
                enemyTroops += c.numOfTroops
        return enemyCountries + enemyTroops
