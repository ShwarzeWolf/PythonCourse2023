class Vehicle:

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.model}, {self.year}, {self.price}"

    def display_info(self):
        print(f"model: {self.model}")
        print(f"year: {self.year}")
        print(f"price: {self.price}")

class Airplane(Vehicle):

    def __init__(self, model, year, price, range, passengers):
        super().__init__(model, year, price)
        self.range = range
        self.passengers = passengers

    def fly(self):
        print(f"{self.model} has {self.range} nm range")

    def display_info(self):
        super().display_info()
        print(f"range: {self.range}")
        print(f"passengers capacity: {self.passengers}")

class Car(Vehicle):

    def __init__(self, model, year, price, fuel_type, mileage, color):
        super().__init__(model, year, price)
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.color = color

    def drive(self):
        print(f"car {self.model} went KABOOM")

    def display_info(self):
        super().display_info()
        print("type: car")
        print(f"fuel type: {self.fuel_type}")
        print(f"mileage: {self.mileage} км")
        print(f"color: {self.color}")


my_plane = Airplane("Boeing 747", 2023, "N/A", 15000, 500)
my_plane.fly()
my_plane.display_info()

my_car = Car("Toyota Camry", 2023, 35000, "oil", 10000, "white")
my_car.drive()
my_car.display_info()

