class PhoneContact:
    def __init__(self, name, phone, workPlace="", notes=""):
        self.name = name
        self.phone = phone
        self.workPlace = workPlace
        self.notes = notes
    def __repr__(self):
        return (f"name: {self.name}, phone: {self.phone}, place of work: {self.workPlace}, notes: {self.notes}")
    def __eq__(self, other):
        return (self.phone == other.phone)
    def __add__(self, other):
        return PhoneContact(name=self.name+other.name,
                            phone=other.phone,
                            workPlace=self.workPlace+other.workPlace,
                            notes=self.notes+other.notes)

class PhoneBook:
    def __init__(self):
        self._contacts = []
    def __repr__(self):
        ans = ""
        for i in self._contacts:
            ans += i.__repr__()
            ans += "\n"
        return ans
    @property
    def contacts(self):
        return self._contacts
    @contacts.setter
    def contacts(self, newContact):
        self._contacts.append(newContact)
    def NameFind(self, name):
        for i in self._contacts:
            if i.name == name:
                return i
    def PhoneFind(self, phone):
        for i in self._contacts:
            if i.phone == phone:
                return i
    def union(self, other):
        for i in range(len(self._contacts)):
            if self._contacts[i] == other:
                self._contacts[i] = self._contacts[i] + other

a = PhoneContact("vasya", 123)
b = PhoneContact("vanya", 456)

book = PhoneBook()
book.contacts = a
book.contacts = b
print(book)

print(book.NameFind("vanya"))
print(book.PhoneFind(123))

c = PhoneContact("1", 123, "apple", "cool")
book.union(c)

print(book)