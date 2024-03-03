
class FieldIsEmpty(Exception):

    def __init__(self, message = 'Field is empty') -> None:
        self.message = message
        super().__init__(self.message)

class PhoneError(Exception):

    def __init__(self, message = 'Phone error') -> None:
        self.message = message
        super().__init__(self.message)

class BirthdayIsAlreadySet(Exception):

    def __init__(self, message = 'Birthday is already set') -> None:
        self.message = message
        super().__init__(self.message)

class RecordIsAlreadyExist(Exception):

    def __init__(self, message = 'Record is already exist') -> None:
        self.message = message
        super().__init__(self.message)

class RecordIsNotExist(Exception):

    def __init__(self, message = 'Record is not exist') -> None:
        self.message = message
        super().__init__(self.message)

class InvalidDateFormat(Exception):

    def __init__(self, message = 'Invalid date format. Use DD.MM.YYYY') -> None:
        self.message = message
        super().__init__(self.message)

class NoSuitableDates(Exception):

    def __init__(self, message = 'There are no suitable dates') -> None:
        self.message = message
        super().__init__(self.message)
