import random


class Cat:

    def __init__(self, age, weight, colour, breed='unknown'):
        self.age = age
        self.weight = weight
        self.start_weight = weight
        self.colour = colour
        self.breed = breed

    def run(self):
        if self.weight - 0.2 >= self.start_weight * 0.7:
            self.weight -= 0.2
        print("*Top-top-top*")

    def mur(self):
        print('*Mrrrrrr*')

    def sleep(self):
        print('*Zzzzzzzzz*')

    def eat(self):
        if self.weight + 0.2 < self.start_weight * 2:
            self.weight += 0.2
        print('*Nyam-nyam*')

    def greet_human(self):
        energy = random.randint(0, 1)

        if energy > 0.5:
            self.run()
        else:
            self.eat()
            self.sleep()


Elfa = Cat(age=8, weight=9, colour='orange')

for day in range(30):
    print(f'day {day + 1}:')
    Elfa.greet_human()
    print(f'weight: {Elfa.weight}kg')

print(f'WEIGHT: {Elfa.weight}kg')