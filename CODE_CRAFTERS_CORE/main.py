from CODE_CRAFTERS_CORE.AvadaKedavra import shutdown_with_countdown
from CODE_CRAFTERS_CORE.FileSorting import executing_command
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from CODE_CRAFTERS_CORE.RecordData import bcolors
from CODE_CRAFTERS_CORE.AddressBook import *
from CODE_CRAFTERS_CORE.NoteFeature import *
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from pathlib import Path
import threading
import asyncio
import random


COLOR_COMMAND_GREEN = "bg:#ansigreen #ffffff"
STYLE = Style.from_dict({"prompt": COLOR_COMMAND_GREEN})

HI_COMMANDS_RU = [
    "🎩✨ Абракадабра! Введите волшебную команду:✍️  ",
    "👋 Скажите мне, что вы хотите сделать:✍️  ",
    "👋 Привет! Чем я могу помочь? Введите команду:✍️  "
    "💫 Жду вашу команду для начала работы:✍️  ",
    "👋 Добро пожаловать в удивительный мир возможностей! Ожидаю вашей команды для начала:✍️  ",
    "🌈 Добро пожаловать в мир возможностей! Ожидаю вашей волшебной команды:✍️  ",
    "🌈 Доброго времени суток! Ожидаю вашей команды:✍️ ",
    "🌈 Привет! Какие чудеса сегодня?:✍️  ",
]

HI_COMMANDS_EN = [
    "🎩✨ Abracadabra! Enter the magic command:✍️  ",
    "👋 Let me know what you want to do:✍️  ",
    "🎩✨ Tell me what you want to do: ",
    "💫 Waiting for your command to start work:✍️  ",
    "👋 Welcome to the amazing world of opportunities! Waiting for your command to start:✍️  ",
    "🌈 Welcome to the world of opportunities! Waiting for your magic command:✍️  ",
    "🎩✨ Welcome to the magical world of possibilities! Enter the magic command:✍️ ",
    "👋 Hello! How can I help? Enter a command:✍️  ",
    "🌈 Good day! Waiting for your command:✍️  ",
    "💫 Greetings! Enter a command:✍️  ",
    "👋 Hello! What wonders do you seek today?:✍️  ",
]

HI_COMMANDS_UA = [
    "🎩✨ Абракадабра! Введіть магічну команду:✍️  ",
    "👋 Будьте добрі скажіть, що я маю зробити:✍️  ",
    "💫 Чекаю на ваші накази:✍️  ",
    "👋 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу команду для початку:✍️  ",
    "🌈 Вітаю Вас в чарівному світі можливостей! Чекаю на Вашу чарівну команду:✍️  ",
    "🎩✨ Абракадабра! Введіть чарівну команду:✍️  ",
    "🎩✨ Скажіть мені, що ви хочете зробити:✍️  ",
    "👋 Привіт! Як я можу допомогти? Введіть команду:✍️  ",
    "🌈 Доброго дня! Очікую вашої команди:✍️  ",
    "💫 Вітаю вас! Введіть команду:✍️  ",
    "🕰 Привіт! Які чудеса сьогодні?:✍️  ",
]

COMMAND_EXPLAIN_RU = WordCompleter(
    [
        "команды",
        "изменить язык",
        "добавление контакта",  # добавление контакта
        "поиск контакта",  # поиск контакта
        "показать все контакты",  # показать все контакты
        "добавить телефон",  # добавить телефон к контакту
        "удалить телефон",  # удалить телефон у контакта
        "добавить электронную почту",  # добавить электронную почту к контакту
        "удалить электронную почту",  # удалить электронную почту у контакта
        "редактировать телефон",  # редактировать телефон контакта
        "редактировать электронную почту",  # редактировать электронную почту контакта
        "редактировать день рождения",  # редактировать день рождения контакта
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
        "показать все разширения",  # сортировать файлы
        "добавить расширение",  # добавить расширение для сортировки
        "удалить расширение",  # удалить расширение из списка сортировки
        "выход",  # выход
    ]
)

