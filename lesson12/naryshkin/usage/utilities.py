class PhoneContact:
    def __init__(self, name, phone, work='', note=''):
        self.name = name
        self.phone = phone
        self.work = work
        self.note = note

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.work}, {self.note}"



class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Контакт не найден")

    def search_by_phone(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                print(contact)
                return
        print("Контакт не найден")

    def print_contacts(self):
        print("список контактов:")
        for contact in self.contacts:
            print(contact)

    def merge_contacts(self):
        pass

    def cdn(self): #check_for_duplicate_phone_numbers
        delete = []
        for i in range(len(self.contacts)):
            for j in range(i+1, len(self.contacts)):
                if self.contacts[i].phone == self.contacts[j].phone:
                    print(f"Контакты с номером {self.contacts[i].phone} повторяются")
                    self.contacts[i].work += self.contacts[j].work
                    self.contacts[i].note += self.contacts[j].note
                    delete.append(j)

        delete.sort(reverse=True)
        for i in delete:
            del self.contacts[i]