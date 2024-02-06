import time
import random

class Cat:
    def __init__(self, name, age, weight, color, breed):
        self.name = name
        self.age = age
        self.start_weight = weight
        self.weight = weight
        self.color = color
        self.breed = "metis"

    def get_data(self):
        return self.name, self.age, self.weight, self.color, self.breed

    def run(self):
        print(f"{self.name} is running")
        if (self.weight - 0.2) / self.start_weight >= 0.7:
            self.weight -= 0.2

    def mur(self):
        print(f"{self.name} says muuurrrrrr")

    def sleep(self, sleep_time):
        print(f"{self.name} is going to sleep for {sleep_time} seconds")
        for i in range(sleep_time):
            print("Zzzzzzzz")
            time.sleep(1)

    def eat(self, food="fish"):
        print(f"{self.name} is eating {food}")
        if (self.weight + 0.2) / self.start_weight <= 2:
            self.weight += 0.2

    def greet_human(self):
        if random.random() > 0.5:
            self.run()
        else:
            self.sleep(3)

    def celebrate_birthday(self):
        print(f"It's {self.name}'s birthday!")
        self.age += 1

cat = Cat("Barsik", 2, 5, "white", "bengal")
cat.greet_human()
print(cat.get_data())
cat.mur()
cat.run()
print(cat.get_data())
cat.eat("meat")
cat.celebrate_birthday()
print(cat.get_data())
cat.sleep(3)