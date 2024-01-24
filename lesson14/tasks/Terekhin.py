class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(
            f'Модель - {self.model}\n'
            f'Год выпуска - {self.year}\n'
            f'Цена - {self.price}'
        )


class Airplane(Vehicle):
    def __init__(self, model, year, price, max_height):
        super().__init__(model, year, price)
        self.max_height = max_height

    def fly(self):
        print(f'Now {self.max_height}m from surface!')

    def display_info(self):
        print(
            f'Модель - {self.model}\n'
            f'Год выпуска - {self.year}\n'
            f'Цена - {self.price}\n'
            f'Максимальная высота полёта - {self.max_height}'
        )


class Car(Vehicle):
    def display_info(self):
        print(
            'Тип транспорта - машина\n'
            f'Модель - {self.model}\n'
            f'Год выпуска - {self.year}\n'
            f'Цена - {self.price}'
        )


vehicle = Vehicle('BMV', 2019, 2_000_000)
vehicle.display_info()
airplane = Airplane('Boing-737', 2010, 10_006_762_000, 11277)
airplane.fly()
airplane.display_info()
car = Car('BMV', 2019, 2_000_000)
car.display_info()
