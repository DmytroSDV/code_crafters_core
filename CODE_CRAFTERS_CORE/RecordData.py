from datetime import datetime
import re


class bcolors:
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    ORANGE = "\033[38;5;208m"
    PINK = "\033[95m"    
    R = "\033[0;31;40m"  # Красный на чорном фоне
    G = "\033[0;32;40m"  # Зеленый на черном фоне
    Y = "\033[0;33;40m"  # Желтый на черном фоне
    B = "\033[0;34;40m"  # Синий на черном фоне
    RESET = "\033[0m"  # Удаление цвета


class Email:
    pattern = r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

    def __init__(self, email):
        if re.match(self.pattern, email):
            self.email = email
        else:
            raise ValueError(bcolors.FAIL + "❌ Incorrect email❗ Please provide correct email❗ 😞" + bcolors.RESET)

    def __str__(self):
        return str(self.email)


class Name:
    def __init__(self, name):
        if len(name) >= 2:
            self.name = name
        else:
            raise ValueError(
                bcolors.FAIL + "❌ Name. Name needs to contain not less than 3 symbols❗ 😞" + bcolors.RESET
            )

    def __str__(self):
        return str(self.name)


class Phone:
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError(bcolors.FAIL + "❌ Incorrect phone number format❗ Please provide correct phone number format❗ 😞" + bcolors.RESET)
        else:
            self.value = value

    def is_valid_phone(self, phone):
        return bool(re.findall(r"^\+380[0-9]{9}$|^[0-9]{10}$|^3[0-9]{9}$", phone))

    def __str__(self):
        return str(self.value)


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
                raise ValueError(bcolors.FAIL + "❌ After year YYYY you must enter month (1-12)❗ 😞" + bcolors.RESET)
            self._value = datetime.strptime(val, "%Y-%m-%d").date()
        else:
            raise ValueError(bcolors.FAIL + "❌ Invalid date format❗ Must be YYYY-MM-DD❗ 😞" + bcolors.RESET)

    def __str__(self):
        return str(self.value)
