#19.12.2023
#first release version 0.0.1

Hi this is command bot Jul developed by `Code Crafters` team. 
- User can choose language for visualization and understanding commands en | ru | ua.


All available commands that bot can do are:

Command prompt: cli
|cli        - виводить список всіх доступних команд|
|contact-add - зберігає контакт з іменем, адресом, номером телефона, email та днем народження до книги контактів|
|contact-find - здійснює пошук контакту серед контактів книги|
|contact-show-all - показує всі існуючі контакти в книзі контактів|       
|contact-phone-add - додати іще 1-ин phone до існуючого контакту|
|contact-phone-remove - видалення існуючого phone|
|contact-email-add - додати іще 1-ин email до існуючого контакту|
|contact-email-remove - видалення існуючого email|
|contact-phone-edit - редагування phone існуючого контакту|
|contact-email-edit - редагування email існуючого контакту|
|contact-birthday-edit - редагування birthday існуючого контакту|
|contact-remove - видалення існуючого контакту|
|display-birthdays - виводить список контактів, у яких день народження через задану кількість днів від поточної дати|
|note-add   - зберігає нотатку за іменем автора|
|note-find  - здійснює пошук нотатки серед існуючих нотатків|
|note-show-all - показує всі існуючі нотатки|
|note-edit  - редагування існуючої нотатки|
|note-remove - видалення існуючої нотатки|
|tag-add    - додавання тегів до існуючої нотатки|
|tag-edit   - редагування тегів існуючої нотатки|
|tag-remove - видалення тегів з існуючої нотатки|
|tag-find-sort - пошук та сортування нотаток за тегами|
|file-sort  - сортування файлів у зазначеній папці за категоріями (зображення, документи, відео та ін.).|
|file-extension-add - додавання додатково розширення для сортування|
|file-extension-remove - видалення розширення із списку для сортування|
|quit       - вихід з програми    |
|exit       - вихід з програми    |
|q          - вихід з програми    |

setup(
    name='CLI_BOT_CC23',
    version='0.0.1',
    description='Command bot that do operations with storing contacts and notes.',
    url='https://github.com/DmytroSDV/code_crafters_core.git',
    author='Code Crafters',
    author_email='code_crafters@python.ua',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License"],
    license='MIT',
    packages=find_namespace_packages(),
    data_files=[("CODE_CRAFTERS_CORE", ['CODE_CRAFTERS_CORE\database.bin', 'CODE_CRAFTERS_CORE\notebase.bin'])],
    include_package_data = True,
    install_requires=['emoji', 'tabulate', 'unidecode', 'prompt_toolkit'],
    entry_points={'console_scripts': ['codecrafters = CODE_CRAFTERS_CORE.main:main']}
)