from Agent import *
import Country
from Country import *
import ctypes


class Human(Agent):

    def canAttack(self, countryAttackFrom, countryAttackTo, amountOfTroops):
        if countryAttackFrom.owner == self and countryAttackTo in countryAttackFrom.neighbors and amountOfTroops < countryAttackFrom.numOfTroops and amountOfTroops >= countryAttackTo.numOfTroops:
            return True
        else:
            return False
            

    def attack(self,countryAttackFrom,countryAttackTo,amountOfTroops):

         flag=self.canAttack(countryAttackFrom,countryAttackTo,amountOfTroops)
         if flag:
            print(countryAttackFrom)
            countryAttackFrom.numOfTroops=countryAttackFrom.numOfTroops - amountOfTroops
            countryAttackTo.numOfTroops = amountOfTroops
            countryAttackTo.owner.removeCountry(countryAttackTo)
            countryAttackTo.owner = self
            self.countries.append(countryAttackTo)
            return True
         else:
          #  ctypes.windll.user32.MessageBoxW(0, "invalid attack PLEASE TRY AGAIN", "ALERT", 1)
            return False
     
         









