from random import random


class Cat:
    def __init__(self, age, weight, color, breed=None):
        """
        Initialize the Cat instance with given parameters.

        Args:
            age (int): The age of the cat.
            weight (float): The weight of the cat in kilograms.
            color (str): The color of the cat.
            breed (str, optional): The breed of the cat. Defaults to None.
        """
        self.age = age
        self.weight = weight
        self.color = color
        self.breed = breed

    def run(self):
        print("I'm running!")
        new_weight = self.weight - 0.2
        self.weight = self._correct_weight(new_weight)

    def eat(self):
        print("Mmm, tasty!")
        new_weight = self.weight + 0.2
        self.weight = self._correct_weight(new_weight)

    def purr(self):
        print("Mrrrrr")

    def sleep(self):
        print("Zzzzzzzz")

    def greet_human(self):
        print("Hi! meow")
        choice = random()
        if choice > 0.5:
            self.run()
        else:
            self.sleep()

    def celebrate_birthday(self):
        print("Woohoo! Birthday!")
        self.age += 1

    def _correct_weight(self, new_weight):
        old_weight = self.weight
        if 2 > new_weight / old_weight > 0.7:
            return new_weight
        else:
            return old_weight


if __name__ == "__main__":
    cat = Cat(
        age=3,
        weight=0.4,
        color="brown",
        breed="Bengal",
    )

    cat.greet_human()
