import re


class Email:
    pattern = r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

    def __init__(self, email):
        if re.match(self.pattern, email):
            self.email = email
        else:
            raise ValueError("Incorrect email! Please provide correct email.")