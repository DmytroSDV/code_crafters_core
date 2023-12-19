from Record import Record
from RecordData import *
from collections import UserList
import pickle
from datetime import datetime,timedelta
from emoji import emojize
from tabulate import tabulate


class bcolors:
    P = "\033[95m"
    G = "\033[92m"
    R = "\033[0;31;40m"  # Красный
    G = "\033[0;32;40m"  # Зеленый
    Y = "\033[0;33;40m"  # Желтый
    B = "\033[0;34;40m"  # Синий
    EN = "\033[0m"


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
            record.birthday = Birthday(birthday)

        contacts = {
            "id": self.id,
            "name": record.name,
            "phone": record.phones,
            "birthday": record.birthday,
            "email": [str(email) for email in record.email],
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
        name = input(emojize("🔍 Введите имя:"))
        found_contacts = []

        for contact in self.data:
            if contact["name"].name.lower() == name.lower():
                found_contacts.append(contact)

        if found_contacts:
            for found_contact in found_contacts:
                print(emojize(f"🎉 Найден контакт с именем '{name}':"))
                print(
                    {
                        emojize("🆔 ID"): found_contact["id"],
                        emojize("👤 Имя"): str(found_contact["name"]),
                        emojize("📞 Телефон") :[
                            str(phone) for phone in found_contact["phone"]
                        ],
                        emojize("🎂 День рождения"): str(found_contact["birthday"]),
                        emojize("📧 Email"): str(found_contact["email"]),
                    }
                )
                print(emojize("✨---------------------------------------✨"))
        else:
            print(emojize(f"😞 Контакт с именем '{name}' не найден."))

    def show_all_contacts(self):
        if not self.data:
            print("Книга контактов пуста.")
            return
        else:
            print("Все контакты в книге:")
            table = []
            for contact in self.data:
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                emails = ", ".join(str(email) for email in contact.get("email", []))
                table.append(
                    [
                        str(contact["id"]),
                        str(contact["name"]),
                        phone_numbers,
                        str(contact.get("birthday", "")),
                        emails,
                    ]
                )
            headers = [
                emojize(":id: ID", language="alias"),
                emojize(":bust_in_silhouette: Имя", language="alias"),
                emojize(":telephone_receiver: Телефон", language="alias"),
                emojize(":birthday_cake: День рождения", language="alias"),
                emojize(":e-mail: Email", language="alias"),
            ]
            print(
                bcolors.G
                + tabulate(table, headers=headers, tablefmt="pretty")
                + bcolors.EN
            )
            print("✨" + "-" * 92 + "✨")

    def remove_phone(self):
        name = input("Please enter name: ")
        for contacts in self.data:
            if str(contacts["name"]) == name:
                phone_to_remove = input("Please enter the phone number to remove: ")
                phone_object_to_remove = None

                for phone_object in contacts["phone"]:
                    if str(phone_object) == phone_to_remove:
                        phone_object_to_remove = phone_object
                        break

                if phone_object_to_remove is not None:
                    contacts["phone"].remove(phone_object_to_remove)
                else:
                    print("Phone number not found.")
            else:
                print("Contact isn't here!")

    def del_contact(self):
        name = input("Please enter name: ")
        for contact in self.data:
            if str(contact["name"]) == name:
                self.data.remove(contact)
            else:
                print("Contact isn't found")

    def add_email(self):
        user_input = input("Please enter name: ")
        for contact in self.data:
            if str(contact["name"]) == user_input:
                email = input("Please enter email: ")
                contact["email"].append(email)
    
    def edit_email(self):
        user_input = input("Please enter name: ")  
        for contact in self.data:
            if str(contact["name"]) == user_input:
                edit_to_email = input("Enter the email to edit📧: ")
                new_email = input("Enter the email📧: ")
                email_object_to_edit = None
                
                for i, email_object in enumerate(contact["email"]):
                    if str(email_object) == edit_to_email:
                        email_object_to_edit = email_object
                        break
                
                if email_object_to_edit is not None:
                    print(f"Old email: {email_object_to_edit}")
                    print(f"Successfully changed to {new_email}")
                                 
                    contact["email"].remove(email_object_to_edit)            
                    contact["email"].append(new_email)
                    
                    print("Email edited successfully✅")
                else:
                    print("Error editing email: email not found❌")
            
    
    def remove_email(self):
        user_input = input("Please enter name: ")
        for contact in self.data:
            if str(contact["name"]) == user_input:
                email_to_remove = input("Please enter the email to remove: ")
                email_object_to_remove = None
                
                for email_object in contact["email"]:
                    if str(email_object) == email_to_remove:
                        email_object_to_remove = email_object
                        break

                if email_object_to_remove is not None:
                    contact["email"].remove(email_object_to_remove)
                else:
                    print("Email not found.")
            else:
                print("Contact isn't here!")
        
    def add_phone(self):
        user_input = input("Please enter name: ")
        for contact in self.data:
            if str(contact["name"]) == user_input:
                phone = input("Please enter phone📞: ")
                contact["phone"].append(phone)
                
    def edit_phone(self):
        user_input = input("Please enter name: ")  
        for contact in self.data:
            if str(contact["name"]) == user_input:
                edit_to_phone_number = input("Enter the phone number to edit📞: ")
                new_phone_number = input("Enter the new phone number📞: ")
                phone_number_object_to_edit = None
                
                for i, phone_number_object in enumerate(contact["phone"]):
                    if str(phone_number_object) == edit_to_phone_number:
                        phone_number_object_to_edit = phone_number_object
                        break
                
                if phone_number_object_to_edit is not None:
                    print(f"Old number: {phone_number_object_to_edit}")
                    print(f"Successfully changed to {new_phone_number}")
                                 
                    contact["phone"].remove(phone_number_object_to_edit)            
                    contact["phone"].append(new_phone_number)
                    
                    print("Phone number edited successfully✅")
                else:
                    print("Error editing phone number: Number not found❌")
            
                    

    def save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"Contacts added to: {file_path}")

    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)

    def edit_birthday(self):  # редагування birthday існуючого контакту
        name = input('Enter name of contact: ')
        for contact in self.data:
            if contact['name'].name == name and contact['birthday']:
                new_birthday = input('Enter new birthday: ')
                contact['birthday'] = Birthday(new_birthday)
                print('Birthday was changed')

    def show_contacts_birthdays(self):
        days = int(input('Enter days: '))
        contacts = []

        for contact in self.data:
            if 'birthday' in contact and contact['birthday']:
                birthday_date = contact['birthday'].value
                record = Record(contact['name'].name, birthday=birthday_date)
                if record.days_to_date(days, birthday_date):
                    contacts.append(contact)

            if contacts:
                for uzer in contacts:
                    print(f'Name: {uzer["name"].name}')
                else:
                    print('there are no birthdays in this number of day')
