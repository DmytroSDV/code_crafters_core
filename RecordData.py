import re

class Email:
    pattern = r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

    def __init__(self, email):
        if re.match(self.pattern, email):
            self.email = email
        else:
            raise ValueError("Incorrect email! Please provide correct email.")

class Name:

    def __init__(self,name):
        self.set_name(name)

    def get_name(self):
        return self.name

    def set_name(self,name):
        if self.valid_name(name):
            self.name=name
        else:
            raise ValueError('Wrong Name. Name needs to contain not less than 3 symbols')

    def valid_name(self,name):
        if len(name)>=3 and name.isalpha():
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

