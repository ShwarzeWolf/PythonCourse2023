class Vehicle():
    def __init__(self, model=None, year=2024, price=10**10):
        self.model = model
        self.year = year
        self.price = price
    def display_info(self):
        return (
            f"модель {self.model}, год {self.year}, цена {self.price}"
        )
    def __repr__(self):
        return self.display_info()

class Airplane(Vehicle):
    def fly(self):
        print("I'm flying")

class Car(Vehicle):
    def drive(self):
        print("I'm alive!")
    def display_info(self):
        return (
            f"модель {self.model}, год {self.year}, цена {self.price}, это машина"
        )

class GenBankParser():
    def parse(self, genBankString):
        isOriging = False
        origing = ""
        for line in genBankString.split("\n"):
            if isOriging:
                origing += line
            if line[:5] == "LOCUS":
                locus = line[12:]
            if line[:6] == "ORIGIN":
                isOriging = True
        return NucleotidesSequence(locus, origing)

class NucleotidesSequence():
    def __init__(self, locus, origing):
        self.origing = origing
        self.locus = locus
    def __repr__(self):
        return f"locus: {self.locus}\noriging: \n{self.origing}"

a = GenBankParser()
file = open("GenBankFile.txt", "r")
print(a.parse(file.read()))
