from CODE_CRAFTERS_CORE.Record import Record
from CODE_CRAFTERS_CORE.RecordData import *
from collections import UserList
from tabulate import tabulate
from emoji import emojize
import pickle


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
                while not flag_name:
                    print(f"{bcolors.ORANGE}📝 Please enter your name that contains more than two characters:✍️  {bcolors.RESET}")
                    name = input(f"{bcolors.BOLD}📝 Please enter your name:✍️  {bcolors.RESET}")

                    record = Record(name)
                    for contact in self.data:
                        if contact["name"].name == name:
                            print(f"{bcolors.WARNING}❌ Contact with this name already exists, try to enter another name!😞 {bcolors.RESET}")
                            print(f"{bcolors.WARNING}📝 Please enter the name again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")
                            if name in ['q', 'back', 'exit', 'quit']:
                                return 
                            break
                    else:
                        flag_name = True

                if not flag_phone:
                    while True:
                        print(f"{bcolors.ORANGE}📞 Exsamples of the input: (+380) or (380) or (10 digits)✅ {bcolors.RESET}")
                        phone = input(f"{bcolors.BOLD}📞 Please enter phone:✍️  {bcolors.RESET}")
                        if phone in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_phone(phone)
                            flag_phone = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {error}{bcolors.RESET}")
                            print(f"{bcolors.WARNING}📞 Please enter the phone number again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                if not flag_birthday:
                    while True:
                        print(f"{bcolors.ORANGE}🎂 Please enter birthday in format (YYYY-MM-DD):✍️  {bcolors.RESET}")
                        birthday = input(f"{bcolors.BOLD}🎂 Please enter birthday:✍️  {bcolors.RESET}")
                        if birthday in ['q', 'back', 'exit', 'quit']:
                            return
                        if birthday:
                            try:
                                record.birthday = Birthday(birthday)
                                flag_birthday = True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}🎂 Please enter the birthday again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️  {bcolors.RESET}")

                if not flag_email:
                    while True:
                        print(f"{bcolors.ORANGE}📧 Please enter email in format (example@example.com):✍️  {bcolors.RESET}")
                        email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                        if email in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            record.add_email(email)
                            flag_email = True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                            print(f"{bcolors.WARNING}📧 Please enter the email again or command ['q', 'back', 'exit', 'quit'] for exit menu:✍️ {bcolors.RESET}")

                contacts = {
                    "id": self.id,
                    "name": record.name,
                    "phone": record.phones,
                    "birthday": record.birthday,
                    "email": [str(email) for email in record.email],
                }
                self.data.append(contacts)
                self.id += 1
                print(f"{bcolors.GREEN}👤 Contact added successfully!✅{bcolors.RESET}")
                break
            except Exception as e:
                attempts += 1
                print(f"{bcolors.FAIL}Error❗ - {bcolors.RESET}{e}")
                print(f"{bcolors.WARNING}🔄 Please enter the information again!🔄 {bcolors.RESET}")


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
        name = input(f"{bcolors.BOLD}🔍 Please enter the name of the contact you want to find:✍️  {bcolors.RESET}")
        matching_contacts = [contact for contact in self.data if contact["name"].name.lower() == name.lower()]

        if not matching_contacts:
            print(f"{bcolors.WARNING}😞 No contacts found with the name 👤 '{name}'{bcolors.RESET}")
            print(emojize(f"{bcolors.WARNING}😞 Contact with name '{name}' does not found❌ {bcolors.RESET}"))
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return

        print(f"{bcolors.GREEN}🔍 Search results for '{name}':🚀  {bcolors.RESET}")
        print(f"{bcolors.GREEN}🎉 Find contact with name🤗  {name}{bcolors.RESET}")
        table = []
        for contact in matching_contacts:
            phone_numbers = ", ".join(str(phone) for phone in contact.get("phone", []))
            emails = ", ".join(str(email) for email in contact.get("email", []))
            table.append([
                str(contact["id"]),
                str(contact["name"]),
                phone_numbers,
                str(contact.get("birthday", "")),
                emails,
            ])

        headers = [
            emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
            emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
            emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
            emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
            emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
        ]

        print(tabulate(table, headers=headers, tablefmt='pretty'))




    def show_all_contacts(self):
        if not self.data:
            print(f"{bcolors.WARNING}📋 Addressbook is empty😞 {bcolors.RESET}")
            print(f"{bcolors.GREEN}🤗 But, you can add a contact if you want ✏️ {bcolors.RESET}")
            return
        else:
            print(f"{bcolors.GREEN}📖 All contacts in book:🚀 {bcolors.RESET}")
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
                emojize(f":id: {bcolors.BLUE}ID{bcolors.RESET}", language="alias"),
                emojize(f":bust_in_silhouette: {bcolors.BLUE}Name{bcolors.RESET}", language="alias"),
                emojize(f":telephone_receiver: {bcolors.BLUE}Phone{bcolors.RESET}", language="alias"),
                emojize(f":birthday_cake: {bcolors.BLUE}Birthday{bcolors.RESET}", language="alias"),
                emojize(f":e-mail: {bcolors.BLUE}Email{bcolors.RESET}", language="alias"),
            ]
            print(tabulate(table, headers=headers, tablefmt='pretty'))
    def remove_phone(self):
        name = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contacts in self.data:
            if str(contacts["name"]) == name:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contacts.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                phone_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the phone number to remove:✍️  {bcolors.RESET}")
                phone_object_to_remove = None

                for phone_object in contacts["phone"]:
                    if str(phone_object) == phone_to_remove:
                        phone_object_to_remove = phone_object
                        break

                if phone_object_to_remove is not None:
                    contacts["phone"].remove(phone_object_to_remove)
                    print(f"{bcolors.GREEN}📞 The phone number '{name}' was successfully deleted!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}📞 Phone number '{phone_to_remove}' not found❌ {bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact '{name}' isn't here!❌ {bcolors.RESET}")

    def del_contact(self):
        name = input(f"{bcolors.BOLD }📝 Please enter name:✍️  {bcolors.RESET}")
        contacts=[]
        for contact in self.data:
            if str(contact["name"]) == name:
                contacts.append(contact)
                self.data.remove(contact)
        if contacts:
            for i in contacts:
                print(f"{bcolors.GREEN}👤 Contact '{i['name'].name}' was deleted!✅{bcolors.RESET}")
        else:
            print(f"{bcolors.FAIL}🔍 Contact '{name}' is not found! 😞{bcolors.RESET}")

    def add_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email = input(f"{bcolors.BOLD}📧 Please enter email:✍️  {bcolors.RESET}")
                contact["email"].append(email)
                print(f"{bcolors.GREEN}📧 Email '{email}' Successfully added!✅{bcolors.RESET}")
                
        if not error_flag:
            print(f"{bcolors.FAIL}👤 Contact isn't here!😞{bcolors.RESET}")
    
    def edit_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                edit_to_email = input(f"{bcolors.BOLD}🔍 Enter the email to edit: {bcolors.RESET}")
                new_email = input(f"{bcolors.BOLD}📧 Enter new email:✍️  {bcolors.RESET}")
                email_object_to_edit = None
                
                for i, email_object in enumerate(contact["email"]):
                    if str(email_object) == edit_to_email:
                        email_object_to_edit = email_object
                        break
                
                if email_object_to_edit is not None:
                    print(f"{bcolors.BOLD}📧 Old email: '{email_object_to_edit}{bcolors.RESET}'")
                    print(f"{bcolors.GREEN}📧 Email successfully changed to '{new_email}'✅{bcolors.RESET}")
                                 
                    contact["email"].remove(email_object_to_edit)            
                    contact["email"].append(new_email)
                    
                    print(f"{bcolors.GREEN}📧 Email edited '{edit_to_email}' successfully!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Error editing email '{edit_to_email}': email not found!❌{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")
            
    
    def remove_email(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                email_list = ", ".join(
                    str(email) for email in contact.get("email", [])
                )
                print(f"{bcolors.WARNING}Select the emails you want to delete{bcolors.RESET}")
                print(f"{bcolors.BLUE}{email_list}{bcolors.WARNING}")
                email_to_remove = input(f"{bcolors.BOLD}🔍 Please enter the email to remove:✍️  {bcolors.RESET}")
                email_object_to_remove = None
                
                for email_object in contact["email"]:
                    if str(email_object) == email_to_remove:
                        email_object_to_remove = email_object
                        break

                if email_object_to_remove is not None:
                    contact["email"].remove(email_object_to_remove)
                    print(f"{bcolors.GREEN}📧 Email '{email_to_remove}' successfully delete!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}❌ Email '{email_to_remove}' not found.😞{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")
        
    def add_phone(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone = input(f"{bcolors.BOLD}🔍 Please enter phone📞: {bcolors.RESET}")
                contact["phone"].append(phone)
                print(f"{bcolors.GREEN}📞 Phone number '{phone}' successfully added!✅{bcolors.RESET}")
        if not error_flag:
            print(f"{bcolors.FAIL}❌ Contact '{user_input}' isn't here!😞{bcolors.RESET}")
                
    def edit_phone(self):
        user_input = input(f"{bcolors.BOLD}🔍 Please enter name:✍️  {bcolors.RESET}")
        error_flag = False 
        for contact in self.data:
            if str(contact["name"]) == user_input:
                error_flag = True
                phone_numbers = ", ".join(
                    str(phone) for phone in contact.get("phone", [])
                )
                print(f"{bcolors.WARNING}Select the phone you want to edit{bcolors.RESET}")
                print(f"{bcolors.BLUE}{phone_numbers}{bcolors.WARNING}")
                edit_to_phone_number = input(f"{bcolors.BOLD}📞 Enter the phone number to edit:✍️  {bcolors.RESET}")
                new_phone_number = input(f"{bcolors.BOLD}📞 Enter the new phone number:✍️  {bcolors.RESET}")
                phone_number_object_to_edit = None
                
                for i, phone_number_object in enumerate(contact["phone"]):
                    if str(phone_number_object) == edit_to_phone_number:
                        phone_number_object_to_edit = phone_number_object
                        break
                
                if phone_number_object_to_edit is not None:
                    print(f"{bcolors.WARNING}📞 Old phone number: '{phone_number_object_to_edit}'{bcolors.RESET}")
                    print(f"{bcolors.GREEN}📞 Successfully changed to '{new_phone_number}'✅{bcolors.RESET}")                                 
                    contact["phone"].remove(phone_number_object_to_edit)            
                    contact["phone"].append(new_phone_number)
                    print(f"{bcolors.GREEN}📞 Phone number '{new_phone_number}' edited successfully!✅{bcolors.RESET}")
                else:
                    print(f"{bcolors.FAIL}📞 Error editing phone number '{new_phone_number}': Phone Number not found❌{bcolors.RESET}")
                    
        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{user_input}'!{bcolors.RESET}")
                                  
    def save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}💾 Contacts added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")

    def read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading contacts from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            return pickle.load(file)

    def edit_birthday(self):  # редагування birthday існуючого контакту
        name = input(f'{bcolors.BOLD}🔍 Enter name of contact:✍️  {bcolors.RESET}')
        error_flag = False
        for contact in self.data:
            if contact['name'].name == name and contact['birthday']:
                new_birthday = input('Enter new birthday: ')
                try:
                    contact['birthday'] = Birthday(new_birthday)
                    print(f'{bcolors.GREEN}🎂 Birthday "{new_birthday}" was changed!✅{bcolors.RESET}')
                except ValueError as ex:
                    print(ex)
                error_flag = True
                
        if not error_flag:
            print(f"{bcolors.FAIL}❌ There are no contacts with such name '{name}'!{bcolors.RESET}")
        
    def show_contacts_birthdays(self):
        while 1:
            try:
                days = int(input(f"{bcolors.BOLD}🤗 Enter days:✍️  {bcolors.RESET}"))
                break
            except Exception as e:
                print(f"{bcolors.WARNING}Enter the number of days by number and not string!{bcolors.RESET}")
                continue
            
        contacts = []

        for contact in self.data:
            if 'birthday' in contact and contact['birthday']:
                birthday_date = contact['birthday'].value
                record = Record(contact['name'].name, birthday=birthday_date)
                if record.days_to_date(days, birthday_date):
                    contacts.append(contact)

        if contacts:
            for uzer in contacts:
                print(f'{bcolors.GREEN}Name: {uzer["name"].name}, Birthday:🎂  {uzer["birthday"].value}{bcolors.RESET}')
        else:
            print(f'{bcolors.WARNING}🎂 There are no birthdays in this number of day!{bcolors.RESET}')
                
