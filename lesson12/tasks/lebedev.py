class PhoneContact:
    def __init__(self, name, phone_number, job=None, description=None) -> None:
        self.name = name
        self.phone_number = phone_number
        self.job = job
        self.description = description
    
    def __repr__(self) -> str:
        name_field = f"name: {self.name}"
        phone_number_field = f"phone_number: {self.phone_number}"
        job_field = f"job: {self.job}" if self.job else ""
        description_field = f"description: {self.description}" if self.description else ""
        return f"PhoneContact({name_field}, {phone_number_field}, {job_field}, {description_field})"
    
    def unite_with_contact(self, other):
        assert isinstance(other, PhoneContact), f"Can't unite PhoneContact with {type(other)}"
        assert self.phone_number == other.phone_number, \
            "To unite PhoneContact instances they should have the same phone number"
        
        if not self.job and not other.job:
            concatenated_job = None
        else:
            concatenated_job = (self.job or "") + " | " + (other.job or "")
        
        if not self.description and not other.description:
            concatenated_description = None
        else:
            concatenated_description = (self.description or "") + " | " + (other.description or "")
            
        self.name += " | " + other.name
        self.job = concatenated_job
        self.description = concatenated_description


class PhoneBook:
    def __init__(self, *contacts) -> None:
        self.contacts: list[PhoneContact] = list(contacts)
    
    def __repr__(self) -> str:
        contacts_string = "\n".join(["\t" + repr(contact) for contact in self.contacts])
        return "PhoneBook {\n" + contacts_string + "\n}"

    def search_by_name(self, searched_name):
        found = filter(lambda contact: contact.name == searched_name, self.contacts)
        return list(found)
    
    def search_by_phone(self, searched_phone_number):
        found = filter(lambda contact: contact.phone_number == searched_phone_number, self.contacts)
        return list(found)
    
    def unite_contacts(self):
        contacts_by_phone: dict[str, PhoneContact] = {}
        for contact in self.contacts:
            phone = contact.phone_number
            if phone not in contacts_by_phone:
                contacts_by_phone[phone] = contact
            else:
                contacts_by_phone[phone].unite_with_contact(contact)
        
        self.contacts = list(contacts_by_phone.values())


if __name__ == "__main__":
    # Создание нескольких экземпляров класса PhoneContact
    contact1 = PhoneContact("Иванов", "12345", "Менеджер", "Рабочий телефон")
    contact2 = PhoneContact("Петров", "54321", "Аналитик", "Личный телефон")
    contact3 = PhoneContact("Сидоров", "12345", "Разработчик", "Основной контакт")

    # Создание экземпляра класса PhoneBook с тестовыми контактами
    phone_book = PhoneBook(contact1, contact2, contact3)

    print(phone_book)

    phone_book.unite_contacts()

    print()

    print(phone_book)
