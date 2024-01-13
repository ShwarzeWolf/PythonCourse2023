class PhoneContact:
    def __init__(self, name, phone, work='---', about=None):
        self.name = name
        self.phone = phone
        self.work = work
        self.about = about or f'Его имя {self.name}'

    def __str__(self):
        return f'{self.name}: {self.phone}\nРабота: {self.work}\n{self.about}'


Bob = PhoneContact('Bob', '+7 921 123 45 67')
print(Bob)
print('\n---\n')


class PhoneBook:
    def __init__(self):
        self.contacts = dict()

    def add_contact(self, name, phone, work=None, about=None):
        if phone not in self.contacts.keys():  # Добавление контакта
            self.contacts.update({phone: [name, work, about]})
        elif None in (self.contacts[phone][1], self.contacts[phone][2]):  # Добавление информации
            contact = self.contacts[phone]
            if contact[1] is None:
                self.contacts.update({phone: [contact[0], work, contact[2]]})
                contact = self.contacts[phone]
            if contact[2] is None:
                self.contacts.update({phone: [contact[0], contact[1], about]})
        else:  # Обновление контакта
            self.contacts.update({phone: [name, work, about]})
        print(self.contacts)

    def search(self, value):
        flag = True
        for contact in self.contacts.items():
            if value in (contact[0], contact[1][0]):
                print(contact)
                flag = False
        if flag:
            print('Not found')


book = PhoneBook()
book.add_contact('Ann', '987 654 321')
book.add_contact('John', '123 456 789')
book.add_contact('John', '123 456 789', 'Student')
book.add_contact('Bob', '123 456 789', 'Another work', 'Something info')
book.add_contact('Bob', '123 456 789', 'Another work', 'Something info')

print('\n---\n')

book.search('John')
book.search('Bob')
book.search('987 654 321')
