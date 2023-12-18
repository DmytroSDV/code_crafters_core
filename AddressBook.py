from Record import Record
from RecordData import *
from collections import UserList
import pickle
from datetime import datetime


class AddressBook(UserList):
    id = 1

    def add_contacts(self):
        name = input("Please enter name: ")
        phone = input("Please enter phone: ")
        record = Record(name)
        record.add_phone(phone)
        birthday = input("Please enter birthday: ")
        email = input("Please enter email: ")
        record.add_email(email)
        # note=input('Please enter note: ')
        # record.add_note(note)
        if birthday:
            # year, month, day = map(int, birthday.split())
            record.birthday = Birthday(birthday)
        if email:
            record.email = Email(email)
        # if note:
        # record.note=Note(note)

        contacts = {
            "id": self.id,
            "name": record.name,
            "phone": record.phones,
            "birthday": record.birthday,
            "email": record.email,
            "note": record.note,
        }
        self.data.append(contacts)
        AddressBook.id += 1
        print("add contact")

    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(contact)
        print(result)

    def seach_contact(self):
        name = input("Please enter name: ")
        for contact in self.data:
            if contact["name"].name == name:
                print(contact)

    def __str__(self):
        result = ""
        for account in self.data:
            phone = ""
            birthday = ""
            email = ""

            if "phone" in account and account["phone"]:
                for i in account["phone"]:
                    phone += str(i.value) + " "

            if "birthday" in account and account["birthday"]:
                birthdaycontact = account["birthday"].value
                birthday = str(birthdaycontact)

            if "email" in account and account["email"]:
                email = account["email"]

            result += f"Contact: \n name: {account['name'].name} \n phone: {phone} \n birthday: {birthday} \n email: {email.email}\n"

        return result

    def remove_phone(self):
        name = input()
        for contacts in self.data:
            if contacts["name"] == name:
                phone = input("Please enter new phone")
                contacts["phone"].remove(phone)
            else:
                print("Contact isn't here!")

    def del_contact(self):
        name = input("Please enter name: ")
        for contact in self.data:
            if contact["name"] == name:
                self.data.remove(contact)
            else:
                print("Contact isn't found")


def save_to_file(self, file_path: str, data):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)
        print(f"Контакты записаны в файл: {file_path}")


def read_from_file(self, file_path: str):
    with open(file_path, "rb") as file:
        return pickle.load(file)
