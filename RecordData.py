class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    def is_valid_phone(self, phone):
    
        return bool(re.match(r'^[\d-]+$', phone))
