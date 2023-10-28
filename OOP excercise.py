class Pets():
    animals = []
    
    def __init__(self, animals) -> None:
        self.animals = animals
    
    
    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'

simon = Simon('Simon', 2)
sally = Sally('Sally', 1)
tom = Tom('Tom', 1)

my_cats = [simon,sally,tom]

pets = Pets(my_cats)
pets.walk()
