import exceptions

def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact exists."
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "Enter the argument for the command."
        except exceptions.FieldIsEmpty as e:
            return e.message
        except exceptions.PhoneError as e:
            return e.message
        except exceptions.BirthdayIsAlreadySet as e:
            return e.message
        except exceptions.RecordIsAlreadyExist as e:
            return e.message
        except exceptions.RecordIsNotExist as e:
            return e.message
        except exceptions.InvalidDateFormat as e:
            return e.message
        except exceptions.NoSuitableDates as e:
            return e.message

    return inner
