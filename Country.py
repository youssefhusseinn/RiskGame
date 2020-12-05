BLACK = (0, 0, 0)


class Country:

    def __init__(self, id,label):
        #self.agent = None
        self.label = label
        self.neighbors = {}
        self.id = id
        self.color=BLACK
        self.troops=0

    def getNumberOfTroops(self) -> int:
        return self.agent.countries[self]
