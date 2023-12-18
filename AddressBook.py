from Record import Record
from RecordData import *
from collections import UserList
import pickle
from datetime import datetime
import emoji


class AddressBook(UserList):
    def __init__(self):
        super().__init__()
        self.id = 1

    def add_contacts(self):
        name = input("Please enter name: ")
        phone = input("Please enter phone: ")
        record = Record(name)
        record.add_phone(phone)
        birthday = input("Please enter birthday: ")
        email = input("Please enter email: ")
        record.add_email(email)

        if birthday:
            # year, month, day = map(int, birthday.split())
            record.birthday = Birthday(birthday)
        if email:
            record.email = Email(email)


        contacts = {
            "id": self.id,
            "name": record.name,
            "phone": record.phones,
            "birthday": record.birthday,
            "email": record.email,
            "note": record.note,
        }
        self.data.append(contacts)
        self.id += 1
        print("add contact")

    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(contact)
        print(result)

    def search_contact(self):
        name = input(emoji.emojize('🔍 Введите имя: '))
        found_contacts = []

        for contact in self.data:
            if contact['name'].name.lower() == name.lower():
                found_contacts.append(contact)

        if found_contacts:
            for found_contact in found_contacts:
                print(emoji.emojize(f"🎉 Найден контакт с именем '{name}':"))
                print({
                    emoji.emojize('🆔 ID:'): found_contact['id'],
                    emoji.emojize('👤 Имя:'): str(found_contact['name']),
                    emoji.emojize('📞 Телефон:'): [str(phone) for phone in found_contact['phone']],
                    emoji.emojize('🎂 День рождения:'): str(found_contact['birthday']),
                    emoji.emojize('📧 Email:'): str(found_contact['email']),
                    emoji.emojize('📝 Примечание:'): str(found_contact['note'])
                })
                print(emoji.emojize("✨---------------------------------------✨"))
        else:
            print(emoji.emojize(f"😞 Контакт с именем '{name}' не найден."))
            
    def show_all_contacts(self):
        if not self.data:
            print("Книга контактов пуста.")
            return
        else:
            print("Все контакты в книге:")
            for contact in self.data:
                print("ID:", contact['id'])
                print("Имя:", contact['name'])
                if 'phone' in contact and isinstance(contact['phone'], list):
                    phone_numbers = [str(phone) for phone in contact['phone']]
                print("Телефон:", ', '.join(phone_numbers))
                print("День рождения:", contact['birthday'])
                print("Email:", contact['email'])
                print("Примечание:", contact['note'] if contact['note'] else "Отсутствует")
                print("✨---------------------------------------✨")
    
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
            if str(contact["name"]) == name:
                self.data.remove(contact)
            else:
                print("Contact isn't found")


    def save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"Contacts added to: {file_path}")


    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)
