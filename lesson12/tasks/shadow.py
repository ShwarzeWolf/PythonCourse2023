# First task

class PhoneContact:
    def __init__(self, name, phone, workplace=None, note=None):
        self.name = name
        self.phone = phone
        self.workplace = workplace
        self.note = note

# Second task
class PhoneContact:
    def __init__(self, name, phone, workplace=None, note=None):
        self.name = name
        self.phone = phone
        self.workplace = workplace
        self.note = note

    def __str__(self):
        contact_str = f"Name: {self.name}, Phone: {self.phone}"
        if self.workplace:
            contact_str += f", Workplace: {self.workplace}"
        if self.note:
            contact_str += f", Note: {self.note}"
        return contact_str

# Third task
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact_by_name(self, name):
        return [contact for contact in self.contacts if contact.name == name]

    def find_contact_by_phone(self, phone):
        return [contact for contact in self.contacts if contact.phone == phone]

