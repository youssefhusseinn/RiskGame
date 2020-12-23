from Agent import *
import ctypes
import time


class GreedyAgent(Agent):
    def takeTurn(self):

        # time.sleep(5)
        self.addBonusTroops()
        # time.sleep(5)
        self.attackHelper()
        # time.sleep(5)
        return True

    def addBonusTroops(self):
        myCountries = self.countries

        # heuristic to put bonus troops : for every country of mine will get num of enemy troops surrouned by
        #                                and the bonus troops will add to country with
        #                                max num of surrouned troops - amount of troops in this country
        bonustroops = self.calcBonusTroops()
        surroundedwith = []

        for mycountry in myCountries:
            counter = 0
            for c in mycountry.neighbors:
                if (c.owner == self):
                    counter -= c.numOfTroops
                else:
                    counter += c.numOfTroops
            surroundedwith.append(counter - mycountry.numOfTroops)
        flag = True
        while flag:
            indexToPutTroops = surroundedwith.index(max(surroundedwith))
            if myCountries[indexToPutTroops].owner == self:
                print(bonustroops)
                myCountries[indexToPutTroops].numOfTroops += bonustroops
                print(myCountries[indexToPutTroops].id)
                flag = False
                return
            else:
                del surroundedwith[indexToPutTroops]

    def attackHelper(self ):
        global countryAttackto
        myCountries = self.countries
        surroundedwith = []

        for mycountry in myCountries:
            counter = 0
            for c in mycountry.neighbors:
                if (c.owner == self):
                    counter -= c.numOfTroops
                else:
                    counter += c.numOfTroops
            surroundedwith.append(counter - mycountry.numOfTroops)
        flag = True
        while flag:

            surroundedwith.sort()
            i=0
            for s in surroundedwith  :
                 if (myCountries[i].owner == self):
                     countryAttackFrom = myCountries[i]
                     countryAttackFrom.neighbors.sort(key=lambda x: x.numOfTroops)
                     for c in countryAttackFrom.neighbors:
                          countryAttackto=c
                          if countryAttackto.numOfTroops < countryAttackFrom.numOfTroops  and countryAttackto.owner != self:
                              # do the attack
                              numOfTroopsAttackwith = countryAttackto.numOfTroops
                              countryAttackto.numOfTroops = numOfTroopsAttackwith
                              countryAttackFrom.numOfTroops -= numOfTroopsAttackwith
                              countryAttackto.owner.removeCountry(countryAttackto)
                              countryAttackto.owner = self
                              countryAttackto.owner.countries.append(countryAttackto)
                              flag = False
                              return
                 i+=1
            print("NO possible attacks")
#            ctypes.windll.user32.MessageBoxW(0, "NO POSSIBLE ATTACKS", "ALERT", 1)
            return