COMMAND_EXPLAIN_EN = WordCompleter(
    [
        "cli",
        "change-language",
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
        "file-extension-show",
        "file-extension-add",
        "file-extension-remove",
        "quit",
        "exit",
        "q",
    ]
)

COMMAND_EXPLAIN_UA = WordCompleter(
    [
        "можливості",
        "зміти мову",
        "додати контакт",
        "пошук контакта",
        "показати всі контакти",
        "додати телефон",
        "видалити телефон",
        "додати електронну пошту",
        "видалити електронну пошту",
        "редагувати телефон",
        "редагувати електронну пошту",
        "редагувати день народження",
        "видалити контакт",
        "показати дні народження",
        "додати нотатку",
        "знайти нотатку",
        "показати всі нотатки",
        "редагувати нотатку",
        "видалити нотатку",
        "додати тег",
        "редагувати тег",
        "видалити тег",
        "знайти та сортувати по тегам",
        "відсортувати файли",
        "показати всі розширення",
        "додати розширення файла",
        "видалити розширення файла", 
        "до зустрічі",  
    ]
)

def pre_run():
    app = get_app()
    b = app.current_buffer
    if b.complete_state:
        b.complete_next()
    else:
        b.start_completion(select_first=False)

def one_command_vizualization(user_input, lists: tuple):
    if user_input:
        for com_list, ex_com in zip(lists[0], lists[1]):  
            if com_list.__contains__(user_input):
                return f"{com_list} {ex_com}"
    return ""

