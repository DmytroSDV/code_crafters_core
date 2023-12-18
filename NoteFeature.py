from collections import UserDict
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
        if val and val[1].isalpha:
            self._value = val
        else:
            raise ValueError(
                "Invalid phone format! Must be not empty and started with the letter!"
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
            raise ValueError("Invalid note format! Must be not empty!")


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
            raise ValueError("Invalid note format! Must be not empty!")


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
            raise ValueError("Such tag is missed in the list!")

    def add_note(self, note):
        if Note(note):
            self.note = Note(note)

    def edit_note(self, new_note):
        self.note = Note(new_note)

    def __str__(self):
        return f"Autor name: {self.name.value}, tags: {'; '.join(tag.value for tag in self.tags)}, note {self.note}."


class NoteBook(UserDict):
    def add_new_note(self):
        author_name = input("Please enter note name: ")
        note_data = input("Please type your note: ")
        tag_data = input("Please enter applicable tag: ")

        note_rec = NoteRec(author_name)
        note_rec.add_note(note_data)
        note_rec.add_tag(tag_data)

        self.data[note_rec.name.value] = note_rec
        print("New note successfully added!")

    def find_author(self):
        author_name = input("Please enter note name: ")
        for key in self.data:
            if key == author_name:
                print(self.data[author_name])

    def find_tag(self, name):
        for key in self.data:
            if key == name:
                return self.data[name]

    def delete(self, user):
        temp_dict = self.data.copy()
        for keys in temp_dict:
            if keys == user:
                self.data.pop(user)

    def note_save_to_file(self, file_path: str, data):
        with open(file_path, "wb") as file:
            pickle.dump(data, file)
            print(f"Notes added to: {file_path}")

    def note_read_from_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return pickle.load(file)
