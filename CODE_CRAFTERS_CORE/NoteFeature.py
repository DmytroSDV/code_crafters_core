from collections import UserDict
import pickle
from emoji import emojize
from tabulate import tabulate
from RecordData import bcolors
from CODE_CRAFTERS_CORE.AddressBook import bcolors

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
               bcolors.RED + "Invalid phone format! Must be not empty and started with the letter!" + bcolors.RESET
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
            raise ValueError(bcolors.RED + "Invalid note format! Must be not empty!" + bcolors.RESET)


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
            raise ValueError(bcolors.RED + "Invalid note format! Must be not empty!" + bcolors.RESET)


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
            raise ValueError(bcolors.RED + "Such tag is missed in the list!" + bcolors.RESET)

    def add_note(self, note):
        if Note(note):
            self.note = Note(note)

    def edit_note(self, new_note):
        self.note = Note(new_note)

    def __str__(self):
        table = []
        headers = [
            emojize(":id: Auhtor", language="alias"),
            emojize(":bust_in_silhouette: Tags", language="alias"),
            emojize(":notebook: Note", language="alias"),
        ]


        table.append([
            emojize(f"🎯 '{self.name.value}'", language="alias"),
            emojize(f"👀 [{' | '.join(tag.value for tag in self.tags)}]", language="alias"),
            emojize(f"📝 '{self.note}'", language="alias"),
        ])


        return f"{bcolors.P + tabulate(table, headers=headers, tablefmt='pretty') + bcolors.EN}"


class NoteBook(UserDict):
    def add_new_note(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                note_data = input("Please type your note: ")
                tag_data = input("Please enter applicable tag: ")

                note_rec = NoteRec(note_name)
                note_rec.add_note(note_data)
                note_rec.add_tag(tag_data)
                self.data[note_rec.name.value] = note_rec
                print("New note successfully added!")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def find_author(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                for key in self.data:
                    if key == note_name:
                        print(self.data[note_name])
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def note_show_all(self):
        for key in self.data:
            print(self.data[key])
        if not self.data:
            print("Note list is empty!")

    def note_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)

                new_note = input("Please type new note: ")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_note(new_note)
                        print("Note successfully updated!")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def note_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)

                temp_dict = self.data.copy()
                for key in temp_dict:
                    if key == note_name:
                        self.data.pop(note_name)
                        print("Note successfully deleted!")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def tag_add(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)

                additional_tag = input("Please type additional tag: ")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].add_tag(additional_tag)
                        print("Tag successfully added!")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def tag_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)

                print(
                    f"Available tags in the note {note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input("Please choose the tag that must be replaced: ")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.RED + "Such tag does not exist!" + bcolors.RESET)

                additional_tag = input("Please type new tag: ")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_tag(old_tag, additional_tag)
                        print("Tag successfully added!")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def tag_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input("Please enter note name: ")
                if not note_name in self.data:
                    raise ValueError(bcolors.RED + "Such note does not exist!" + bcolors.RESET)

                print(
                    f"Available tags in the note {note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input("Please choose the tag that must be replaced: ")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.RED + "Such tag does not exist!" + bcolors.RESET)

                for key in self.data:
                    if key == note_name:
                        self.data[note_name].remove_tag(old_tag)
                        print("Tag successfully removed!")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\nExeption - {ex}.\nYou have one more last try to enter data!\n"
                    if tries > 0
                    else f"\n{ex}\nAttempts ended, please try again later!\n"
                )
                print(message)
                continue

    def tag_find_and_sort(self):
        tag_name = input("Please enter tag name: ")
        temp_list = []
        for key in self.data:
            for tag in self.data[key].tags:
                if tag.value == tag_name:
                    temp_list.append(self.data[key])
        if temp_list == []:
            print(f"There are no notes with tag '{tag_name}' in the notebook")
        else:
            for item in temp_list:
                print(item)


    def note_save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"Notes added to: {file_path}")

    def note_read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)