def available_commands(command = None):

    if language == 'en':
        command_list = [
            bcolors.ORANGE + "cli" + bcolors.RESET,
            bcolors.ORANGE + "change-language" + bcolors.RESET,
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
            bcolors.ORANGE + "file-extension-show" + bcolors.RESET,
            bcolors.ORANGE + "file-extension-add" + bcolors.RESET,
            bcolors.ORANGE + "file-extension-remove" + bcolors.RESET,
            bcolors.ORANGE + "quit" + bcolors.RESET,
            bcolors.ORANGE + "exit" + bcolors.RESET,
            bcolors.ORANGE + "q" + bcolors.RESET,
        ]

        command_explain = [
            bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
            bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
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
            bcolors.BLUE + "показати всі розширення" + bcolors.RESET,
            bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
            bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
            bcolors.BLUE + "вихід з програми" + bcolors.RESET,
        ]
        
    elif language == 'ru':
        command_list = [
            bcolors.ORANGE + "команды" + bcolors.RESET,
            bcolors.ORANGE + "изменить язык" + bcolors.RESET,
            bcolors.ORANGE + "добавление контакта" + bcolors.RESET,
            bcolors.ORANGE + "поиск контакта" + bcolors.RESET,
            bcolors.ORANGE + "показать все контакты" + bcolors.RESET,
            bcolors.ORANGE + "добавить телефон" + bcolors.RESET,
            bcolors.ORANGE + "удалить телефон" + bcolors.RESET,
            bcolors.ORANGE + "добавить электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "удалить электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "редактировать телефон" + bcolors.RESET,
            bcolors.ORANGE + "редактировать электронную почту" + bcolors.RESET,
            bcolors.ORANGE + "редактировать день рождения" + bcolors.RESET,
            bcolors.ORANGE + "удалить контакт" + bcolors.RESET,
            bcolors.ORANGE + "показать дни рождения" + bcolors.RESET,
            bcolors.ORANGE + "добавить заметку" + bcolors.RESET,
            bcolors.ORANGE + "найти заметку" + bcolors.RESET,
            bcolors.ORANGE + "показать все заметки" + bcolors.RESET,
            bcolors.ORANGE + "редактировать заметку" + bcolors.RESET,
            bcolors.ORANGE + "удалить заметку" + bcolors.RESET,
            bcolors.ORANGE + "добавить тег" + bcolors.RESET,
            bcolors.ORANGE + "редактировать тег" + bcolors.RESET,
            bcolors.ORANGE + "удалить тег" + bcolors.RESET,
            bcolors.ORANGE + "найти и отсортировать по тегам" + bcolors.RESET,
            bcolors.ORANGE + "сортировать файлы" + bcolors.RESET,
            bcolors.ORANGE + "показать все разширения" + bcolors.RESET,
            bcolors.ORANGE + "добавить расширение" + bcolors.RESET,
            bcolors.ORANGE + "удалить расширение" + bcolors.RESET,
            bcolors.ORANGE + "выход" + bcolors.RESET,
        ]

        command_explain = [
            bcolors.BLUE + "выводит все доступные команды" + bcolors.RESET,
            bcolors.BLUE + "изменение языка приложения" + bcolors.RESET,
            bcolors.BLUE + "сохраняет контакт с именем, адресом, номером телефона, электронной почтой и днем рождения в контактную книгу" + bcolors.RESET,
            bcolors.BLUE + "ищет контакт между контактами книги" + bcolors.RESET,
            bcolors.BLUE + "показывает все существующие контакты в контактной книге" + bcolors.RESET,
            bcolors.BLUE + "добавить еще 1-ин телефон к существующему контакту" + bcolors.RESET,
            bcolors.BLUE + "удаление существующего телефона" + bcolors.RESET,
            bcolors.BLUE + "добавить еще 1-ин email к существующему контакту" + bcolors.RESET,
            bcolors.BLUE + "удалять существующее письмо" + bcolors.RESET,
            bcolors.BLUE + "редактировать телефон действующего контактного лица" + bcolors.RESET,
            bcolors.BLUE + "редактирование электронной почты существующего контакта" + bcolors.RESET,
            bcolors.BLUE + "редактирование дня рождения существующего контакта" + bcolors.RESET,
            bcolors.BLUE + "удалять существующий контакт" + bcolors.RESET,
            bcolors.BLUE + "отображает список контактов, имеющих день рождения после указанного числа дней с текущей даты" + bcolors.RESET,
            bcolors.BLUE + "сохраняет примечание по имени автора" + bcolors.RESET,
            bcolors.BLUE + "поиск примечаний среди существующих примечаний" + bcolors.RESET,
            bcolors.BLUE + "показывает все существующие примечания" + bcolors.RESET,
            bcolors.BLUE + "редактирование существующей записки" + bcolors.RESET,
            bcolors.BLUE + "удаление существующего примечания" + bcolors.RESET,
            bcolors.BLUE + "добавление тегов в существующее примечание" + bcolors.RESET,
            bcolors.BLUE + "редактирование тегов для существующей заметки" + bcolors.RESET,
            bcolors.BLUE + "удаление тегов из существующей записи" + bcolors.RESET,
            bcolors.BLUE + "поиск и сортировка заметок по тегам" + bcolors.RESET,
            bcolors.BLUE + "Сортировать файлы в указанной папке по категориям (изображения, документы, видео и т.д.)." + bcolors.RESET,
            bcolors.BLUE + "показать все доступные расширения для сортировки." + bcolors.RESET,
            bcolors.BLUE + "добавление дополнительного расширения для сортировки" + bcolors.RESET,
            bcolors.BLUE + "удаление расширения из списка для сортировки" + bcolors.RESET,
            bcolors.BLUE + "виход" + bcolors.RESET,
        ]
        
    elif language == 'ua':
        command_list = [
            bcolors.ORANGE + "можливості" + bcolors.RESET,
            bcolors.ORANGE + "зміти мову" + bcolors.RESET,
            bcolors.ORANGE + "додати контакт" + bcolors.RESET,
            bcolors.ORANGE + "пошук контакта" + bcolors.RESET,
            bcolors.ORANGE + "показати всі контакти" + bcolors.RESET,
            bcolors.ORANGE + "додати телефон" + bcolors.RESET,
            bcolors.ORANGE + "видалити телефон" + bcolors.RESET,
            bcolors.ORANGE + "додати електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "видалити електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "редагувати телефон" + bcolors.RESET,
            bcolors.ORANGE + "редагувати електронну пошту" + bcolors.RESET,
            bcolors.ORANGE + "редагувати день народження" + bcolors.RESET,
            bcolors.ORANGE + "видалити контакт" + bcolors.RESET,
            bcolors.ORANGE + "показати дні народження" + bcolors.RESET,
            bcolors.ORANGE + "додати нотатку" + bcolors.RESET,
            bcolors.ORANGE + "знайти нотатку" + bcolors.RESET,
            bcolors.ORANGE + "показати всі нотатки" + bcolors.RESET,
            bcolors.ORANGE + "редагувати нотатку" + bcolors.RESET,
            bcolors.ORANGE + "видалити нотатку" + bcolors.RESET,
            bcolors.ORANGE + "додати тег" + bcolors.RESET,
            bcolors.ORANGE + "редагувати тег" + bcolors.RESET,
            bcolors.ORANGE + "видалити тег" + bcolors.RESET,
            bcolors.ORANGE + "знайти та сортувати по тегам" + bcolors.RESET,
            bcolors.ORANGE + "відсортувати файли" + bcolors.RESET,
            bcolors.ORANGE + "показати всі розширення" + bcolors.RESET,
            bcolors.ORANGE + "додати розширення файла" + bcolors.RESET,
            bcolors.ORANGE + "видалити розширення файла" + bcolors.RESET,
            bcolors.ORANGE + "до зустрічі" + bcolors.RESET,
        ]

        command_explain = [
            bcolors.BLUE + "виводить список всіх доступних команд" + bcolors.RESET,
            bcolors.BLUE + "змінити мову додатка" + bcolors.RESET,
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
            bcolors.BLUE + "показати всі наявні розширеннядля сортування" + bcolors.RESET,
            bcolors.BLUE + "додавання додатково розширення для сортування" + bcolors.RESET,
            bcolors.BLUE + "видалення розширення із списку для сортування" + bcolors.RESET,
            bcolors.BLUE + "бот іде відпочивати" + bcolors.RESET,
        ]

    if command:
        return (command_list, command_explain)

    return "".join(
        "|{:<10} - {:<20}|\n".format(command_list[item], command_explain[item])
        for item in range(len(command_list))
    )


