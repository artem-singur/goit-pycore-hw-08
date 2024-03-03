from record import Record
from input_errors import input_error

def parse_input(user_input):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args

@input_error
def add_contact(args, book):

    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)

    return "Contact added."

@input_error
def change_contact(args, book):

    name, phone = args

    record = book.find(name)
    if record is None:
        return "No such contact exists."
    elif len(record.phones) == 0:
        return "No phone to change."
    else:
        record.edit_phone(record.phones[0].phone, phone)
        return "Contact changed."

@input_error
def get_contact(args, book):

    name = args[0]
    record = book.find(name)
    if record is None:
        return "No such contact exists."
    else:
        return record

@input_error
def all_contacts(book):

    if len(book) > 0:
        book_str = ""
        for name, record in book.data.items():
            book_str = ("" if len(book_str) == 0 else book_str + "\n") + str(record)
        return book_str
    else:
        return "The list of contacts is empty."

@input_error
def add_birthday(args, book):

    name, birthday = args

    record = book.find(name)
    if record is None:
        return "No such contact exists."
    else:
        record.add_birthday(birthday)
        return "Birthday added."

@input_error
def show_birthday(args, book):

    name = args[0]
    record = book.find(name)
    if record is None:
        return "No such contact exists."
    else:
        return "No information yet" if record.birthday.value is None else record.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(book):
    return book.birthdays()
