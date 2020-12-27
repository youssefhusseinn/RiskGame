from Country import *
from Agent import *
import copy
from Node import *

class Node:
    def __init__(self, countries: [Country], parent):
        #self.countries = countries
        self.encodedState = self.encode(countries)
        self.countries = self.decode(self.encodedState)
        self.heuristic = self.calculate_heuristic(countries)
        self.parent = parent
        if parent is None:
            self.cost = 0
        else:
            self.cost = parent.cost + 1
        self.totalCost = self.cost + self.heuristic

    def path_to_root(self):
        temp = self
        if temp.parent is None:
            return None
        while temp.parent.parent != None:
            temp = temp.parent
        return temp

    # def calculate_heuristic(self, state) -> float:
    #     sum_enemy_amount_of_units = 0
    #     sum_border_security_ratio = 0
    #     x = 0
    #     for c in state:
    #         if c.ownerboolean:
    #             for neighbor in c.neighbors:
    #                 if not neighbor.ownerboolean:
    #                     sum_enemy_amount_of_units += neighbor.numOfTroops
    #             sum_border_security_ratio += sum_enemy_amount_of_units * 1.0 / c.numOfTroops
    #             sum_enemy_amount_of_units = 0
    #         else:
    #             x += 1
    #     return 0.5 * sum_border_security_ratio + 0.5 * x


    def calculate_heuristic(self, state) -> int:
        enemyCountries = 0
        enemyTroops = 0
        for c in state:
            if c.ownerboolean == False:
                enemyCountries += 1
                enemyTroops += c.numOfTroops
        return enemyCountries + enemyTroops


    def calcBonus(self) -> int:
        counter = 0
        for c in self.countries:
            if c.ownerboolean:
                counter += 1
        return max(3, counter // 3)

    def isGoal(self):
        for country in self.countries:
            if not country.ownerboolean:
                return False
        return True

    def generateChildren(self):
        retStates = []
        amount = self.calcBonus()
        for c in self.countries:
            if c.ownerboolean:
                c.addTroops(amount)
                for neighbor in c.neighbors:
                    if not neighbor.ownerboolean and c.numOfTroops - 1 > neighbor.numOfTroops:
                        #do
                        attackerTroops = c.numOfTroops
                        defenderTroops = neighbor.numOfTroops
                        neighbor.numOfTroops = attackerTroops - 1
                        c.numOfTroops = 1
                        neighbor.ownerboolean = True

                        retStates.append(Node(self.countries, self))
                        #undo
                        c.numOfTroops = attackerTroops
                        neighbor.numOfTroops = defenderTroops
                        neighbor.ownerboolean = False
                retStates.append(Node(self.countries, self))
                c.numOfTroops -= amount
        return retStates


    def encode(self, countries: [Country]) -> str:
        x = ""
        for c in countries:
            x = x + " " + c.id + "," + str(c.ownerboolean) + "," + str(c.numOfTroops) + ",["
            for neighbor in c.neighbors:
                x = x + neighbor.id + "-"
            x = x[:-1]
            x += "]"
        return x

    def decode(self, string: str) -> [Country]:
        array = string.split()
        countryneighbors = dict()
        troopsset = {}
        ownerset = {}
        for i in range(0,len(array)):
            country = array[i].split(",")
            id = country[0]
            if country[1] == "True":
                owner = True
            else:
                owner = False
            troops = country[2]
            troopsset[id] = int(troops)
            ownerset[id] = owner
            neighbors = country[3]
            neighbors = neighbors[1:-1].split("-")
            countryneighbors[id] = set()
            for neighborid in neighbors:
                countryneighbors[id].add(neighborid)
        countryset = dict()
        for countryid in countryneighbors:
            newCountry = Country(countryid)
            newCountry.ownerboolean = ownerset[countryid]
            newCountry.numOfTroops = troopsset[countryid]
            countryset[countryid] = newCountry
        for countryid in countryset.keys():
            for neighborid in countryneighbors[countryid]:
                countryset[countryid].neighbors.append(countryset[neighborid])
        return countryset.values()


