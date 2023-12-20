import random

class Cat:
    def __init__(self, age, mass, fur_color, breed):
        self.age = age
        self.mass = mass
        self.initial_mass = mass
        self.fur_color = fur_color
        self.breed = breed

    def run(self):
        potential_mass = self.mass - 0.2
        if potential_mass >= 0.7 * self.initial_mass:
            self.mass = potential_mass
        print(f"Кот пробежал и теперь весит {self.mass:.2f} kg.")

    def purr(self):
        print("Mrrrrr")

    def sleep(self):
        print("Zzzzzz")

    def eat(self):
        potential_mass = self.mass + 0.2
        if potential_mass <= 2 * self.initial_mass:
            self.mass = potential_mass
        print(f"Кот поел и теперь весит {self.mass:.2f} kg.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"С днём рождения! Теперь коту {self.age} лет.")

    def greet_human(self):
        value = random.random()
        if value > 0.5:
            self.run()
        else:
            self.sleep()