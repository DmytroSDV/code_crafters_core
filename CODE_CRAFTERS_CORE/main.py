from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from CODE_CRAFTERS_CORE.FileSorting import executing_command
from CODE_CRAFTERS_CORE.RecordData import bcolors
from pathlib import Path
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.application.current import get_app
import random
import threading
from prompt_toolkit.styles import Style


COLOR_COMMAND_GREEN = 'bg:#ansigreen #ffffff'
STYLE = Style.from_dict({"prompt": COLOR_COMMAND_GREEN})

    
HI_COMMANDS = [
    "🎩✨Abracadabra! Enter the magic team:",
    "Let me know what you want to do: ",
    "Waiting for your team to start work: ",
    "Welcome to the amazing world of opportunities! Waiting for your team to start.",
    "Welcome to the world of opportunities! Waiting for your magic team.",
]


COMMAND_EXPLAIN = WordCompleter(
    [
        "cli",
        "contact-add",
        "contact-find",
        "contact-show-all",
        "contact-phone-add",
        "contact-phone-remove",
        "contact-email-add",
        "contact-email-remove",
        "contact-phone-edit",
        "contact-email-edit",
        "contact-birthday-edit",
        "contact-remove",
        "display-birthdays",
        "note-add",
        "note-find",
        "note-show-all",
        "note-edit",
        "note-remove",
        "tag-add",
        "tag-edit",
        "tag-remove",
        "tag-find-sort",
        "file-sort",
        "file-extension-add",
        "file-extension-remove",
        "quit",
        "exit",
        "q",
    ]
)


def pre_run():
    app = get_app()
    b = app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)


def available_commands():
    command_list = [
        "cli",
        "contact-add",
        "contact-find",
        "contact-show-all",
        "contact-phone-add",
        "contact-phone-remove",
        "contact-email-add",
        "contact-email-remove",
        "contact-phone-edit",
        "contact-email-edit",
        "contact-birthday-edit",
        "contact-remove",
        "display-birthdays",
        "note-add",
        "note-find",
        "note-show-all",
        "note-edit",
        "note-remove",
        "tag-add",
        "tag-edit",
        "tag-remove",
        "tag-find-sort",
        "file-sort",
        "file-extension-add",
        "file-extension-remove",
        "quit",
        "exit",
        "q",
    ]

    command_explain = [
        "виводить список всіх доступних команд",
        "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів",
        "здійснює пошук контакту серед контактів книги",
        "показує всі існуючі контакти в книзі контактів",
        "додати іще 1-ин phone до існуючого контакту",
        "видалення існуючого phone",
        "додати іще 1-ин email до існуючого контакту",
        "видалення існуючого email",
        "редагування phone існуючого контакту",
        "редагування email існуючого контакту",
        "редагування birthday існуючого контакту",
        "видалення існуючого контакту",
        "виводить список контактів, у яких день народження через задану кількість днів від поточної дати",
        "зберігає нотатку за іменем автора",
        "здійснює пошук нотатки серед існуючих нотатків",
        "показує всі існуючі нотатки",
        "редагування існуючої нотатки",
        "видалення існуючої нотатки",
        "додавання тегів до існуючої нотатки",
        "редагування тегів існуючої нотатки",
        "видалення тегів з існуючої нотатки",
        "пошук та сортування нотаток за тегами",
        "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.).",
        "додавання додатково розширення для сортування",
        "видалення розширення із списку для сортування",
        "вихід з програми",
        "вихід з програми",
        "вихід з програми",
    ]

    return "".join(
        "|{:<10} - {:<20}|\n".format(command_list[item], command_explain[item])
        for item in range(len(command_list))
    )


def get_input():
    from_user = prompt(
        random.choice(HI_COMMANDS),
        completer=COMMAND_EXPLAIN,
        pre_run=pre_run,
        style=STYLE,
    )
    return from_user


def wait_for_input(timeout=60):
    result = None
    event = threading.Event()

    def input_thread():
        nonlocal result
        result = get_input()
        event.set()

    thread = threading.Thread(target=input_thread, daemon=True)
    thread.start()

    # Создаем таймер для обновления времени
    timer = threading.Timer(timeout, event.set)
    timer.start()

    # Ждем ввода или завершения таймера
    thread.join(timeout=timeout)

    # Отменяем таймер, если пользователь ввел команду
    timer.cancel()

    if thread.is_alive():
        print("\n⏰ You are here, I'm waiting for your command")

    return result


