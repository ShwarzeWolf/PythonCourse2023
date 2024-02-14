from  random import random


class Cat:
    def __init__(self, age, mass, colour, breed):
        self.age = age
        self.mass = mass
        self.colour = colour
        self.breed = breed

    def to_run(self):
        if (self.mass - 200) >= (0.7 * self.mass):
            self.mass -= 200
        print("Im runing")

    def to_purr(self):
        print("Mrrrr")

    def to_sleep(self):
        print("Zzz")

    def to_eat(self):
        if (self.mass + 200) <= (2 * self.mass):
            self.mass += 200
        print("So tasty!")

    def greet_human(self):
        n = random()
        if n > 0.5:
            self.to_run()
        else:
            self.to_sleep()

    def celebrate_birthday(self):
        self.age += 1