from Agent import *
import Country
from Country import *

class Human:


    def attacking(self,country0,country1):

        if((country0.troops-1 >= country1.troops ) and (country0.owner != country1.owner) and (country1 in country0.neighbors)):
            country1.setNumOfTroops(country0.troops-1)
            country1.setOwner(country0.owner)
            country0.setNumOfTroops(1)
            return True
        else:
            print("you can not do this attack")
            return False







