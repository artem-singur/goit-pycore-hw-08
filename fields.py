from datetime import datetime
import exceptions

class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):

    def __init__(self, value):
        name = str(value).strip()
        if len(name) > 0:
            self.name = name
            super().__init__(self.name)
        else:
            raise exceptions.FieldIsEmpty('Name is empty')

    def get_name(self):
        return self.name

class Phone(Field):

    def __init__(self, value):
        phone = str(value).strip()
        if len(phone) == 10:
            self.phone = phone
            super().__init__(self.phone)
        else:
            raise exceptions.PhoneError('Phone number must contain ten digits')

    def __eq__(self, __value: object) -> bool:
        return self.phone == __value.phone

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise exceptions.InvalidDateFormat
