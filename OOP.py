# Inheritence 

class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    pass


class Archers(User):
    pass

wizard1 = Wizard()
print(wizard1.sign_in())
