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

    def addbonustroops(self,country,c102,c101,redPlayer,bluePlayer):
        if c101.label== "RED PLAYER" and country.owner == redPlayer and redPlayer.bonustroops > 0 :
             country.setNumOfTroops(int(country.troops) +1)
             redPlayer.decreasetroops(1)
             c102.setNumOfTroops(redPlayer.bonustroops)
        elif  c101.label== "BLUE PLAYER" and country.owner == bluePlayer and bluePlayer.bonustroops > 0:
             country.setNumOfTroops(int(country.troops) + 1)
             bluePlayer.decreasetroops(1)
             c102.setNumOfTroops(bluePlayer.bonustroops)




    def addelements(self,country,c102,c101,redPlayer,bluePlayer):
        human= Human()
        flag1=False
        if country not in self.attack:
            self.attack.append(country)
        if len(self.attack) ==2:
            if (redPlayer.bonustroops==0 and c101.label=="RED PLAYER") or (bluePlayer.bonustroops==0 and c101.label=="BLUE PLAYER"):
                 flag=human.attacking(self.attack[0],self.attack[1],c101,redPlayer,bluePlayer)
                 if flag == True:
                     if (c101.label == "RED PLAYER"):
                       c102.setlabel(str(bluePlayer.bonustroops))
                       c102.color = bluePlayer.color
                       c102.setOwner(bluePlayer)
                       c102.setNumOfTroops(bluePlayer.bonustroops)
                     else:
                       c102.setlabel(str(redPlayer.bonustroops))
                       c102.color = redPlayer.color
                       c102.setOwner(redPlayer)
                       c102.setNumOfTroops(redPlayer.bonustroops)

                     flag1=True
            else:
                print("you should place all bonus troops first")
                self.attack.clear()
                return  False
        if len(self.attack)>=2:
            self.attack.clear()
        return flag1

