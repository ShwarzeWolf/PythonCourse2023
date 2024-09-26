class Vehicle:

    def __init__(self, model=None, year=None, price=None):
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f'model: {self.model} | year: {self.year} | price: {self.price}')


class Airplane(Vehicle):
    def __init__(self, model=None, year=None, price=None, engine_capacity=None):
        super().__init__(model, year, price)
        self.engine_capacity = engine_capacity
        self.state = 'landed'

    def display_info(self):
        print(
            f'model: {self.model} | year: {self.year} | price: {self.price} | engine_capacity: {self.engine_capacity} |'
            f' state: {self.state}')

    def fly(self):
        if self.state == 'flying':
            print('Already flying')
        else:
            self.state = 'flying'
            print('Took off')

    def land(self):
        if self.state == 'landed':
            print('Already on the land')
        else:
            self.state = 'landed'
            print('Landed')


class Car(Vehicle):

    def __init__(self, model=None, year=None, price=None, top_speed=None):
        super().__init__(model, year, price)
        self.top_speed = top_speed
        self.fuel = 200

    def display_info(self):
        print(f'Vehicle_type: Car | model: {self.model} | year: {self.year} | price: {self.price} | '
              f'top_speed: {self.top_speed}')

    def drive(self):
        if self.fuel == 0:
            print('You need to visit filling station')
        else:
            self.fuel -= 10
            print('*Driving*')
            print(f'Fuel: {self.fuel}')

    def fill_fuel(self):
        self.fuel = 200


print('')
print('Vehicle:')
vehicle = Vehicle('2.3.1', 2019, 10_000)

vehicle.display_info()

print('')
print('Airplane:')
plane = Airplane('5.1.6', 2021, 120_000, 1_500)

plane.display_info()
plane.fly()
plane.display_info()
plane.land()
plane.display_info()

print('')
print('Car:')

car = Car('4.7.3', 2015, 15_000, 240)

car.display_info()
for _ in range(21):
    car.drive()

car.fill_fuel()
car.drive()
