from CODE_CRAFTERS_CORE.Record import Record
from CODE_CRAFTERS_CORE.RecordData import *
from collections import UserList
import pickle
from datetime import datetime,timedelta
from emoji import emojize
from tabulate import tabulate


class AddressBook(UserList):
    def __init__(self):
        super().__init__()
        self.id = 1

    def add_contacts(self):
        attempts = 0
        flag_name = False
        flag_phone = False
        flag_birthday = False
        flag_email = False

        while attempts < 3:
            try:
                if not flag_name:
                    name = input("Please enter name: ")
                    record = Record(name)
                    flag_name = True

                if not flag_phone:
                    while True:
                        print('Exsamples of the input: (+380) or (380) or (10 digits) ')
                        phone = input("Please enter phone: ")
                        if phone=='q':
                            return
                        try:
                            record.add_phone(phone)
                            flag_phone = True
                            break
                        except ValueError as error:
                            print(f"Error: {error}")
                            print("Please enter the phone number again or command 'q' for exit ")

                if not flag_birthday:
                    while True:
                        birthday = input("Please enter birthday with the help of YYYY-MM-DD: ")
                        if birthday=='q':
                            return
                        if birthday:
                            try:
                                record.birthday = Birthday(birthday)
                                flag_birthday = True
                                break
                            except ValueError as error:
                                print(f"Error: {error}")
                                print("Please enter the birthday again or command 'q' for exit ")

                if not flag_email:
                    while True:
                        email = input("Please enter email : ")
                        if email=='q':
                            return
                        try:
                            record.add_email(email)
                            flag_email = True
                            break
                        except ValueError as error:
                            print(f"Error: {error}")
                            print("Please enter the email again or command 'q' for exit ")

                contacts = {
                    "id": self.id,
                    "name": record.name,
                    "phone": record.phones,
                    "birthday": record.birthday,
                    "email": [str(email) for email in record.email],
                }
                self.data.append(contacts)
                self.id += 1
                print("Contact added successfully!✅")
                break
            except Exception as e:
                attempts += 1
                print(f"Error: {e}")
                print("Please enter the information again.")


                flag_name = False
                flag_phone = False
                flag_birthday = False
                flag_email = False
    def birthdays(self, days):
        result = []
        for contact in self.data:
            compare = contact.days_to_birthday()
            if str(compare) == days:
                result.append(contact)
        print(result)

    def search_contact(self):
        name = input(emojize("🔍 Enter your name:"))
        found_contacts = []

        for contact in self.data:
            if contact["name"].name.lower() == name.lower():
                found_contacts.append(contact)

        if found_contacts:
            for found_contact in found_contacts:
                print(emojize(f"🎉 Find contact with name '{name}':"))
                print(
                    {
                        emojize("🆔 ID"): found_contact["id"],
                        emojize("👤 Name"): str(found_contact["name"]),
                        emojize("📞 Phone") :[
                            str(phone) for phone in found_contact["phone"]
                        ],
                        emojize("🎂 Birthday"): str(found_contact["birthday"]),
                        emojize("📧 Email"): str(found_contact["email"]),
                    }
                )
                print(emojize("✨---------------------------------------✨"))
        else:
            print(emojize(f"😞 Contact with name '{name}' does not found."))

    def show_all_contacts(self):
        if not self.data:
            print("Addressbook is empty")
            return
        else:
            print("All contacts in book:")
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
                emojize(f":id:{bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
                emojize(":bust_in_silhouette: Name", language="alias"),
                emojize(":telephone_receiver: Phone", language="alias"),
                emojize(":birthday_cake: Birthday", language="alias"),
                emojize(":e-mail: Email", language="alias"),
            ]
            print(tabulate(table, headers=headers,tablefmt='pretty'))
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
        contacts=[]
        for contact in self.data:
            if str(contact["name"]) == name:
                contacts.append(contact)
                self.data.remove(contact)
        if contacts:
            for i in contacts:
                print(f"contact {i['name'].name} was deleted")
        else:
            print('Contact is not found')

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
            print(f"{bcolors.GREEN}💾 Contacts added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")

    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading contacts from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
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
                    print(f'Name: {uzer["name"].name}, Birthday: {uzer["birthday"].value}')
            if not contact:
                print('there are no birthdays in this number of day')
