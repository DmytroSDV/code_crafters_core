from Record import Record
from RecordData import *
from collections import UserList
import pickle


class AddressBook(UserList):
    id=1



    def add_contacts(self):
        name=input('Please enter name: ')
        phone=input('Please enter phone: ')
        record=Record(name,phone)
        record.add_phone(phone)
        birthday=input('Please enter birthday: ')
        email=input('Please enter email: ')
        record.add_email(email)
        note=input('Please enter note: ')
        record.add_note(note)
        if birthday:
            year, month, day = map(int, birthday.split())
            record.birthday = Birthday(year, month, day)
        if email:
            record.email=Email(email)
        if note:
            record.note=Note(note)

        contacts={'id':self.id,'name': record.name,'phone':record.phones, 'birthday': record.birthday,'email': record.email,'note': record.note }
        self.data.append(contacts)
        AddressBook.id+=1
        
    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(contact)
        print(result)

    def seach_contact(self):
        name=input('Please enter name: ')
        for contact in self.data:
            if contact['name']==name:
                print(contact)

    def display_all_contacts(self):
        for contact in self.data:
            print(contact['name'])


    def remove_phone(self):
        name=input()
        for contacts in self.data:
            if contacts['name']==name:
                phone=input('Please enter new phone')
                contacts['phone'].remove(phone)
            else:
                print("Contact isn't here!")


    def del_contact(self):
        name=input('Please enter name: ')
        for contact in self.data:
            if contact['name']==name:
                self.data.remove(contact)
            else:
                print("Contact isn't found")


    def save_to_file(self):
        file_name=input()
        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)
            print(f'Контакты записаны в файл: {file_name}')


    def read_from_file(self):
        file_name = input('Введите имя файла: ')
        with open(file_name, "rb") as file:
            self.data = pickle.load(file)
        for contact in self.data:
            print(contact)



















