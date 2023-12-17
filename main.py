from AdressBook import *

class Run:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        action = action.strip().lower()
        
        if action == 'add':
            name = input("Name: ").strip()
            phones = Phone().phone
            birth = Birthday().birthday
            email = Email().value.strip()
            note = input("Note: ").strip()
            record = Record(name, phones, birth, email, status, note)
            return self.book.add_contacts(record)
        
    def show_help(self):
        commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']   
        print("Available commands:")
        for command in commands:
            print(f"  {command}")

    def run(self):
        print('Hello')
        self.book.read_from_file("data.bin")
        while True:
            action = input('Enter your command\n').strip().lower()

            if action == 'help':
                self.show_help()
            elif action == 'exit':
                break
            else:
                self.handle(action)

            if action in ['add', 'remove', 'edit']:
                self.book.save_to_file("auto_save")
                


if __name__ == "__main__":
    run = Run()
    run.run()
    