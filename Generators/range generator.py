# create range generator to be used for for loop

class MyGen():
    current_item = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    # need to use iter function ability to iterate through the object we're creating so
    def __iter__(self):
        return self
    # to return the object itself

    # iter needs the ability of next, to keep track of where we are 
    def __next__(self):
        if MyGen.current_item < self.last:
            num = MyGen.current_item
            MyGen.current_item+=1
            return num
        raise StopIteration

# instanciate object
gen = MyGen(0,100) 

for i in gen:
    print(i)

