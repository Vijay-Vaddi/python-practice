class MyArray():
    
    def __init__(self, capacity) -> None:
        self.data = [None]*capacity
        self.len = 0
        self.capacity = capacity
    
    def lenght(self):
        return self.len
    
    def addItem(self, item):
        if self.len == self.capacity:
            self._resize(self.capacity*2)
        self.data[self.len] = item
        self.len = self.len+1

    def popItem(self):
        if self.len == 0:
            return 'There doesn\'t seem to be anything here'
        else: 
            self.data[self.len-1] = None
            self.len = self.len-1

    def _resize(self, new_capacity):
        print('Overflow, resizing array')
        new_data = [None]*new_capacity
        for i in range(self.len):
            new_data[i] = self.data[i]
        self.capacity= new_capacity
        self.data = new_data

newlist = MyArray(3)
newlist.addItem(5)
newlist.addItem(5)
newlist.addItem(5)
newlist.addItem(6)
newlist.popItem()


print(newlist.data) 