async def get_input():
    global exit_flag
    if language == "ru":
        HI_COMMANDS = HI_COMMANDS_RU
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_RU
        print(f"{bcolors.PINK}🤖 Я здесь, чтобы сделать твой день немного ярче!\n🌞 Не стесняйтесь задавать вопросы или просто общаться. Вместе мы можем сделать этот день незабываемым! 🎉🎈{bcolors.RESET}")
    elif language == "en":
        HI_COMMANDS = HI_COMMANDS_EN
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_EN
        print(f"{bcolors.PINK}🤖 I'm here to make your day a little brighter!\n🌞 Feel free to ask questions or just communicate. Together we can make this day unforgettable!{bcolors.RESET}")
    elif language == "ua" :
        HI_COMMANDS = HI_COMMANDS_UA
        COMMAND_EXPLAIN = COMMAND_EXPLAIN_UA
        print(f"{bcolors.PINK}🤖 Я тут, щоб зробити ваш день трохи яскравішим!\n🌞 Не соромтеся задавати питання або просто спілкуватися. Разом ми можемо зробити цей день незабутнім!{bcolors.RESET}")   
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
        print(f"\n{bcolors.FAIL}❌ KeyBoard interrupt error, EXITING❗{bcolors.RESET}\n")
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)
        exit_flag = True
        
    except RuntimeError:
        pass


def timer_function():
    print(f"\n{bcolors.WARNING}⏰ Time's up! You didn't enter any command💀 {bcolors.RESET}")
    print(f"{bcolors.WARNING}😄 I'm offended, you're not using me, so I run the Awadakedabra command and I shut down you forever!💀 {bcolors.RESET}")
    shutdown_with_countdown()


