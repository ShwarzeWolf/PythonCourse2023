from cats import cat

def print_commands():
    commands = [
        ("help", "выводит список актуальных комманд"),
        ("meow", "мяукает"),
        ("run", "бежит"),
        ("purr", "мурлычет"),
        ("sleep", "спит"),
        ("eat", "кушает"),
        ("greet human", "встречает человека (либо спит либо бежит)"),
        ("celebrate birthday", "прибавляет год к возрасту кота"),
        ("exit", "завершаяет программу"),

    ]

    for command, description in commands:
        print(f"{command} - {description}")

if __name__ == "__main__":
    name = input("дайте имя вашему коту: ")
    age = int(input("задайте возраст вашему коту: "))
    weight = float(input("задайте вес вашему коту: "))
    color = input("задайте цвет вашему коту: ")
    breed = input("задайте породу вашему коту: ")
    kot = cat.Cat(name, age, weight, color, breed)
#    print(kot)  # проверка заданных значений


    while True:
        command = input()
        if command == "help":
            print_commands()
        elif command == "meow":
            kot.meow()
        elif command == "run":
            kot.run()
        elif command == "purr":
            kot.purr()
        elif command == "sleep":
            kot.sleep()
        elif command == "eat":
            kot.eat()
        elif command == "greet human":
            kot.greet_human()
        elif command == "celebrate birthday" or command == "birthday" or command == "celebrate":
            kot.celebrate_birthday()
        elif command == "exit":
            break
        elif command == "dev test":
            print(kot) #проверка текущих значений
        else:
            print("not valid command, use 'help' to see the list of commands")
