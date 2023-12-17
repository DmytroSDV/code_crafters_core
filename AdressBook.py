from Record import Record
from collections import UserList


class AddressBook(UserList):

    def __init__(self,addressbook):
        self.addressbook=addressbook
        self.id=1

    def add_contacts(self):
        name=input('Please enter name: ')
        phone=input('Please enter phone: ')
        record=Record(name)
        record.add(phone)
        birthday=input('Please enter birthday: ')
        email=input('Please enter email: ')
        record.add_mail(email)
        note=input('Please enter note: ')
        record.add_note(note)
        if birthday:
            year, month, day = map(int, birthday.split())
            record.birthday = Birthday(year, month, day)

        contacts={'id':self.id,'name': record.name,'phone':record.phones, 'birthday': record.birthday,'email': record.email,'note': record.note }
        self.data.append(contacts)



















