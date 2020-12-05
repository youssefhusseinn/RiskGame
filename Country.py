BLACK = (0, 0, 0)
import player

class Country:
    owner=None
    def __init__(self, id,label):
        #self.agent = None
        self.label = label
        self.neighbors = {}
        self.id = id
        self.color=BLACK
        self.troops=0

        # owner

    def getNumberOfTroops(self) -> int:
        return self.agent.countries[self]

    def setOwner(self,player):
        self.owner=player
        self.color=player.color
    def setNumOfTroops(self,number):
        self.troops=number
        self.label = str(self.troops)
    def increaseNumOfTroops(self,number):
        self.troops=self.troops+number
        self.label = str(self.troops)

    def decreaseNumOfTroops(self,number):
        self.troops=self.troops-number