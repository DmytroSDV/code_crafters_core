from CODE_CRAFTERS_CORE.RecordData import bcolors
from collections import UserDict
import pickle
from emoji import emojize
from tabulate import tabulate


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class AuthorName(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val and val[1].isalpha:
            self._value = val
        else:
            raise ValueError(
               bcolors.FAIL + "Invalid phone format! Must be not empty and started with the letter!😞" + bcolors.RESET
            )


class Note(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val:
            self._value = val
        else:
            raise ValueError(bcolors.FAIL + "Invalid note format! Must be not empty!😞" + bcolors.RESET)


class Tag(Field):
    def __init__(self, value):
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        if val:
            self._value = val
        else:
            raise ValueError(bcolors.FAIL + "Invalid note format! Must be not empty!😞" + bcolors.RESET)


class NoteRec:
    def __init__(self, name):
        self.name = AuthorName(name)
        self.tags = []
        self.note = ""

    def add_tag(self, tag):
        if str(Tag(tag)):
            self.tags.append(Tag(tag))

    def remove_tag(self, del_tag):
        for tag in self.tags:
            if tag.value == del_tag:
                self.tags.remove(tag)

    def edit_tag(self, exist_tag, new_tag):
        check_flag = False
        for ind, tag in enumerate(self.tags):
            if tag.value == exist_tag:
                self.tags[ind] = Tag(new_tag)
                check_flag = True
        if not check_flag:
            raise ValueError(bcolors.FAIL + "Such tag is missed in the list!😞" + bcolors.RESET)

    def add_note(self, note):
        if Note(note):
            self.note = Note(note)

    def edit_note(self, new_note):
        self.note = Note(new_note)

    def __str__(self):
        table = []
        headers = [
            emojize(f":id: {bcolors.BOLD} Auhtor {bcolors.RESET}", language="alias"),
            emojize(f":bust_in_silhouette: {bcolors.BOLD} Tags {bcolors.RESET}", language="alias"),
            emojize(f":notebook: {bcolors.BOLD} Note {bcolors.RESET}", language="alias"),
        ]


        table.append([
            emojize(f"🎯 '{self.name.value}'", language="alias"),
            emojize(f"👀 [{' | '.join(tag.value for tag in self.tags)}]", language="alias"),
            emojize(f"📝 '{self.note}'", language="alias"),
        ])


        return f"{tabulate(table, headers=headers, tablefmt='pretty')}"


class NoteBook(UserDict):
    def add_new_note(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                note_data = input(f"{bcolors.BOLD}Please type your note:✍️  {bcolors.RESET}")
                tag_data = input(f"{bcolors.BOLD}Please enter applicable tag:✍️  {bcolors.RESET}")

                note_rec = NoteRec(note_name)
                note_rec.add_note(note_data)
                note_rec.add_tag(tag_data)
                self.data[note_rec.name.value] = note_rec
                print(f"{bcolors.GREEN}New note successfully added!{bcolors.RESET}✅")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def find_author(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        print(self.data[note_name])
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def note_show_all(self):
        for key in self.data:
            print(self.data[key])
        if not self.data:
            print(f"{bcolors.WARNING}Note list is empty!😞{bcolors.RESET}")

    def note_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)

                new_note = input(f"{bcolors.BOLD}Please type new note:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_note(new_note)
                        print(f"{bcolors.GREEN}Note successfully updated!✅{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def note_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)

                temp_dict = self.data.copy()
                for key in temp_dict:
                    if key == note_name:
                        self.data.pop(note_name)
                        print(f"{bcolors.GREEN}Note successfully deleted✅!{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_add(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}Please type additional tag:✍️ {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].add_tag(additional_tag)
                        print(f"{bcolors.GREEN}Tag successfully added✅!{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RED}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)

                print(
                    f"{bcolors.UNDERLINE}Available tags in the note {bcolors.RESET}{note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}Please choose the tag that must be replaced: {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "Such tag does not exist!😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}Please type new tag:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_tag(old_tag, additional_tag)
                        print(f"{bcolors.GREEN}Tag successfully added!{bcolors.RESET}✅")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "Such note does not exist!😞" + bcolors.RESET)

                print(
                    f"{bcolors.UNDERLINE}Available tags in the note{bcolors.RESET} {note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}Please choose the tag that must be replaced:✍️  {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "Such tag does not exist!😞" + bcolors.RESET)

                for key in self.data:
                    if key == note_name:
                        self.data[note_name].remove_tag(old_tag)
                        print(f"{bcolors.GREEN}Tag successfully removed!{bcolors.RESET}✅")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}Exeption - {bcolors.RESET}{ex}\n{bcolors.WARNING}You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}Attempts ended, please try again later!😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_find_and_sort(self):
        tag_name = input(f"{bcolors.BOLD}Please enter tag name:✍️  {bcolors.RESET}")
        temp_list = []
        for key in self.data:
            for tag in self.data[key].tags:
                if tag.value == tag_name:
                    temp_list.append(self.data[key])
        if temp_list == []:
            print(f"{bcolors.WARNING}There are no notes with tag{bcolors.RESET} '{tag_name}' {bcolors.WARNING}in the notebook{bcolors.RESET}")
        else:
            for item in temp_list:
                print(item)


    def note_save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}Notes added to:{bcolors.RESET} {file_path}")

    def note_read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)
