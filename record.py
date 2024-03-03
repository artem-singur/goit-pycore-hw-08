import exceptions
import fields

class Record:

    def __init__(self, name):
        self.name = fields.Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_str):

        phone = fields.Phone(phone_str)
        try:
            self.phones.index(phone)
        except:
            self.phones.append(phone)

    def find_phone(self, phone_str):

        phone = fields.Phone(phone_str)
        try:
            return self.phones[self.phones.index(phone)]
        except:
            return None

    def delete_phone(self, phone_str):

        phone = fields.Phone(phone_str)
        try:
            self.phones.pop(self.phones.index(phone))
        except:
            raise exceptions.RecordIsNotExist(f'Phone {phone} is not exist')

    def edit_phone(self, phone_str, new_phone_str):

        phone     = fields.Phone(phone_str)
        new_phone = fields.Phone(new_phone_str)

        try:
            self.phones[self.phones.index(phone)] = new_phone
        except:
            raise exceptions.RecordIsNotExist(f'Phone {phone} is not exist')

    def add_birthday(self, value):
        if self.birthday is None:
            self.birthday = fields.Birthday(value)
        else:
            raise exceptions.BirthdayIsAlreadySet

    def show_birthday(self):
        return 'None' if self.birthday is None else self.birthday.value.strftime("%d.%m.%Y")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
