def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."

def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number is {contacts[name]}"
    else:
        return f"Contact {name} not found."

def all(args,contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_contact(args, contacts))
            elif command == "all":
                print(all(args, contacts))
            else:
                print("Invalid command.")
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
