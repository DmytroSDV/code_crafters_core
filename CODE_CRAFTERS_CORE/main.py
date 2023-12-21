from CODE_CRAFTERS_CORE.AvadaKedavra import shutdown_with_countdown
from CODE_CRAFTERS_CORE.FileSorting import executing_command
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from CODE_CRAFTERS_CORE.RecordData import bcolors
from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
from pathlib import Path
import threading
import asyncio
import random




messages = {
    "english": {
        "welcome": "Welcome! How can I assist you today?",
        "error": "Oops! I didn't understand that command. Please try again.",
        "commands": "Here is the list of available commands:",
        "save_contact": "Save a contact with a name, address, phone number, email, and birthday to the contacts book",
        "search_contact": "Search for a contact among the contacts in the book",
        "show_contacts": "Show all existing contacts in the contacts book",
        "add_phone": "Add another phone to an existing contact",
        "delete_phone": "Delete an existing phone",
        "add_email": "Add another email to an existing contact",
        "delete_email": "Delete an existing email",
        "edit_phone": "Edit the phone of an existing contact",
        "edit_email": "Edit the email of an existing contact",
        "edit_birthday": "Edit the birthday of an existing contact",
        "delete_contact": "Delete an existing contact",
        "upcoming_birthdays": "Display a list of contacts whose birthday is within a specified number of days from the current date",
        "save_note": "Save a note with the author's name",
        "search_note": "Search for a note among existing notes",
        "show_notes": "Show all existing notes",
        "edit_note": "Edit an existing note",
        "delete_note": "Delete an existing note",
        "add_tags": "Add tags to an existing note",
        "edit_tags": "Edit the tags of an existing note",
        "delete_tags": "Delete tags from an existing note",
        "search_sort_notes": "Search and sort notes by tags",
        "sort_files": "Sort files in the specified folder by categories (images, documents, videos, etc.)",
        "add_extension": "Add an additional extension for sorting",
        "remove_extension": "Remove an extension from the sorting list",
        "exit_program": "Exit the program",
    },
    "russian": {
        "welcome": "Добро пожаловать! Чем я могу помочь вам сегодня?",
        "error": "Ой! Я не понял эту команду. Пожалуйста, попробуйте еще раз.",
        "commands": "Вот список доступных команд:",
        "save_contact": "Сохранить контакт с именем, адресом, номером телефона, электронной почтой и днем рождения в книге контактов",
        "search_contact": "Поиск контакта среди контактов в книге",
        "show_contacts": "Показать все существующие контакты в книге контактов",
        "add_phone": "Добавить еще один телефон к существующему контакту",
        "delete_phone": "Удалить существующий телефон",
        "add_email": "Добавить еще один адрес электронной почты к существующему контакту",
        "delete_email": "Удалить существующий адрес электронной почты",
        "edit_phone": "Редактировать телефон существующего контакта",
        "edit_email": "Редактировать адрес электронной почты существующего контакта",
        "edit_birthday": "Редактировать день рождения существующего контакта",
        "delete_contact": "Удалить существующий контакт",
        "upcoming_birthdays": "Показать список контактов, у которых день рождения через указанное количество дней от текущей даты",
        "save_note": "Сохранить заметку с именем автора",
        "search_note": "Поиск заметки среди существующих заметок",
        "show_notes": "Показать все существующие заметки",
        "edit_note": "Редактировать существующую заметку",
        "delete_note": "Удалить существующую заметку",
        "add_tags": "Добавить теги к существующей заметке",
        "edit_tags": "Редактировать теги существующей заметки",
        "delete_tags": "Удалить теги из существующей заметки",
        "search_sort_notes": "Поиск и сортировка заметок по тегам",
        "sort_files": "Сортировка файлов в указанной папке по категориям (изображения, документы, видео и т. д.)",
        "add_extension": "Добавить дополнительное расширение для сортировки",
        "remove_extension": "Удалить расширение из списка сортировки",
        "exit_program": "Выход из программы",
    },
}

COLOR_COMMAND_GREEN = "bg:#ansigreen #ffffff"
STYLE = Style.from_dict({"prompt": COLOR_COMMAND_GREEN})

