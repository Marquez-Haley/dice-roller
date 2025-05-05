import random

class Dice:
    def __init__(self, sides):
        if sides % 2 == 0:
            self.sides = sides
        else:
            self.sides = None

        self.total = 0

    def roll(self):
        if self.sides == None:
            number = 0
        else:
            number = random.randint(1, self.sides)
            self.total += number
        return number
    
    def get_total(self):
        return self.total
    
    def clear(self):
        self.total = 0