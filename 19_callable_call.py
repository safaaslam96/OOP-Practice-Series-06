class Multiplier:
    def __init__(self, factor):
        self.factor = factor


    def __call__(self, value):
        return self.factor * value
    
m = Multiplier(5)

# check if m is callable
print(callable(m)) # output true
print (m(10)) # output 50
        