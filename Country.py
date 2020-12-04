class Country:

    def __init__(self, id):
        self.agent = None
        self.label = None
        self.neighbors = {}
        self.id = id

    def getNumberOfTroops(self) -> int:
        return self.agent.countries[self]
