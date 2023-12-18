import re
from datetime import datetime


class Email:
    pattern = r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

    def __init__(self, email):
        if re.match(self.pattern, email):
            self.email = email
        else:
            raise ValueError("Incorrect email! Please provide correct email.")


class Name:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.name

    def set_name(self, name):
        if self.valid_name(name):
            self.name = name
        else:
            raise ValueError(
                "Wrong Name. Name needs to contain not less than 3 symbols"
            )

    def valid_name(self, name):
        if len(name) >= 3 and name.isalpha():
            return True
        return False


class Phone:
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        else:
            self.value = value

    def is_valid_phone(self, phone):
        return bool(re.findall(r"^\+380[0-9]{9}$|^[0-9]{10}$|^3[0-9]{9}$", phone))


class Birthday:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        date_pattern = r"\d{4}-\d{2}-\d{2}"
        if re.match(date_pattern, val):
            date_split = val.split("-")
            if int(date_split[1]) > 12:
                raise ValueError("After year YYYY you must enter month (1-12)!")
            self._value = datetime.strptime(val, "%Y-%m-%d").date()
        else:
            raise ValueError("Invalid date format! Must be YYYY-MM-DD!")

class Note:
    def __init__(self, title):
        self.title = title
        self.content = ""
        self.tags = []

    def add_tag(self, value):
        result = map(lambda t: t.value, self.tags)
        if not value in result:
            self.tags.append(value)

    def add_content(self, value):
        self.content = value