HI_COMMANDS_RU = [
    "🎩✨Абракадабра! Введите волшебную команду:",
    "Скажите мне, что вы хотите сделать: ",
    "Жду вашу команду для начала работы: ",
    "Добро пожаловать в удивительный мир возможностей! Ожидаю вашей команды для начала.",
    "Добро пожаловать в мир возможностей! Ожидаю вашей волшебной команды.",
]



HI_COMMANDS = [
    "🎩✨Abracadabra! Enter the magic command:",
    "Let me know what you want to do: ",
    "Waiting for your command to start work: ",
    "Welcome to the amazing world of opportunities! Waiting for your command to start.",
    "Welcome to the world of opportunities! Waiting for your magic command.",
]


COMMAND_EXPLAIN_RU = WordCompleter(
    [
        "Команды",
        "добавление контакта",  # добавление контакта
        "поиск контакта",  # поиск контакта
        "показать все контакты",  # показать все контакты
        "добавить телефон к контакту",  # добавить телефон к контакту
        "удалить телефон у контакта",  # удалить телефон у контакта
        "добавить электронную почту к контакту",  # добавить электронную почту к контакту
        "удалить электронную почту у контакта",  # удалить электронную почту у контакта
        "редактировать телефон контакта",  # редактировать телефон контакта
        "редактировать электронную почту контакта",  # редактировать электронную почту контакта
        "редактировать день рождения контакта",  # редактировать день рождения контакта
        "удалить контакт",  # удалить контакт
        "показать дни рождения",  # показать дни рождения
        "добавить заметку",  # добавить заметку
        "найти заметку",  # найти заметку
        "показать все заметки",  # показать все заметки
        "редактировать заметку",  # редактировать заметку
        "удалить заметку",  # удалить заметку
        "добавить тег",  # добавить тег
        "редактировать тег",  # редактировать тег
        "удалить тег",  # удалить тег
        "найти и отсортировать по тегам",  # найти и отсортировать по тегам
        "сортировать файлы",  # сортировать файлы
        "добавить расширение для сортировки",  # добавить расширение для сортировки
        "удалить расширение из списка сортировки",  # удалить расширение из списка сортировки
        "выход",  # выход
    ]
)


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
        bcolors.ORANGE + "cli" + bcolors.RESET,
        bcolors.ORANGE + "contact-add" + bcolors.RESET,
        bcolors.ORANGE + "contact-find" + bcolors.RESET,
        bcolors.ORANGE + "contact-show-all" + bcolors.RESET,
        bcolors.ORANGE + "contact-phone-add" + bcolors.RESET,
        bcolors.ORANGE + "contact-phone-remove" + bcolors.RESET,
        bcolors.ORANGE + "contact-email-add" + bcolors.RESET,
        bcolors.ORANGE + "contact-email-remove" + bcolors.RESET,
        bcolors.ORANGE + "contact-phone-edit" + bcolors.RESET,
        bcolors.ORANGE + "contact-email-edit" + bcolors.RESET,
        bcolors.ORANGE + "contact-birthday-edit" + bcolors.RESET,
        bcolors.ORANGE + "contact-remove" + bcolors.RESET,
        bcolors.ORANGE + "display-birthdays" + bcolors.RESET,
        bcolors.ORANGE + "note-add" + bcolors.RESET,
        bcolors.ORANGE + "note-find" + bcolors.RESET,
        bcolors.ORANGE + "note-show-all" + bcolors.RESET,
        bcolors.ORANGE + "note-edit" + bcolors.RESET,
        bcolors.ORANGE + "note-remove" + bcolors.RESET,
        bcolors.ORANGE + "tag-add" + bcolors.RESET,
        bcolors.ORANGE + "tag-edit" + bcolors.RESET,
        bcolors.ORANGE + "tag-remove" + bcolors.RESET,
        bcolors.ORANGE + "tag-find-sort" + bcolors.RESET,
        bcolors.ORANGE + "file-sort" + bcolors.RESET,
        bcolors.ORANGE + "file-extension-add" + bcolors.RESET,
        bcolors.ORANGE + "file-extension-remove" + bcolors.RESET,
        bcolors.ORANGE + "quit" + bcolors.RESET,
        bcolors.ORANGE + "exit" + bcolors.RESET,
        bcolors.ORANGE + "q" + bcolors.RESET,
    ]

    command_explain = [
        bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
        bcolors.BLUE + "зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів" + bcolors.RESET,
        bcolors.BLUE + "здійснює пошук контакту серед контактів книги" + bcolors.RESET,
        bcolors.BLUE + "показує всі існуючі контакти в книзі контактів" + bcolors.RESET,
        bcolors.BLUE + "додати іще 1-ин phone до існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "видалення існуючого phone" + bcolors.RESET,
        bcolors.BLUE + "додати іще 1-ин email до існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "видалення існуючого email" + bcolors.RESET,
        bcolors.BLUE + "редагування phone існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "редагування email існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "редагування birthday існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "видалення існуючого контакту" + bcolors.RESET,
        bcolors.BLUE + "виводить список контактів, у яких день народження через задану кількість днів від поточної дати" + bcolors.RESET,
        bcolors.BLUE + "зберігає нотатку за іменем автора" + bcolors.RESET,
        bcolors.BLUE + "здійснює пошук нотатки серед існуючих нотатків" + bcolors.RESET,
        bcolors.BLUE + "показує всі існуючі нотатки" + bcolors.RESET,
        bcolors.BLUE + "редагування існуючої нотатки" + bcolors.RESET,
        bcolors.BLUE + "видалення існуючої нотатки" + bcolors.RESET,
        bcolors.BLUE + "додавання тегів до існуючої нотатки" + bcolors.RESET,
        bcolors.BLUE + "редагування тегів існуючої нотатки" + bcolors.RESET,
        bcolors.BLUE + "видалення тегів з існуючої нотатки" + bcolors.RESET,
        bcolors.BLUE + "пошук та сортування нотаток за тегами" + bcolors.RESET,
        bcolors.BLUE + "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)." + bcolors.RESET,
        bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
        bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
        bcolors.BLUE + "вихід з програми" + bcolors.RESET,
        bcolors.BLUE + "вихід з програми" + bcolors.RESET,
        bcolors.BLUE + "вихід з програми" + bcolors.RESET,
    ]

    return "".join(
        "|{:<10} - {:<20}|\n".format(command_list[item], command_explain[item])
        for item in range(len(command_list))
    )


