# First task

from math import sqrt


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

# Fourth task
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact_by_name(self, name):
        return [contact for contact in self.contacts if contact.name == name]

    def find_contact_by_phone(self, phone):
        return [contact for contact in self.contacts if contact.phone == phone]

    def merge_duplicate_numbers(self):
        unique_phones = {}
        for contact in self.contacts:
            if contact.phone in unique_phones:
                existing_contact = unique_phones[contact.phone]
                existing_contact.name = contact.name or existing_contact.name
                existing_contact.workplace = contact.workplace or existing_contact.workplace
                existing_contact.note = contact.note or existing_contact.note
            else:
                unique_phones[contact.phone] = contact
        self.contacts = list(unique_phones.values())

# Доп. задания (now task 2) (я изменил цифру, теперь у меня есть прогресс)
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

class Plane:
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector
    
    def distance_to_point(self, point):
        A = self.normal_vector.x
        B = self.normal_vector.y
        C = self.normal_vector.z
        D = self.D
        x = point.x
        y = point.y
        z = point.z

        num = abs(A * x + B * y + C * z + D)
        den = sqrt(A**2 + B**2 + C**2)

        return num / den

