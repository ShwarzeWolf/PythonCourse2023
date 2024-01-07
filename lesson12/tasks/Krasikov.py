class PhoneContact:
    def __init__(self, name, phone, work_place="", note=""):
        self.id = 0
        self.name = name
        self.phone = phone
        # if work_place != "":
        self.work_place = work_place
        # if note != "":
        self.note = note

    def __str__(self):
        return f"Name: {self.name}, phone: {self.phone}{f', work place: {self.work_place}' if self.work_place != '' else ''}{f', note: {self.note}' if self.note != '' else ''}"

    def __eq__(self, contact):
        if self.phone == contact.phone:
            return 1
        else:
            return 0


class PhoneBook:
    def __init__(self, *args):
        self.contact_list = []
        for contact in args:
            self.add(contact)

    def __repr__(self):
        return str([contact.__str__() for contact in self.contact_list])

    def add(self, contact):
        contact.id = len(self.contact_list)
        self.contact_list.append(contact)

    def delete(self, contact):
        del self.contact_list[contact.id]
        self.re_id()

    def search_by_name(self, name):
        return [contact for contact in self.contact_list if contact.name == name][0]

    def search_by_phone(self, phone):
        return [contact for contact in self.contact_list if contact.phone == phone][0]

    def re_id(self):
        for i in range(len(self.contact_list)):
            self.contact_list[i].id = i

    def delete_duplicates(self):
        for contact1 in self.contact_list:
            for contact2 in self.contact_list[1:]:
                if contact1.id == contact2.id:
                    continue
                if contact1 == contact2:
                    print(contact1, " = ", contact2)
                    if contact2.work_place != "" and contact1.work_place == "":
                        contact1.work_place = contact2.work_place
                    if contact2.note != "" and contact1.note == "":
                        contact1.note = contact2.note
                    self.delete(contact2)


me = PhoneContact("Sasha", "89315310681", note="Student")
print(me)
someone = PhoneContact("Misha", "123456789", "IT center")
phoneBook = PhoneBook(me, someone)
print(phoneBook.search_by_name("Misha"))
print(phoneBook.search_by_phone("89315310681"))
phoneBook.add(PhoneContact("Misha", "123456789", note="Friend"))
print(phoneBook)
phoneBook.delete_duplicates()
print(phoneBook)