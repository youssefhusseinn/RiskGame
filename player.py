class player:

    def __init__(self, color,label):
        self.color=color
        self.countries=[]
        self.numberoftroops=20
        self.label=label
    def addcountry(self,country):
       self.countries.append(country)
    def decreasetroops(self,number):
        self.numberoftroops=self.numberoftroops-number
    def increasetroops(self,number):
        self.numberoftroops=self.numberoftroops+number