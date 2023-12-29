# First task

from math import sqrt, pi, acos


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

# Доп. задания (now task 4)
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def direction_vector(self):
        return Point(
            self.point2.x - self.point1.x,
            self.point2.y - self.point1.y,
            self.point2.z - self.point1.z
        )

    @staticmethod
    def angle_between_lines(line1, line2):
        d1 = line1.direction_vector()
        d2 = line2.direction_vector()

        dot_product = (
            d1.x * d2.x +
            d1.y * d2.y +
            d1.z * d2.z
        )

        len_d1 = sqrt(d1.x**2 + d1.y**2 + d1.z**2)
        len_d2 = sqrt(d2.x**2 + d2.y**2 + d2.z**2)

        cos_angle = dot_product / (len_d1 * len_d2)

        angle = acos(cos_angle)

        return angle

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

    def angle_with_line(self, line):
        direction_vector = Point(
            line.point2.x - line.point1.x,
            line.point2.y - line.point1.y,
            line.point2.z - line.point1.z
        )

        normal_vector = self.normal_vector

        dot_product = abs(
            direction_vector.x * normal_vector.x +
            direction_vector.y * normal_vector.y +
            direction_vector.z * normal_vector.z
        )

        len_direction_vector = sqrt(
            direction_vector.x**2 +
            direction_vector.y**2 +
            direction_vector.z**2
        )
        len_normal_vector = sqrt(
            normal_vector.x**2 +
            normal_vector.y**2 +
            normal_vector.z**2
        )

        cos_angle = dot_product / (len_direction_vector * len_normal_vector)

        angle = pi/2 - acos(cos_angle)

        return angle

