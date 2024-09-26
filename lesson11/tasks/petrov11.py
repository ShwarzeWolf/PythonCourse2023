class cat():
    def __init__(self, age=-1, weight=-1, color="", breed=""):
        self.age = age
        self.weight = weight
        self.color = color
        cat.breed = breed
    def eat(self, quantity=1):
        if self.weight < 2:
            self.weight += quantity*0.2
            return 0
        else:
            return 1
    def run(self, quanity=1):
        if self.weight > 0.7:
            self.weight -= quanity*0.2
            return 0
        else:
            return 1
