import shutil
from pathlib import Path
from unidecode import unidecode
import re


class FileSorter:
    extensions_dict = {
        "Image": [".jpeg", ".png", ".jpg", ".svg"],
        "Video": [".avi", ".mp4", ".mov", ".mkv"],
        "Document": [
            ".doc",
            ".docx",
            ".txt",
            ".pdf",
            ".xlsx",
            ".pptx",
        ],
        "Audio": [".mp3", ".ogg", ".wav", ".amr"],
        "Archive": [".zip", ".gz", ".tar"],
    }

    def __init__(self, path_to_folder: str):
        self._path_to_folder = None
        self.path_to_folder = Path(path_to_folder)

    @property
    def path_to_folder(self):
        return self._path_to_folder

    @path_to_folder.setter
    def path_to_folder(self, folder_path):
        folder_path = Path(folder_path)
        if folder_path.exists() and folder_path.is_dir():
            self._path_to_folder = folder_path
        else:
            raise ValueError("No such folder exists!")

    def adding_new_exxtension(self, key_from_dict: str, extension: str):
        if (
            key_from_dict in FileSorter.extensions_dict.keys()
            and not extension in FileSorter.extensions_dict[key_from_dict]
        ):
            FileSorter.extensions_dict[key_from_dict].append(extension)
        else:
            if not key_from_dict in FileSorter.extensions_dict.keys():
                print(
                    f"Sorry but such '{key_from_dict}' does not exist in the available file types [Image, Video, Audio, Document, Archive]"
                )
            if (
                key_from_dict in FileSorter.extensions_dict.keys()
                and extension in FileSorter.extensions_dict[key_from_dict]
            ):
                print(
                    f"Sorry but extension '{extension}' does exist in the '{key_from_dict}' list.\nCurrent extensions in '{key_from_dict}': {FileSorter.extensions_dict[key_from_dict]}"
                )

    def removing_new_extension(self, key_from_dict: str, extension: str):
        if (
            key_from_dict in FileSorter.extensions_dict.keys()
            and extension in FileSorter.extensions_dict[key_from_dict]
        ):
            FileSorter.extensions_dict[key_from_dict].remove(extension)
        else:
            if not key_from_dict in FileSorter.extensions_dict.keys():
                print(
                    f"Sorry but such '{key_from_dict}' does not exist in the available file types [Image, Video, Audio, Document, Archive]"
                )
            if (
                key_from_dict in FileSorter.extensions_dict.keys()
                and not extension in FileSorter.extensions_dict[key_from_dict]
            ):
                print(
                    f"Sorry but extension '{extension}' does not exist in the '{key_from_dict}' list.\nCurrent extensions in '{key_from_dict}': {FileSorter.extensions_dict[key_from_dict]}"
                )

    def is_dir_empty(self, path_argv: Path) -> bool:
        for element in path_argv.iterdir():
            return False
        return True

    def normalize(self, path_argv: str) -> str:
        to_check_if_it_file = Path(path_argv)
        if to_check_if_it_file.suffix:
            extension_of_file = to_check_if_it_file.suffix
            path_argv = re.sub(extension_of_file, "", path_argv)
        new_name = unidecode(path_argv)
        new_name = "".join([item if item.isalnum() else "_" for item in new_name]) + (
            extension_of_file if to_check_if_it_file.suffix else ""
        )
        return new_name

    def trash_sorting(self):
        def trash_sorting_recursion(recursion_path: Path):
            for element in recursion_path.iterdir():
                if not element.name in (
                    "video",
                    "audio",
                    "images",
                    "documents",
                    "archives",
                ):
                    if element.is_dir():
                        it_dir = element.name
                        new_name = self.normalize(it_dir)
                        new_path = element.parent / new_name
                        try:
                            element = element.rename(new_path)
                        except Exception as e:
                            print(f"exeption - {e}")
                        trash_sorting_recursion(element)
                        if self.is_dir_empty(element):
                            element.rmdir()
                    else:
                        it_file = element.name
                        new_name = self.normalize(it_file)
                        new_path = element.with_name(new_name)
                        element = element.rename(new_path)

                        if (
                            element.suffix.lower()
                            in FileSorter.extensions_dict["Image"]
                        ):
                            destination_dir = self.path_to_folder / "images"
                            destination_dir.mkdir(exist_ok=True)
                            destination_dir = destination_dir / new_name
                            shutil.move(element, destination_dir)

                        elif (
                            element.suffix.lower()
                            in FileSorter.extensions_dict["Video"]
                        ):
                            destination_dir = self.path_to_folder / "video"
                            destination_dir.mkdir(exist_ok=True)
                            destination_dir = destination_dir / new_name
                            shutil.move(element, destination_dir)

                        elif (
                            element.suffix.lower()
                            in FileSorter.extensions_dict["Document"]
                        ):
                            destination_dir = self.path_to_folder / "documents"
                            destination_dir.mkdir(exist_ok=True)
                            destination_dir = destination_dir / new_name
                            shutil.move(element, destination_dir)
                        elif (
                            element.suffix.lower()
                            in FileSorter.extensions_dict["Audio"]
                        ):
                            destination_dir = self.path_to_folder / "audio"
                            destination_dir.mkdir(exist_ok=True)
                            destination_dir = destination_dir / new_name
                            shutil.move(element, destination_dir)
                        elif (
                            element.suffix.lower()
                            in FileSorter.extensions_dict["Archive"]
                        ):
                            destination_dir = self.path_to_folder / "archives"
                            destination_dir.mkdir(exist_ok=True)
                            get_suffix = element.suffix
                            get_folder_name = re.sub(get_suffix, "", element.name)
                            destination_dir = destination_dir / get_folder_name
                            destination_dir.mkdir(exist_ok=True)
                            shutil.unpack_archive(element, destination_dir)
                            
        return trash_sorting_recursion(self.path_to_folder)