def main():
    file_name = "database.bin"
    note_name = "notebase.bin"
    file_database = Path(file_name)
    note_database = Path(note_name)

    # Deserialization adddressbook
    if file_database.exists() and file_database.is_file():
        with open(file_database, "rb") as fh:
            check_content = fh.read()

        if not check_content:
            book = AddressBook()
        else:
            deserialization = AddressBook()
            book = deserialization.read_from_file(file_name)
    else:
        with open(file_database, "wb") as fh:
            pass
        book = AddressBook()

    # Deserialization notebook
    if note_database.exists() and note_database.is_file():
        with open(note_database, "rb") as fh:
            check_content = fh.read()
        if not check_content:
            note = NoteBook()
        else:
            deserialization = NoteBook()
            note = deserialization.note_read_from_file(note_name)
    else:
        with open(note_database, "wb") as fh:
            pass
        note = NoteBook()


    print("Hello! My name is Bot Jul. How can I help you today?")

    try:
        while 1:
            user_input = wait_for_input()

            match user_input:
                case "cli":
                    print(available_commands())

                case "contact-add":
                    # 'зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів'
                    book.add_contacts()

                case "contact-find":
                    # 'здійснює пошук контакту серед контактів книги'
                    book.search_contact()

                case "contact-show-all":
                    # "показує всі існуючі контакти в книзі контактів"
                    book.show_all_contacts()

                case "contact-phone-add":
                    # "додати іще 1-ин phone до існуючого контакту"
                    book.add_phone()

                case "contact-phone-remove":
                    # "видалення існуючого phone",
                    book.remove_phone()

                case "contact-email-add":
                    # "додати іще 1-ин email до існуючого контакту"
                    book.add_email()

                case "contact-email-remove":
                    # "видалення існуючого email",
                    book.remove_email()

                case "contact-phone-edit":
                    # "редагування phone існуючого контакту"
                    book.edit_phone()

                case "contact-email-edit":
                    # 'редагування email існуючого контакту'
                    book.edit_email()

                case "contact-birthday-edit":
                    # 'редагування birthday існуючого контакту'
                    book.edit_birthday()

                case "contact-remove":
                    # "видалення існуючого контакту"
                    book.del_contact()

                case "display-birthdays":
                    # "виводить список контактів, у яких день народження через задану кількість днів від поточної дати"
                    book.show_contacts_birthdays()

                case "note-add":
                    # "зберігає нотатку за іменем автора",
                    note.add_new_note()

                case "note-find":
                    # "здійснює пошук нотатки серед існуючих нотатків"
                    note.find_author()

                case "note-show-all":
                    # "показує всі існуючі нотатки"
                    note.note_show_all()

                case "note-edit":
                    # "редагування існуючої нотатки"
                    note.note_edit()

                case "note-remove":
                    # "видалення існуючої нотатки"
                    note.note_remove()

                case "tag-add":
                    #  "додавання тегів до існуючої нотатки"
                    note.tag_add()

                case "tag-edit":
                    #  "редагування тегів існуючої нотатки"
                    note.tag_edit()

                case "tag-remove":
                    #  "видалення тегів з існуючої нотатки"
                    note.tag_remove()

                case "tag-find-sort":
                    #  "пошук та сортування нотаток за тегами"
                    note.tag_find_and_sort()

                case "file-sort":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())

                case "file-extension-add":
                    #  "додавання додатково розширення для сортування"
                    executing_command(user_input.lower())

                case "file-extension-remove":
                    #  "видалення розширення із списку для сортування"
                    executing_command(user_input.lower())

                case "quit" | "exit" | "q":
                    print("Good bye!\n")

                    serialization = AddressBook()
                    serialization.save_to_file(file_name, book)
                    note_serialization = NoteBook()
                    note_serialization.note_save_to_file(note_name, note)
                    break

                case _:
                  error_messages = [
                    "Oh! You seem to have introduced the wrong team. Please try again!",
                    "Oops! This is not like the right team. Let's try again",
                    "Error: The team is not recognized. Try again.",
                    "😮 Hmm, I don't understand this team. Let's try something else."
                  ]
                  print(random.choice(error_messages))

                
    except Exception as ex:
        print("Unnexpected error!\n")

        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)
    
    except KeyboardInterrupt:
        print("KeyBoard interrupt error, EXITING!\n")

        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)




if __name__ == "__main__":
    main()
