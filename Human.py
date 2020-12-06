from Agent import *
import Country
from Country import *

class Human:


    def attacking(self,country0,country1):

        if((country0.troops-1 >= country1.troops ) and (country0.owner != country1.owner) and (country1 in country0.neighbors)):
            val = input("Enter amount of troop you want to attack with: ")
            if(int(val)<=country0.troops-1 and int(val) >= country1.troops ):
                country1.setNumOfTroops(val)
                country1.setOwner(country0.owner)
                country0.setNumOfTroops(country0.troops-int(val))
                return True
            else:
                print("invalid amount of troops")
                return False
        else:
            print("you can not do this attack")
            return False







