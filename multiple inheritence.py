class User():
    def signin(self):
        print (f'Signed in')
    

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    
    def attack(self):
        print(f'Wizard {self.name} attacked with power of {self.power}')
    

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows     
    
    
    def check_arrows(self):
        print(f'Archer {self.name} attacked with power of {self.arrows}')
    

    def run(self):
        print(f'ran really fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hb1 = HybridBorg('Borgie', 50, 100)
# the first elements passed will correspond to the arguments of first class being inherited. 
# (borgie, 50) --> name, power of Wizard, not archer. 
print(hb1.attack())
