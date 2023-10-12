# Inheritence 

class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with awesome fire blaze {self.power}')


class Archers(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} killer arrows !!')

wizard1 = Wizard('Merllin', 50)
archer1 = Archers('legolas', 1)
wizard1.attack()
archer1.sign_in()
