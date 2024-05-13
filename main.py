
from adress_book_class import AddressBook
from contacts_utills import add_birthday, add_contact, birthdays, change_contact, all_contacts, show_birthday, show_phone


def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:


            case "close" | "exit":
                print("Good bye!")
                break
            
            case  "hello":
                print("How can I help you?")

            case   "add":
                print(add_contact(args, book))

            case "change":
                print(change_contact(args, book))

            case  "phone":
                print(show_phone(args, book))

            case  "all":
                print(all_contacts(book))

            case  "add-birthday":
                print(add_birthday(args, book))

            case  "show-birthday":
                print(show_birthday(args, book))

            case  "birthdays":
                print(birthdays(book))

            case _:
                print("Invalid command.")


if __name__ == "__main__": 
    
    print('\t1. Use "add" to add username phone')
    print('\t2. Use "change" to change username phone')
    print('\t3. Use "show_phone" to show username phone')
    print('\t4. Use "all" to see all cantacts')
    print('\t5. Use "close" or "exit" to stop work with bot')
    


    main()