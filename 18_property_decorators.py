class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price....")
        del self._price

p = Product(100)
print(p.price) # output: 100

p.price = 150
print(p.price) # output: 150

del p.price # output deleting price...
    
        