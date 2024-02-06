class PhoneContact:
    def __init__(self, name, phone_number, work_place, notes,):
        self.name = name
        self.phone_number = phone_number
        self.work_place = work_place
        self.notes = notes
        self.contact_list = {"Роман": "+7-986-930-32-11",
                             "Никита": "+7-917-234-11-55",
                             "Артем": "+7-952-812-52-52"}

    def __str__(self):
        return f"Name: {self.name}, phone number: " \
               f"{self.phone_number}, work place: {self.work_place}, notes:{self.notes}"

    def get_number(self, name):
        pass

