class Orders():
    items = []
    prices = []
    quantities = []
    status = open

    def add_items(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    
    def total_price(self):
        total = 0
        for i in range(len(self.quantities)):
            total+= self.quantities[i]*self.prices[i]
        
        return total

    def pay(self, payment_type, security_code):
        if payment_type == 'debit':
            print('processing debit type')
            print(f"verifying security code: {security_code}") 
            self.status = "paid"
        elif payment_type == 'credit':
            print('processing credit type')
            print(f"verifying security code: {security_code}") 
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")
        

order = Orders()
order.add_items('Wooden Spoon', 1, 20)
order.add_items('A nice stick', 1, 0)
order.add_items('water', 1, 10)

print(order.total_price())

