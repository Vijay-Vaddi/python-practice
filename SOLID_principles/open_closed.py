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
    def pay(self, order, security_code):
        pass
    
class DebitPaymentHandler(PaymentHandler):
    def pay(self, order, security_code):
        print('processing debit type')
        print(f"verifying security code: {security_code}") 
        order.status = "paid"

class CreditPaymentHandler(PaymentHandler):
    def pay(self, order, security_code):
        print('processing credit type')
        print(f"verifying security code: {security_code}") 
        order.status = "paid"

class BitcoinPaymentHandler(PaymentHandler):
    def pay(self, order, security_code):
        print('processing bitcoin type')
        print(f"verifying security code: {security_code}") 
        order.status = "paid"

order = Orders()
order.add_items('Wooden Spoon', 1, 20)
order.add_items('A nice stick', 1, 0)
order.add_items('water', 1, 10)

print(order.total_price())
pay = BitcoinPaymentHandler()
pay.pay(order, 200)

print(order.status)

