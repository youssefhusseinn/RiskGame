import random

from Country import *
import Human
from Human import *
DARKRED=(229,12,22)
DARKBLUE=(2,8,126)

class USGame():
    attack =[]


    def __init__(self):
       ## self.agents = [agent1, agent2]
       """"
"""


    def addelements(self,country,c101,redPlayer,bluePlayer):
        human= Human()
        flag1=False
        if country not in self.attack:
            self.attack.append(country)
        if len(self.attack) ==2:
            flag=human.attacking(self.attack[0],self.attack[1],c101,redPlayer,bluePlayer)
            if flag == True :
                flag1=True
        if len(self.attack)>=2:
            self.attack.clear()
        return flag1

