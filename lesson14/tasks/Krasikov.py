class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    def display_info(self):
        print(f"Model: {self.model}, year: {self.year}, price: {self.price}")

class Airplane(Vehicle):
    def fly(self):
        print("Flying")

class Car(Vehicle):
    def display_info(self):
        print(f"Car Model: {self.model}, year: {self.year}, price: {self.price}")

car = Car("BMW", 2018, 10000)
car.display_info()
plane = Airplane("Boeing", 2000, 999999)
plane.display_info()