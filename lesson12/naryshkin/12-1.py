from usage import utilities

if __name__ == "__main__":
    book = utilities.PhoneBook()

    book.add_contact(utilities.PhoneContact("Иван Иванов", "+7 (912) 333-33-33"))
    book.add_contact(utilities.PhoneContact("Петр Петров", "+7 (911) 222-22-22"))
    book.add_contact(utilities.PhoneContact("Иван Иванов", "+7 (912) 333-33-33"))
    book.add_contact(utilities.PhoneContact("Петр Петров", "+7 (911) 222-22-22"))

    book.cdn()
    book.search_by_name("Петр Петров")
    book.search_by_phone("+7-923-456-78-90")
    book.print_contacts()
