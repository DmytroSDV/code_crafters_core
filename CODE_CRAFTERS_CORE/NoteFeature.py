from CODE_CRAFTERS_CORE.RecordData import bcolors
from collections import UserDict
from tabulate import tabulate
from emoji import emojize
import pickle


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
        if val and val[0].isalpha:
            self._value = val
        else:
            raise ValueError(
               bcolors.FAIL + "❌ Invalid note format❗ Must be not empty and started with the letter❗ 😞" + bcolors.RESET
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
            raise ValueError(bcolors.FAIL + "❌ Invalid note format! Must be not empty❗ 😞" + bcolors.RESET)


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
            raise ValueError(bcolors.FAIL + "❌ Invalid note format! Must be not empty❗ 😞" + bcolors.RESET)


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
            raise ValueError(bcolors.FAIL + "❌ Such tag is missed in the list❗ 😞" + bcolors.RESET)

    def add_note(self, note):
        if Note(note):
            self.note = Note(note)

    def edit_note(self, new_note):
        self.note = Note(new_note)


class NoteBook(UserDict):
	
    def responce_visualization(func):
        def inner(self, *args, **kwargs):

            result = func(self, *args, **kwargs)
            if isinstance(result, dict):
                print(f" {bcolors.BOLD}😊 All notes in the notebook!📝 {bcolors.RESET}")
                table = []
                headers = [
                    emojize(":id: Author", language="alias"),
                    emojize(":bust_in_silhouette: Tags", language="alias"),
                    emojize(":notebook: Note", language="alias"),
                ]

                for note_name in result.values():

                    table.append([
                        emojize(f"🎅 '{note_name.name.value}'"
                                , language="alias"),
                        emojize(
                            f"🔥 [{' | '.join(tag.value for tag in note_name.tags)}]", language="alias"),
                        emojize(f"💼 '{note_name.note}'", language="alias"),
                    ])

                print(bcolors.B + tabulate(table, headers=headers,
                                           tablefmt='pretty') + bcolors.RESET)

        return inner
	
    def add_new_note(self):
        tries = 2
        one_flag=False
        two_flag=False
        three_flag=False
        while True:
            try:
                if not one_flag:
                    while True:
                        note_name = input(f"{bcolors.BOLD}📝 Please enter Author name:✍️  {bcolors.RESET}")
                        if note_name in ['q', 'back', 'exit', 'quit']:
                            return
                        try:
                            note_rec = NoteRec(note_name)
                            one_flag=True
                            break
                        except ValueError as error:
                            print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                            print(f"{bcolors.WARNING}📝 Please enter Author name again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")
                    if not two_flag:
                        while True:
                            note_data = input(f"{bcolors.BOLD}📝 Please type your note:✍️  {bcolors.RESET}")
                            if note_data in ['q', 'back', 'exit', 'quit']:
                                return
                            try:
                                note_rec.add_note(note_data)
                                two_flag=True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}📝 Please type your note again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")
                    if not three_flag:
                        while True:
                            tag_data = input(f"{bcolors.BOLD}📝 Please enter applicable tag:✍️  {bcolors.RESET}")
                            if tag_data in ['q', 'back', 'exit', 'quit']:
                                return
                            try:
                                note_rec.add_tag(tag_data)

                                three_flag=True
                                break
                            except ValueError as error:
                                print(f"{bcolors.FAIL}❌ Error❗ - {bcolors.RESET}{error}")
                                print(f"{bcolors.WARNING}📝 Please enter applicable tag again or command ['q', 'back', 'exit', quit] for exit menu:✍️  {bcolors.RESET}")

                self.data[note_rec.name.value] = note_rec
                print(f"{bcolors.GREEN}📋 New note successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    @responce_visualization
    def find_author(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        return {self.data[note_name].name: self.data[note_name]}
                if not note_name in self.data:
                    raise ValueError(
                        bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    @responce_visualization
    def note_show_all(self):
        if self.data:
            return self.data

        if not self.data:
            print(f"{bcolors.WARNING}❌ Note list is empty❗ 😞{bcolors.RESET}")
            print(f"{bcolors.GREEN}🏷️  But, you can add a note if you want ✏️ {bcolors.RESET}")

    def note_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                new_note = input(f"{bcolors.BOLD}📝 Please type new note:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_note(new_note)
                        print(f"{bcolors.GREEN}📋 Note successfully updated!✅{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def note_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                temp_dict = self.data.copy()
                for key in temp_dict:
                    if key == note_name:
                        self.data.pop(note_name)
                        print(f"{bcolors.GREEN}📋 Note successfully deleted✅!{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_add(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}📝 Please type additional tag:✍️ {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].add_tag(additional_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully added✅!{bcolors.RESET}")
                break

            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RED}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_edit(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                print(
                    f"{bcolors.BOLD}📝 Available tags in the note 📝 {bcolors.RESET}{note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}📝 Please choose the tag that must be replaced:✍️  {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "❌ Such tag does not exist❗ 😞" + bcolors.RESET)

                additional_tag = input(f"{bcolors.BOLD}📝 Please type new tag:✍️  {bcolors.RESET}")
                for key in self.data:
                    if key == note_name:
                        self.data[note_name].edit_tag(old_tag, additional_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    def tag_remove(self):
        tries = 2
        while tries > 0:
            try:
                note_name = input(f"{bcolors.BOLD}🔍 Please enter note name:✍️  {bcolors.RESET}")
                if not note_name in self.data:
                    raise ValueError(bcolors.FAIL + "❌ Such note does not exist❗ 😞" + bcolors.RESET)

                print(
                    f"{bcolors.BOLD}🏷️  Available tags in the note 📝{bcolors.RESET} {note_name} - ",
                    " | ".join(tag.value for tag in self.data[note_name].tags),
                )
                old_tag = input(f"{bcolors.BOLD}📝 Please choose the tag that must be replaced:✍️  {bcolors.RESET}")

                check_tag = any(
                    tag.value == old_tag for tag in self.data[note_name].tags
                )
                if not check_tag:
                    raise ValueError(bcolors.FAIL + "❌ Such tag does not exist❗ 😞" + bcolors.RESET)

                for key in self.data:
                    if key == note_name:
                        self.data[note_name].remove_tag(old_tag)
                        print(f"{bcolors.GREEN}📋 Tag successfully removed!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter data!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    @responce_visualization
    def tag_find_and_sort(self):
        tag_name = input(f"{bcolors.BOLD}🔍 Please enter tag name:✍️  {bcolors.RESET}")
        match_dict = {}
        similar_dict = {}
        for key in self.data:
            for tag in self.data[key].tags:
                if tag.value == tag_name:
                    match_dict[self.data[key].name] = self.data[key]
                if tag_name in tag.value:
                    similar_dict[self.data[key].name] = self.data[key]
        if match_dict:
            print(f"{bcolors.GREEN}📋 We have a 100% match!✅{bcolors.RESET}")
            return match_dict
        elif not match_dict and similar_dict:
            print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, but I found some similarity❗ 🔄{bcolors.RESET}")
            return similar_dict
        elif not match_dict and not similar_dict:
            suggested_dict = {}
            for key in self.data:
                if self.data[key].note.value.__contains__(tag_name):   
                    suggested_dict[self.data[key].name] = self.data[key]
            if suggested_dict:
                print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, but I found some similarity in note body❗ 🔄{bcolors.RESET}")
                return suggested_dict
            else:
                return print(f"{bcolors.WARNING}❌ There are no notes with exact tag 📋 {bcolors.RESET}{bcolors.UNDERLINE}'{tag_name}'{bcolors.RESET}{bcolors.WARNING} in the notebook, as well as any similarity..😞{bcolors.RESET}")
            

    def note_save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"{bcolors.GREEN}💾 Notes added to:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            

    def note_read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            print(f"{bcolors.GREEN}📖 Reading notes from:{bcolors.RESET} 📂 {bcolors.UNDERLINE}{file_path}{bcolors.RESET}✅")
            return pickle.load(file)
