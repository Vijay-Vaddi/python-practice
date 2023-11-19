# implement a fibinacci generator
# 
class Fibonacci():
        
    def __init__(self, num):
        self.num = num
        self.items = 0
        self.num1, self.num2 = 0, 1
         

    def __iter__(self):
        return self
    

    def __next__(self):
        if self.items < self.num:
            result = self.num1
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.items+=1
            return result
        raise StopIteration

fib = Fibonacci(10)

for i in fib:
    print(i)
