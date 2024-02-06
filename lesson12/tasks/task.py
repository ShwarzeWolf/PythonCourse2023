class PhoneContact:
    def __init__(self, name, phone_number, work, info):
        self.name = name
        self.phone_number = phone_number
        self.work = work
        self.info = info

    def write_information(self):
        print(self.name, self.phone_number, self.work, self.info)

information = PhoneContact("Maksin", "7567575", "Yandex", "2008")

information.write_information()
