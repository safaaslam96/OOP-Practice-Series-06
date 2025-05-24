class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        self.current = self.start # reset for iteration
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -=1
        return value
    
cd = Countdown(5)

for num in cd:
    print (num)
        