def wait_for_input(timeout=120, timeout2=1000):
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
        print(f"{bcolors.ORANGE}\n⏰: You are here, I'm waiting for your command{bcolors.RESET}")
    
    return result


def main():
    global exit_flag
    global file_name
    global note_name
    global book
    global note
    global language
    exit_flag = False
    language_flag = False
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

    print(f"{bcolors.PINK}👋 Hello! My name is Bot Jul. Please choose the language and we will begin 🤖 {bcolors.RESET}")

    try:
        while 1:
            if not language_flag:
                language = input(f"{bcolors.BOLD}🏳️  Please choose a language (en/:ru:/ua): {bcolors.RESET}")
                language_flag = True
                if not language in ("en", "ru", 'ua'):
                    while 1:
                        print(f"{bcolors.BOLD}🙃  Wrong language format entered!\nPlease enter en | ru or ua to choose language:{bcolors.RESET}")
                        language = input(f"{bcolors.BOLD}🫠  Please choose a language (en/ru/ua): {bcolors.RESET}")
                        if language in ("en", "ru", 'ua'):
                            language_flag = True
                            break
                        
            user_input = wait_for_input()
            print(one_command_vizualization(user_input, available_commands(user_input)))
            match user_input:
                case "cli" | "команды" | "можливості":
                    print(available_commands())
                
                case "change-language" | "изменить язык" | "зміти мову":
                    language_flag = False

                case "contact-add" | "добавление контакта" | "додати контакт":
                    # 'зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів'
                    book.add_contacts()

                case "contact-find" | "поиск контакта" | "пошук контакта":
                    # 'здійснює пошук контакту серед контактів книги'
                    book.search_contact()

                case "contact-show-all" | "показать все контакты" | "показати всі контакти":
                    # "показує всі існуючі контакти в книзі контактів"
                    book.show_all_contacts()

                case "contact-phone-add" | "добавить телефон" | "додати телефон":
                    # "додати іще 1-ин phone до існуючого контакту"
                    book.add_phone()

                case "contact-phone-remove" | "удалить телефон" | "видалити телефон":
                    # "видалення існуючого phone",
                    book.remove_phone()

                case "contact-email-add" | "добавить электронную почту" | "додати електронну пошту":
                    # "додати іще 1-ин email до існуючого контакту"
                    book.add_email()

                case "contact-email-remove" | "удалить электронную почту" | "видалити електронну пошту":
                    # "видалення існуючого email",
                    book.remove_email()

                case "contact-phone-edit" | "редактировать телефон" | "редагувати телефон":
                    # "редагування phone існуючого контакту"
                    book.edit_phone()

                case "contact-email-edit" | "редактировать электронную почту" | "редагувати електронну пошту":
                    # 'редагування email існуючого контакту'
                    book.edit_email()

                case "contact-birthday-edit" | "редактировать день рождения" | "редагувати день народження":
                    # 'редагування birthday існуючого контакту'
                    book.edit_birthday()

                case "contact-remove" | "удалить контакт" | "видалити контакт":
                    # "видалення існуючого контакту"
                    book.del_contact()

                case "display-birthdays" | "показать дни рождения" | "показати дні народження":
                    # "виводить список контактів, у яких день народження через задану кількість днів від поточної дати"
                    book.show_contacts_birthdays()

                case "note-add" | "добавить заметку" | "додати нотатку":
                    # "зберігає нотатку за іменем автора",
                    note.add_new_note()

                case "note-find" | "найти заметку" | "знайти нотатку":
                    # "здійснює пошук нотатки серед існуючих нотатків"
                    note.find_author()

                case "note-show-all" | "показать все заметки" | "показати всі нотатки":
                    # "показує всі існуючі нотатки"
                    note.note_show_all()

                case "note-edit" | "редактировать заметку" | "редагувати нотатку":
                    # "редагування існуючої нотатки"
                    note.note_edit()

                case "note-remove" | "удалить заметку" | "видалити нотатку":
                    # "видалення існуючої нотатки"
                    note.note_remove()

                case "tag-add" | "добавить тег" | "додати тег":
                    #  "додавання тегів до існуючої нотатки"
                    note.tag_add()

                case "tag-edit" | "редактировать тег" | "редагувати тег":
                    #  "редагування тегів існуючої нотатки"
                    note.tag_edit()

                case "tag-remove" | "удалить теги из заметки" | "видалити тег":
                    #  "видалення тегів з існуючої нотатки"
                    note.tag_remove()

                case "tag-find-sort" | "найти и отсортировать по тегам" | "знайти та сортувати по тегам":
                    #  "пошук та сортування нотаток за тегами"
                    note.tag_find_and_sort()

                case "file-sort" | "сортировать файлы" | "відсортувати файли":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())
                
                case "file-extension-show" | "показать все разширения" | "показати всі розширення":
                    #  "сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.)."
                    executing_command(user_input.lower())

                case "file-extension-add" | "добавить расширение" | "додати розширення файла":
                    #  "додавання додатково розширення для сортування"
                    executing_command(user_input.lower())

                case "file-extension-remove" | "удалить расширение" | "видалити розширення файла":
                    #  "видалення розширення із списку для сортування"
                    executing_command(user_input.lower())

                case "quit" | "exit" | "q" | "выход" | "в" | "до зустрічі" | "д":
                    print("Good bye!\n")
                    serialization = AddressBook()
                    serialization.save_to_file(file_name, book)
                    note_serialization = NoteBook()
                    note_serialization.note_save_to_file(note_name, note)
                    break
                
                case _:
                    if language == "en":
                        error_messages = [
                            f"{bcolors.WARNING}😔 Oh! You seem to have introduced the wrong command. Please try again!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔 Oops! This is not like the right command. Let's try again😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😟 Error: The command is not recognized. Try again.😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😮 Hmm, I don't understand this command. Let's try something else.😔{bcolors.RESET}"
                        ]
                    elif language == "ru":
                        error_messages = [
                            f"{bcolors.WARNING}🙃 Ой! Похоже, вы ввели неправильную команду. Пожалуйста, попробуйте снова!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😟 Упс! Это не похоже на правильную команду. Давайте попробуем еще раз😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😯 Ошибка: Команда не распознана. Попробуйте еще раз.{bcolors.RESET}",
                            f"{bcolors.WARNING}😮 Хмм, я не понимаю эту команду. Давайте попробуем что-то еще.😔{bcolors.RESET}"
                        ]
                    elif language == "ua":
                        error_messages = [
                            f"{bcolors.WARNING}😔 Ой! Начебто Ви ввели хибну команду. Будь ласка спробуйте ыще раз!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😯 Упс! Це не схоже правельну команду. Давайте спробуэмо ыще раз!😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔 Помилка: Незрозумыла команда. Спробуйте іще раз.😔{bcolors.RESET}",
                            f"{bcolors.WARNING}😔😮 Хмм, я не розумію цю команду. давайте спробуємо щось інше!😔{bcolors.RESET}"
                        ]
                    
                    print(random.choice(error_messages))
                    if exit_flag:
                        timer_thread.cancel()
                        break
                            

    except Exception as ex:
        print(f"{bcolors.FAIL}\n❌ Unnexpected error!{bcolors.RESET}")
        print(ex)
        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)

    except KeyboardInterrupt:
        print(f"{bcolors.FAIL}\n❌ KeyBoard interrupt error, EXITING!\n{bcolors.RESET}")

        serialization = AddressBook()
        serialization.save_to_file(file_name, book)
        note_serialization = NoteBook()
        note_serialization.note_save_to_file(note_name, note)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{bcolors.BLUE}The script is interrupted by the user!{bcolors.RESET}")


