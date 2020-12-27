import operator

from Agent import *
from heapq import *
from copy import *
import random
from Node import *
from US_STATE import *

class GreedyAgent(Agent):

    def _init_(self, type, color):
        super()._init_(type, color)

    def takeTurn(self, countries):
        self.attack(countries)

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
        pq = []
        heapify(pq)
        arr = dict()
        curState = countries
        arr[self.encode(countries)] = countries
        children = self.generateChildren(curState)
        print(len(children))
        for child in children:
            arr[child] = self.decode(child)
        for child in arr.keys():
            x = int( self.heuristic(arr[child]))
            heappush(pq, (x, random.random(), arr[child]))

        (bestCost, y, newCountries) = heappop(pq)

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


    def generateChildren(self, state) -> [str]:
        retStates = []
        amount = self.calcBonusTroops()
        for c in state:
            if c.ownerboolean:
                c.addTroops(amount)
                for neighbor in c.neighbors:
                    if not neighbor.ownerboolean and c.numOfTroops - 1 > neighbor.numOfTroops:
                        #do
                        attackerTroops = c.numOfTroops
                        defenderTroops = neighbor.numOfTroops
                        defenderOwner = neighbor.owner
                        defenderOwner.removeCountry(neighbor)
                        self.countries.append(neighbor)
                        neighbor.owner = self
                        neighbor.numOfTroops = attackerTroops - 1
                        c.numOfTroops = 1
                        neighbor.ownerboolean = True

                        retStates.append(self.encode(state))
                        #undo
                        c.numOfTroops = attackerTroops
                        neighbor.numOfTroops = defenderTroops
                        neighbor.owner = defenderOwner
                        neighbor.ownerboolean = False
                        self.removeCountry(neighbor)
                        defenderOwner.countries.append(neighbor)
                retStates.append(self.encode(state))
                c.numOfTroops -= amount
        return retStates

    def chooseCountryToAddTroops(self) -> Country:
        pass

    def heuristic(self, state) -> int:
        enemyCountries = 0
        enemyTroops = 0
        for c in state:
            if c.ownerboolean == False:
                enemyCountries += 1
                enemyTroops += c.numOfTroops
        return enemyCountries + enemyTroops

    # def heuristic(self, state) -> float:
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






# from Agent import *
# import ctypes
# import time
# import threading
#
#
# class GreedyAgent(Agent):
#     c=None
#     num=0
#
#     def func(self):
#         #country.numOfTroops=num
#         self.c.numOfTroops=self.num
#     def takeTurn(self):
#
#         # time.sleep(5)
#         troopsAddedToCountry=self.addBonusTroops()
#         print(troopsAddedToCountry.id)
#         self.attackHelper(troopsAddedToCountry)
#         return True
#
#     def addBonusTroops(self):
#         myCountries = self.countries
#
#         # heuristic to put bonus troops : for every country of mine will get num of enemy troops surrouned by
#         #                                and the bonus troops will add to country with
#         #                                max num of surrouned troops - amount of troops in this country
#         bonustroops = self.calcBonusTroops()
#         surroundedwith = []
#
#         for mycountry in myCountries:
#             counter = 0
#             for c in mycountry.neighbors:
#                 if (c.owner == self):
#                     counter -= c.numOfTroops
#                 else:
#                     counter += c.numOfTroops
#             surroundedwith.append(counter)
#         flag = True
#         while flag:
#             indexToPutTroops = surroundedwith.index(max(surroundedwith))
#             if myCountries[indexToPutTroops].owner == self:
#
#                 myCountries[indexToPutTroops].numOfTroops += bonustroops
#                 return myCountries[indexToPutTroops]
#
#
#             else:
#                 del surroundedwith[indexToPutTroops]
#
#     def attackHelper(self ,troopsAddedToCountry):
#         global countryAttackto
#         myCountries = self.countries
#         surroundedwith = []
#
#         for mycountry in myCountries:
#             counter = 0
#             for c in mycountry.neighbors:
#                 if (c.owner == self):
#                     counter -= c.numOfTroops
#                 else:
#                     counter += c.numOfTroops
#             surroundedwith.append(counter)
#         flag = True
#         while flag:
#
#             surroundedwith.sort()
#             i=0
#             for s in surroundedwith  :
#                  if (myCountries[i].owner == self):
#                      countryAttackFrom = myCountries[i]
#                      countryAttackFrom.neighbors.sort(key=lambda x: x.numOfTroops)
#                      for c in countryAttackFrom.neighbors:
#                           countryAttackto=c
#                           if countryAttackto.numOfTroops < countryAttackFrom.numOfTroops-1  and countryAttackto.owner != self:
#                               # do the attack
#                               numOfTroopsAttackwith = countryAttackto.numOfTroops+1
#                               use_timer=True
#                               if use_timer:
#                                 temp_num_to=numOfTroopsAttackwith
#                                 temp_num_from=countryAttackFrom.numOfTroops
#                                 t=threading.Timer(1,self.setTroops,args=(countryAttackto,countryAttackFrom,temp_num_to,temp_num_from,troopsAddedToCountry,troopsAddedToCountry.numOfTroops))
#                                 t.start()
#                                 troopsAddedToCountry.numOfTroops= str(troopsAddedToCountry.numOfTroops)+' B'
#                                 countryAttackFrom.numOfTroops=str(countryAttackFrom.numOfTroops)+'A'
#                                 countryAttackto.numOfTroops = str(countryAttackto.numOfTroops)+"D"
#                               else:
#                                   countryAttackFrom.numOfTroops -= numOfTroopsAttackwith
#                                   countryAttackto.owner.removeCountry(countryAttackto)
#                                   countryAttackto.owner = self
#                                   countryAttackto.owner.countries.append(countryAttackto)
#
#
#                               flag = False
#                               return
#                  i+=1
#             print("NO possible attacks")
# #            ctypes.windll.user32.MessageBoxW(0, "NO POSSIBLE ATTACKS", "ALERT", 1)
#             return
#     def setTroops(self,country_to,country_from,num_to,num_from,troopsAddedToCountry,num_bonus):
#         country_to.numOfTroops=num_to
#         country_from.numOfTroops=num_from
#         country_from.numOfTroops -= num_to
#         troopsAddedToCountry.numOfTroops=num_bonus
#         country_to.owner.removeCountry(country_to)
#         country_to.owner = self
#         country_to.owner.countries.append(country_to)
#     def setTroopsBonus(self,country,old_num,amount):
#         country.numOfTroops=old_num+amount