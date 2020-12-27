import operator

from Agent import *
from heapq import *
from copy import *

from Node import *
from US_STATE import *


class AStarAgent(Agent):

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

        newCountries = self.a_star_search(countries)
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

    def a_star_search(self, countries: [Country]) -> [Country]:
        curNode = Node(countries, None)
        frontier = []
        stateToNode = dict()
        heapify(frontier)
        stateToNode[curNode.encodedState] = curNode
        heappush(frontier, (curNode.totalCost, curNode.encodedState))
        explored = set()
        frontier_config = {}
        helper = dict()
        helper[curNode.encodedState] = curNode.totalCost
        frontier_config[curNode.encodedState] = True
        nodes_expanded = 0
        number_child = 0
        while len(frontier) > 0:
            #print(nodes_expanded)
            if nodes_expanded >= 10000:
                x, y = heappop(frontier)
                #print(nodes_expanded)
                print(number_child)
                return stateToNode[y].path_to_root().countries
            (cost, encodedState) = heappop(frontier)
            while encodedState in helper and cost > helper[encodedState]:
                cost, encodedState = heappop(frontier)

            explored.add(encodedState)
            helper.pop(encodedState)

            if stateToNode[encodedState].isGoal():
                print(number_child)
                #print(nodes_expanded)
                return stateToNode[encodedState].path_to_root().countries
            nodes_expanded += 1
            for neighborNode in stateToNode[encodedState].generateChildren():
                # Add state to explored states if doesn't already exists.
                number_child += 1
                if neighborNode.encodedState not in explored and neighborNode.encodedState not in frontier_config:
                    heappush(frontier, (neighborNode.totalCost, neighborNode.encodedState))
                    stateToNode[neighborNode.encodedState] = neighborNode
                    helper[neighborNode.encodedState] = neighborNode.totalCost
                    frontier_config[neighborNode.encodedState] = True
                elif neighborNode.encodedState in helper:
                    if neighborNode.totalCost < helper[neighborNode.encodedState]:
                        heappush(frontier, (neighborNode.totalCost, neighborNode.encodedState))
                        stateToNode[neighborNode.encodedState] = neighborNode
                        helper[neighborNode.encodedState] = neighborNode.totalCost
        print(number_child)
        #print(nodes_expanded)
        return None

    # def heuristic(self, state) -> int:
    #     enemyCountries = 0
    #     enemyTroops = 0
    #     for c in state:
    #         if c.ownerboolean == False:
    #             enemyCountries += 1
    #             enemyTroops += c.numOfTroops
    #     return enemyCountries + enemyTroops
