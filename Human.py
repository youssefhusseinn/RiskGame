from Agent import *
import Country
from Country import *
import ctypes


class Human(Agent):

    def canAttack(self,countryAttackFrom,countryAttackTo,amountOfTroops):
        if countryAttackFrom.owner== self and \
                countryAttackTo in countryAttackFrom.neighbors and \
                amountOfTroops-1 <= countryAttackFrom.numOfTroops and \
                amountOfTroops-1 > countryAttackTo.numOfTroops :
            return True
        else:
            return False
            

    def attack(self,countryAttackFrom,countryAttackTo,amountOfTroops):
         flag=self.canAttack(self,countryAttackFrom,countryAttackTo,amountOfTroops)
         if flag:
            countryAttackFrom.numOfTroops=countryAttackFrom.numOfTroops-amountOfTroops
            countryAttackTo=amountOfTroops
            countryAttackTo.owner = self
         else:
            ctypes.windll.user32.MessageBoxW(0, "invalid attack", "ALERT", 1)
     
         









