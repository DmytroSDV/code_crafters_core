from RecordData import *
from datetime import datetime



class Record:
    def __init__(self, name: str, phone=None, birthday = None, email = None, note = None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
        self.email = []
        self.note = Note(note)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_email(self, email):
        self.email.append(Email(email))

    def remove_email(self, email):
        self.email = [p for p in self.email if p.value != email]

    def edit_email(self, old_email, new_email):
        for p in self.email:
            if p.value == old_email:
                p.value = new_email

    def find_email(self, email):
        for p in self.email:
            if p.value == email:
                return p
        return None

    def add_email(self, email):
        self.email.append(Email(email))

    def add_note(self, note):
        self.note.append(Note(note))

    def days_to_birthday(self):
        try:
            current_date = datetime.now().date()
            record_nearest_birthday = self.birthday.value.replace(
                year=current_date.year
            )
            if record_nearest_birthday < current_date:
                record_nearest_birthday = self.birthday.value.replace(
                    year=current_date.year + 1
                )
                days_until_birthday = (record_nearest_birthday - current_date).days
                # print(f"Record: {self.name.value}, Nearest Birthday: {record_nearest_birthday}, Days until Birthday: {days_until_birthday}")
            return days_until_birthday

        except AttributeError:
            print(f"Contact name do not have birthday record")
