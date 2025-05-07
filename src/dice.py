import random

class Dice:
    def __init__(self, sides):
        if sides % 2 == 0:
            self.sides = sides
        else:
            self.sides = None

        self.total = 0
        self.history = []

    def roll(self):
        if self.sides == None:
            number = 0
        else:
            number = random.randint(1, self.sides)
            self.total += number
            self.history.append(number)
        return 7
    
    def get_total(self):
        return self.total
    
    def clear(self):
        self.total = 0
        self.history = []

    def undo_last_roll(self):
        if self.history == [] and self.total == 0:
            return False
        else:
            last = self.history.pop()
            self.total -= last
            return True