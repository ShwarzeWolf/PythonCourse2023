class PhoneContact:

    def __init__(self, contact_name, phone_number, work_place='unspecified', note='unspecified'):
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.work_place = work_place
        self.note = note

    def __repr__(self):
        return f'Имя контакта: {self.contact_name},' \
               f' Номер телефона: {self.phone_number},' \
               f' Место работы: {self.work_place},' \
               f' Примечание: {self.note}.'

    def __eq__(self, other):
        return self.phone_number == other.phone_number

    def merge(self, other):
        if self.work_place == 'unspecified':
            self.work_place = other.work_place

        if self.note == 'unspecified':
            self.note = other.note


class PhoneBook:

    def __init__(self):
        self.contact_list = []

    def add_person(self, phone_contact):
        self.contact_list.append(phone_contact)

    def __str__(self):
        return f'{self.contact_list}'

    def search(self, search_request):
        searched_contacts = []
        for contact in self.contact_list:
            if contact.contact_name == search_request or contact.phone_number == search_request:
                searched_contacts.append(contact)

        print(searched_contacts)

    def merge_similars(self):
        clones = {}
        for i in range(len(self.contact_list)):
            for j in range(i + 1, len(self.contact_list)):
                if self.contact_list[i].phone_number == self.contact_list[j].phone_number:
                    clones[i] = j
                    self.contact_list[i].merge(self.contact_list[j])

        delete_list = []
        for original, clone in clones.items():
            delete_list.append(clone)

        delete_list.sort(reverse=True)

        for index in delete_list:
            self.contact_list.pop(index)


Tim1 = PhoneContact(contact_name='Тим', phone_number='+7(967)597-37-90')
Tim2 = PhoneContact(contact_name='Тимофей', phone_number='+7(967)597-37-90', work_place='Школа 617')
Tim3 = PhoneContact(contact_name='Тима', phone_number='+7(967)597-37-91', note='Хороший человек<з<з<з')

book = PhoneBook()
book.add_person(Tim1)
book.add_person(Tim2)
book.add_person(Tim3)

print(book)

book.search('Тима')

book.merge_similars()
print(book)
