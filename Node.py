from Country import *
from Agent import *
import copy


class Node:
    def __init__(self, countries: [Country], agent: Agent):
        self.countries = copy.deepcopy(countries)
        self.agent = agent
        self.children = []

    def calcBonus(self) -> int:
        counter = 0
        for c in self.countries:
            if c.owner == self.agent:
                counter += 1
        return max(3, counter // 3)

    def isGoal(self):
        for country in self.countries:
            if country.agent != self.agent:
                return False
        return True

    def generateChildren(self):
        for attacker in self.agent.countries:
            for defender in attacker.neighbors:
                if defender.owner != self.agent and attacker.numOfTroops - 1 > defender.numOfTroops:
                    newCountries = []
                    for c in self.countries:
                        if c != attacker and c != defender:
                            newCountries.append(copy.deepcopy(c))
                    newattacker = copy.deepcopy(attacker)
                    newdefender = copy.deepcopy(defender)
                    newattacker.numOfTroops = 1
                    newdefender.numOfTroops = attacker.numOfTroops -1
                    newdefender.owner = self.agent
                    newCountries.append(newdefender)
                    newCountries.append(newattacker)
                    nextState = Node(newCountries, self.agent)
                    self.children.append(nextState)
        """
        
        for c in agent.countries:
            for each possible attack with c:
                simulate perform el attack
                self.children.append(new Node(....))
        
        """

    def heuristic(self) -> int:
        numOfCountries = 0
        numOfTroops = 0
        for country in self.countries:
            if country.agent == self.agent:
                numOfCountries += 1
                numOfTroops += country.numOfTroops
        return 2*numOfCountries + numOfTroops