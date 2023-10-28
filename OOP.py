# Inheritence 

class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)
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

wizard1 = Wizard('Merllin', 50, '@email')
print(wizard1.email)

print(isinstance(wizard1, Wizard))

