from Agent import *
import Country
from Country import *
import ctypes
import threading

class Human(Agent):

    def canAttack(self, countryAttackFrom, countryAttackTo, amountOfTroops):
        if countryAttackFrom.owner == self and countryAttackTo in countryAttackFrom.neighbors \
                and amountOfTroops < countryAttackFrom.numOfTroops and amountOfTroops >= countryAttackTo.numOfTroops:
            return True
        else:
            return False
            

    def attack(self, countryAttackFrom, countryAttackTo, amountOfTroops):
         if amountOfTroops== 0:
          return True
         flag=self.canAttack(countryAttackFrom,countryAttackTo,amountOfTroops)
         if flag:
            useTimer=False
            if useTimer:
                temp_num_from=countryAttackFrom.numOfTroops
                temp_num_to=countryAttackTo.numOfTroops
                t = threading.Timer(0, self.setTroops,args=(countryAttackTo, countryAttackFrom, temp_num_to, temp_num_from,amountOfTroops))
                t.start()
                countryAttackFrom.numOfTroops = str(countryAttackFrom.numOfTroops) + 'A'
                countryAttackTo.numOfTroops = str(countryAttackTo.numOfTroops) + "D"
            else:
                countryAttackFrom.numOfTroops = countryAttackFrom.numOfTroops - amountOfTroops
                countryAttackTo.numOfTroops = amountOfTroops
                countryAttackTo.owner.removeCountry(countryAttackTo)
                countryAttackTo.owner = self
                countryAttackTo.owner.countries.append(countryAttackTo)
            return True
         else:
            ctypes.windll.user32.MessageBoxW(0, "invalid attack PLEASE TRY AGAIN", "ALERT", 1)
            return False
     
    def setTroops(self,country_to,country_from,num_to,num_from,amountOfTroops):
        country_to.numOfTroops=num_to
        country_from.numOfTroops=num_from
        country_from.numOfTroops = country_from.numOfTroops - amountOfTroops
        country_to.numOfTroops = amountOfTroops
        country_to.owner.removeCountry(country_to)
        country_to.owner = self
        country_to.owner.countries.append(country_to)









