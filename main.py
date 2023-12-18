from AddressBook import *
from pathlib import Path
from FileSorting import executing_command


def available_commands():
    command_list = [
        "contact-add",
        "contact-find",
        "contact-show-all",
        "contact-phone-add",
        "contact-email-add",
        "contact-edit-phone",
        "contact-edit-email",
        "contact-edit-birthday",
        "contact-remove",
        "display-birthdays",
        "note-add",
        "note-find",
        "note-show-all",
        "note-edit",
        "note-remove",
        "tag-add",
        "tag-find-sort",
        "file-sort",
        "file-extension-add",
        "file-extension-remove",
        "quit",
        "exit",
        "q",
    ]
    command_explain = [
        "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів",
        "здійснює пошук контакту серед контактів книги",
        "показує всі існуючі контакти в книзі контактів",
        "додати іще 1-ин phone до існуючого контакту",
        "додати іще 1-ин email до існуючого контакту",
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


def main():
    while 1:
        from_user = input(
            "To see available list of commands enter 'cli'.\nCommand prompt: "
        )

        match from_user.lower():
            case "cli":
                print(available_commands())

            case "contact-add":
                # 'зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів'
                pass

            case "contact-find":
                # 'здійснює пошук контакту серед контактів книги'
                pass

            case "contact-show-all":
                # "показує всі існуючі контакти в книзі контактів"
                pass
            case "contact-phone-add":
                # "додати іще 1-ин phone до існуючого контакту"
                pass

            case "contact-email-add":
                # "додати іще 1-ин email до існуючого контакту"
                pass

            case "contact-edit-phone":
                # "редагування phone існуючого контакту"
                pass

            case "contact-edit-email":
                # 'редагування email існуючого контакту'
                pass

            case "contact-edit-birthday":
                # 'редагування birthday існуючого контакту'
                pass

            case "contact-edit-birthday":
                # 'редагування birthday існуючого контакту'
                pass

            case "contact-edit-birthday":
                # 'редагування birthday існуючого контакту'
                pass

            case "contact-remove":
                # 'видалення існуючого контакту'
                pass

            case "display-birthdays":
                # "виводить список контактів, у яких день народження через задану кількість днів від поточної дати"
                pass

            case "note-add":
                # "зберігає нотатку за іменем автора"
                pass

            case "note-find":
                # "здійснює пошук нотатки серед існуючих нотатків"
                pass

            case "note-show-all":
                # "показує всі існуючі нотатки",
                pass

            case "note-edit":
                # "редагування існуючої нотатки"
                pass

            case "note-remove":
                #  "видалення існуючої нотатки"
                pass

            case "tag-add":
                #  "додавання тегів до існуючої нотатки"
                pass

            case "tag-find-sort":
                #  "пошук та сортування нотаток за тегами"
                pass

            case "file-sort":
                #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                executing_command(from_user.lower())

            case "file-extension-add":
                #  "додавання додатково розширення для сортування"
                executing_command(from_user.lower())

            case "file-extension-remove":
                #  "видалення розширення із списку для сортування"
                executing_command(from_user.lower())

            case "quit" | "exit" | "q":
                print("Good bye!\n")
                # сюди так само можна передавати файл і видалити іnput з save_to_file
                serialization = AddressBook()
                serialization.save_to_file(file_name, book)
                break

            case _:
                print(
                    f"Such command '{from_user}' does not exist! TO saw available commands please type 'cli'."
                )


if __name__ == "__main__":
    file_name = "database.json"
    file_database = Path(file_name)

    if file_database.exists() and file_database.is_file():
        with open(file_database, "r") as fh:
            check_content = fh.read()

        if not check_content:
            book = AddressBook()
        else:
            desirialization = AddressBook()
            book = desirialization.read_from_file(file_name)
    else:
        with open(file_database, "w") as fh:
            pass
        book = AddressBook()

    main()
