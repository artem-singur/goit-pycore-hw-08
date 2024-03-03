import input_processing
import data_processing

def main():

    book = data_processing.load_data()

    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        command, *args = input_processing.parse_input(user_input)

        if command in ["close", "exit"]:

            data_processing.save_data(book)
            print("Good bye!")
            break

        elif command == "hello":

            print("How can I help you?")

        elif command == "add":

            print(input_processing.add_contact(args, book))

        elif command == "change":

            print(input_processing.change_contact(args, book))

        elif command == "phone":

            print(input_processing.get_contact(args, book))

        elif command == "all":

            print(input_processing.all_contacts(book))

        elif command == "add-birthday":

            print(input_processing.add_birthday(args, book))

        elif command == "show-birthday":

            print(input_processing.show_birthday(args, book))

        elif command == "birthdays":

            print(input_processing.birthdays(book))

        else:

            print("Invalid command.")

if __name__ == "__main__":

    main()
