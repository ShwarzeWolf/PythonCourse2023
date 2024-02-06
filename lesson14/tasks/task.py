class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Машина: {self.model} {self.year} : {self.price}")

class Airplane:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Самолёт: {self.model} {self.year} : {self.price}")

my_car = Vehicle("BMW M5 F90", "2023", "10.000.000")
my_air = Airplane("Airbull", "2020", "1000000000")
my_car.display_info()
my_air.display_info()