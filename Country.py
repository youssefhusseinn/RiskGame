class Country:
    def __init__(self, id):
        self.numOfTroops = 0
        self.owner = None
        self.neighbors = []
        self.id = id
        self.ownerboolean = False

    def addTroops(self, amount):
        self.numOfTroops += int(amount)
