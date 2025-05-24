class Car:
    def __init__(self, brand):
      self.brand = brand 
      
    def strat(self):
       print(f"{self.brand} is starting")
          
my_car = Car("Porsche")
print(my_car.brand)
my_car.start()
        