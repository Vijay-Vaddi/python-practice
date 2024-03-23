from abc import ABC, abstractmethod
class Orders():
    items = []
    prices = []
    quantities = []
    status = 'open'

    def add_items(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    
    def total_price(self):
        total = 0
        for i in range(len(self.quantities)):
            total+= self.quantities[i]*self.prices[i]
        
        return total
    
class PaymentHandler(ABC):
    @abstractmethod
    def pay(self, order):
        pass
    
class DebitPaymentHandler(PaymentHandler):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
    def pay(self, order):
        print('processing debit type')
        print(f"verifying security code: {self.security_code}") 
        order.status = "paid"

class CreditPaymentHandler(PaymentHandler):
    def __init__(self, security_code) -> None:
        self.security_code = security_code
    
    def pay(self, order):
        print('processing credit type')
        print(f"verifying security code: {self.security_code}") 
        order.status = "paid"

class BitcoinPaymentHandler(PaymentHandler):
    def __init__(self, security_code) -> None:
        self.security_code = security_code

    def pay(self, order):
        print('processing bitcoin type')
        print(f"verifying security code: {self.security_code}") 
        order.status = "paid"

class PaypalPaymentHandler(PaymentHandler):
    def __init__(self, email) -> None:
        self.email = email

    def pay(self, order):
        print('processing bitcoin type')
        print(f"verifying security code: {self.email}") 
        order.status = "paid"


order = Orders()
order.add_items('Wooden Spoon', 1, 20)
order.add_items('A nice stick', 1, 0)
order.add_items('water', 1, 10)

print(order.total_price())
pay = PaypalPaymentHandler("hello@123")
pay.pay(order)

print(order.status)

