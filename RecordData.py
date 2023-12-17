
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

