import math

class player:

    def __init__(self, color,label):
        self.color=color
        self.countries=[]
        self.numberoftroops=20
        self.label=label
        self.bonustroops=0
        if(len(self.countries)/3 <= 3):
            self.bonustroops= 3
        else:
            self.bonustroops=int(len(self.countries)/3)
    def setbonustroops(self):
        if (len(self.countries) / 3 <= 3):
            self.bonustroops = 3
        else:
            self.bonustroops= math.floor(len(self.countries) / 3)

    def addcountry(self,country):
       self.countries.append(country)
    def decreasetroops(self,number):
        self.bonustroops=self.bonustroops-number
    def increasetroops(self,number):
        self.numberoftroops=self.numberoftroops+number