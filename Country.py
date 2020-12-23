class Country:
    def __init__(self, id):
        self.numOfTroops = 0
        self.owner = None
        self.neighbors = []
        self.id = id
        self.ownerboolean=False

    def addTroops(self, amount):
        self.numOfTroops += int(amount)

    def addBonusTroops(self,amount):
        self.numOfTroops+=int(amount)
        self.owner.bonusTroops-=1
        print("Owner bonus troops: ")
        print(self.owner.bonusTroops)
        print("************")
