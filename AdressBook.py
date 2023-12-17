from collections import UserList

class AddressBook(UserList):
    
    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(key)
        print(result)
