from collections import UserDict
from datetime import datetime, timedelta
import exceptions

class AddressBook(UserDict):
    
    def add_record(self, record):

        if self.data.get(record.name.name) is None:
            self.data[record.name.name] = record
        else:
            raise exceptions.RecordIsAlreadyExist

    def find(self, name):

        record = self.data.get(name)
        if record is None:
            raise exceptions.RecordIsNotExist
        else:
            return record

    def delete(self, name):

        record = self.data.get(name)
        if record is None:
            raise exceptions.RecordIsNotExist
        else:
            self.data.pop(name)

    def birthdays(self):

        today = datetime.today().date()
        first_day = today + timedelta(days = 1)
        last_day  = today + timedelta(days = 7)
        upcoming_birthdays_list = []
        # upcoming_birthdays = ""

        for name, record in self.data.items():
            if record.birthday is None:
                continue
            else:
                birthday = record.birthday.value.date()
                birthday_this_year = datetime(year = first_day.year, month = birthday.month, day = birthday.day).date()

                if birthday_this_year < first_day:
                    birthday_this_year = datetime(year = last_day.year, month = birthday.month, day = birthday.day).date()

                birthday_weekday = birthday_this_year.weekday()

                if (birthday_weekday == 5) or (birthday_weekday == 6):
                    birthday_this_year = birthday_this_year + timedelta(days = (7 - birthday_weekday))

                if first_day <= birthday_this_year <= last_day:
                    upcoming_birthdays_list.append(birthday_this_year.strftime("%d.%m.%Y") + "  " + str(record))
                    # upcoming_birthdays = ("" if len(upcoming_birthdays) == 0 else upcoming_birthdays + "\n") + birthday_this_year.strftime("%d.%m.%Y") + "  " + str(record)

        if len(upcoming_birthdays_list) == 0:
            raise exceptions.NoSuitableDates
        else:
            return "\n".join(upcoming_birthdays_list)
