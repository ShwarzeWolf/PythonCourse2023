from time import sleep


class Cat:
    def __init__(self, age, weight, colour, breed='mongrel'):
        self.age = age
        self.weight = weight
        self.start_weight = weight
        self.colour = colour
        self.breed = breed

    def eat(self):
        print('Om-nom-nom')
        if self.weight + 200 < 2 * self.start_weight:
            self.weight += 200

    def run(self):
        print('(^◕ᴥ◕^)')
        for i in range(10):
            print('  '*i + '...(^◕ᴥ◕^)')
            sleep(0.2)
        if self.weight - 200 > 0.7 * self.start_weight:
            self.weight -= 200


Stepa = Cat(3, 2000, 'orange')

print(Stepa.weight, 'г')
Stepa.eat()
Stepa.eat()
print(Stepa.weight, 'г')
Stepa.run()
print(Stepa.weight, 'г')
