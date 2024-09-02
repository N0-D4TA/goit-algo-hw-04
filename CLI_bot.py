# Parser section
def parse_input(user_input: str) -> str | list:
        cmd, *args = user_input.split()
        cmd = cmd.strip().casefold()
        return cmd, *args

# Handler section
def add_contact(args: list, contacts: dict):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Error: Contact not found!"

def show_phone(args, contacts: dict):
    name = str(args)
    if name in contacts.keys():
        return f"Phone number: {contacts.get(name)}"
    else:
        return "Error: Contact not found!"

def show_all(contacts: dict):
    for name, phone in contacts.items():
        yield f"{name}, {phone}"

# Interface
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
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
            print(show_phone(args, contacts))
        elif command == "all":
            # Unpacking list adding new line separator
            for contact in show_all(contacts):
                print(contact)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()