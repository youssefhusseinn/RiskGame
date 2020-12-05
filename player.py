class player:
    numberoftroops=20
    listofmycountries=[]
    def __init__(self, color):
        self.color=color
    def addtomycountries(self,country):
       self.listofmycountries.append(country)
    def decreasetroops(self,number):
        self.numberoftroops=self.numberoftroops-number
    def increasetroops(self,number):
        self.numberoftroops=self.numberoftroops+number