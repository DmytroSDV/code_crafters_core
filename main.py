from AdressBook import *

class Run:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        action = action.strip().lower()
        
        if action == 'add':
            try:
                self.book.add_contacts()
            except ValueError as e:
                print(f"Error: {e}")
                print("Try again")

    def show_help(self):
        commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']   
        print("Available commands:")
        for command in commands:
            print(f"  {command}")

    def run(self):
        print('Hello')
        self.book.read_from_file()
        while True:
            action = input('Enter your command\n').strip().lower()

            if action == 'help':
                self.show_help()
            elif action == 'exit':
                break
            else:
                self.handle(action)

            if action in ['add', 'remove', 'edit']:
                self.book.save_to_file()

if __name__ == "__main__":
    run = Run()
    run.run()


if __name__ == "__main__":
    run = Run()
    run.run()
    