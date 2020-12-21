from Agent import *
import Country
from Country import *
import ctypes


class Human:

    def canAttack(self,countryAttackFrom,countryAttackTo,amountOfTroops):
        if countryAttackFrom.owner== self and \
                countryAttackTo in countryAttackFrom.neighbors and \
                amountOfTroops-1 <= countryAttackFrom.numOfTroops and \
                amountOfTroops-1 > countryAttackTo.numOfTroops :
            self.attacking(self,countryAttackFrom,countryAttackTo,amountOfTroops)
        else:
            ctypes.windll.user32.MessageBoxW(0, "invalid attack", "ALERT", 1)
            

    def attacking(self,countryAttackFrom,countryAttackTo,amountOfTroops):
         countryAttackFrom.numOfTroops=countryAttackFrom.numOfTroops-amountOfTroops
         countryAttackTo=amountOfTroops
         countryAttackTo.owner = self
         









