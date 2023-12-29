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