async def get_input():
    global exit_flag
    try:
        session = PromptSession()
        result = await session.prompt_async(
            random.choice(HI_COMMANDS),
            completer=COMMAND_EXPLAIN,
            pre_run=pre_run,
            style=STYLE,
        )
        timer_thread.cancel()
        return result
    except KeyboardInterrupt:
        print("KeyBoard interrupt error, EXITING!\n")
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)
        exit_flag = True
        
    except RuntimeError:
        pass

def timer_function():
    print("\n:alarm_clock: Time's up! You didn't enter any command.")
    print("I'm offended, you're not using me, so I run the Awadakedabra command and I shut down you forever!")
    shutdown_with_countdown()


def wait_for_input(timeout=60, timeout2=300):
    loop = asyncio.get_event_loop()
    result = None
    global timer_thread

    async def wait_input():
        nonlocal result
        result = await get_input()
        

    timer_thread = threading.Timer(timeout2, timer_function)
    timer_thread.start()

    try:
        loop.run_until_complete(asyncio.wait_for(wait_input(), timeout=timeout))
    except asyncio.TimeoutError:
        print("\n:alarm_clock: You are here, I'm waiting for your command")
    
    return result


def main():
    global exit_flag
    global file_name
    global note_name
    global book
    global note
    exit_flag = False
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

    # print("Hello! My name is Bot Jul. How can I help you today?")
    # language = input("Please choose a language (english/russian): ")
    try:

        while 1:
            language = input("Please choose a language (english/russian): ")
            if language == "english":
                user_input = wait_for_input()
                print(messages[language]["welcome"])
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
                            "Oh! You seem to have introduced the wrong command. Please try again!",
                            "Oops! This is not like the right command. Let's try again",
                            "Error: The command is not recognized. Try again.",
                            "😮 Hmm, I don't understand this command. Let's try something else."
                        ]
                        print(random.choice(error_messages))
                        if exit_flag:
                            timer_thread.cancel()
                            break
                            
            else:
                user_input = prompt(
                    random.choice(HI_COMMANDS_RU),
                    completer=COMMAND_EXPLAIN_RU,
                    pre_run=pre_run,
                    style=STYLE,
                )
                if user_input == "cli":
                    print(available_commands())

                if user_input == "добавление контакта":
                    # 'сохраняет контакт с именем, адресом, номером телефона, email и днем рождения в книге контактов'
                    book.add_contacts()

                if user_input == "поиск контакта":
                    # 'осуществляет поиск контакта среди контактов книги'
                    book.search_contact()

                if user_input == "показать все контакты":
                    # "показывает все существующие контакты в книге контактов"
                    book.show_all_contacts()

                if user_input == "добавить телефон к контакту":
                    # "добавить еще 1-ин телефон к существующему контакту"
                    book.add_phone()

                if user_input == "удалить телефон у контакта":
                    # "удаление существующего телефона",
                    book.remove_phone()

                if user_input == "добавить email к контакту":
                    # "добавить еще 1-ин email к существующему контакту"
                    book.add_email()

                if user_input == "удалить email у контакта":
                    # "удаление существующего email",
                    book.remove_email()

                if user_input == "редактировать телефон контакта":
                    # "редактирование телефона существующего контакта"
                    book.edit_phone()

                if user_input == "редактировать email контакта":
                    # 'редактирование email существующего контакта'
                    book.edit_email()

                if user_input == "редактировать день рождения контакта":
                    # 'редактирование дня рождения существующего контакта'
                    book.edit_birthday()

                if user_input == "удалить контакт":
                    # "удаление существующего контакта"
                    book.del_contact()

                if user_input == "выводить список контактов, у которых день рождения через заданную кількість днів від поточної дати":
                    # "выводит список контактов, у которых день рождения через заданное количество дней от текущей даты"
                    book.show_contacts_birthdays()

                if user_input == "сохранить заметку с именем автора":
                    # "сохраняет заметку с именем автора",
                    note.add_new_note()

                if user_input == "поиск заметки":
                    # "осуществляет поиск заметки среди существующих заметок"
                    note.find_author()

                if user_input == "показать все заметки":
                    # "показывает все существующие заметки"
                    note.note_show_all()

                if user_input == "редактировать заметку":
                    # "редактирование существующей заметки"
                    note.note_edit()

                if user_input == "удалить заметку":
                    # "удаление существующей заметки"
                    note.note_remove()

                if user_input == "добавить тег к заметке":
                    #  "добавление тегов к существующей заметке"
                    note.tag_add()

                if user_input == "редактировать теги заметки":
                    #  "редактирование тегов существующей заметки"
                    note.tag_edit()

                if user_input == "удалить теги из заметки":
                    #  "удаление тегов из существующей заметки"
                    note.tag_remove()

                if user_input == "поиск и сортировка заметок по тегам":
                    #  "поиск и сортировка заметок по тегам"
                    note.tag_find_and_sort()

                if user_input == "сортировка файлов в указанной папке по категориям (изображения, документы, видео и т. д.)":
                    #  "сортировка файлов в указанной папке по категориям (изображения, документы, видео и т. д.)"
                    executing_command(user_input.lower())

                if user_input == "добавление дополнительного расширения для сортировки":
                    #  "добавление дополнительного расширения для сортировки"
                    executing_command(user_input.lower())

                if user_input == "удаление расширения из списка для сортировки":
                    #  "удаление расширения из списка для сортировки"
                    executing_command(user_input.lower())

                if user_input == "выход" | "завершение" | "q":
                    print("До свидания!\n")

                    serialization = AddressBook()
                    serialization.save_to_file(file_name, book)
                    note_serialization = NoteBook()
                    note_serialization.note_save_to_file(note_name, note)
                    break

                if not user_input:
                    error_messages = [
                        "Ой! Похоже, вы ввели неправильную команду. Пожалуйста, попробуйте снова!",
                        "Упс! Это не похоже на правильную команду. Давайте попробуем еще раз",
                        "Ошибка: Команда не распознана. Попробуйте еще раз.",
                        "😮 Хмм, я не понимаю эту команду. Давайте попробуем что-то еще.,"
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
    asyncio.run(main())
