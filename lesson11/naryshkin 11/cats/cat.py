import random

class Cat():

    def __init__(self, name,  age, weight, color, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.breed = breed
        self.initial_weight = weight

    def __str__(self):
        return f'name: {self.name}, age: {self.age}, weight: {self.weight}, color: {self.color}, breed: {self.breed}'

    def meow(self):
        print("Мяу!")

    def run(self):
        print("Бежит")
        if self.weight - 0.2 < self.initial_weight * 0.7:
            return

        self.weight -= 0.2

    def purr(self):
        print("Mrrrrr")

    def sleep(self):
        print("Zzzzzz")

    def eat(self):
        print("кушает")
        if self.weight + 0.2 > self.initial_weight * 2:
            return
        self.weight += 0.2

    def greet_human(self):
        random_number = random.random()
        if random_number > 0.5:
            self.run()
        else:
            self.sleep()

    def celebrate_birthday(self):
        self.age += 1
        print("вам кот стал на год старше")