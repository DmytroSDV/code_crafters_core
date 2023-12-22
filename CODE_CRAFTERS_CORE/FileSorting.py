from CODE_CRAFTERS_CORE.RecordData import bcolors
from unidecode import unidecode
from pathlib import Path
import shutil
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
            raise ValueError(bcolors.FAIL + "❌ No such folder exists❗ 😞" + bcolors.RESET)

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
                            print(f"{bcolors.FAIL}❌ Exeption❗ - {bcolors.RESET}{e}")
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

def show_extension():
    img = FileSorter.extensions_dict["Image"]
    vid = FileSorter.extensions_dict["Video"]
    doc = FileSorter.extensions_dict["Document"]
    aud = FileSorter.extensions_dict["Audio"]
    arch = FileSorter.extensions_dict["Audio"]
    print(f"{bcolors.BLUE}Image: {bcolors.RESET}", f"{bcolors.WARNING} {img} {bcolors.RESET}")
    print(f"{bcolors.BLUE}Video: {bcolors.RESET}", f"{bcolors.WARNING} {vid} {bcolors.RESET}")
    print(f"{bcolors.BLUE}Document: {bcolors.RESET}", f"{bcolors.WARNING} {doc} {bcolors.RESET}")
    print(f"{bcolors.BLUE}Audio: {bcolors.RESET}", f"{bcolors.WARNING} {aud} {bcolors.RESET}")
    print(f"{bcolors.BLUE}Archive: {bcolors.RESET}", f"{bcolors.WARNING} {arch} {bcolors.RESET}")
    return ""


def adding_extension(key_from_dict: str, extension: str):
    if (
        key_from_dict in FileSorter.extensions_dict.keys()
        and not extension in FileSorter.extensions_dict[key_from_dict]
    ):
        FileSorter.extensions_dict[key_from_dict].append(extension)
    else:
        if not key_from_dict in FileSorter.extensions_dict.keys():
            raise ValueError(
                f"{bcolors.FAIL}😞 Sorry but such {bcolors.RESET}'{key_from_dict}'{bcolors.FAIL}❌ does not exist in the available file types❗  {bcolors.RESET}{bcolors.ORANGE}[Image, Video, Audio, Document, Archive]{bcolors.RESET}"
            )
        if (
            key_from_dict in FileSorter.extensions_dict.keys()
            and extension in FileSorter.extensions_dict[key_from_dict]
        ):
            raise ValueError(
                f"{bcolors.FAIL}'😞 Sorry but extension {bcolors.RESET}''{extension}'❌ {bcolors.FAIL}'does exist in the {bcolors.RESET}''{key_from_dict}' {bcolors.ORANGE}'❗ list.\nCurrent extensions in {bcolors.RESET}''{key_from_dict}': {FileSorter.extensions_dict[key_from_dict]}"
            )


def removing_extension(key_from_dict: str, extension: str):
    if (
        key_from_dict in FileSorter.extensions_dict.keys()
        and extension in FileSorter.extensions_dict[key_from_dict]
    ):
        FileSorter.extensions_dict[key_from_dict].remove(extension)
    else:
        if not key_from_dict in FileSorter.extensions_dict.keys():
            print(
                f"{bcolors.FAIL}'😞Sorry but such {bcolors.RESET}''{key_from_dict}'{bcolors.FAIL}'❌ does not exist in the available file types❗  '{bcolors.RESET}{bcolors.ORANGE}'[Image, Video, Audio, Document, Archive]{bcolors.RESET}'"
            )
        if (
            key_from_dict in FileSorter.extensions_dict.keys()
            and not extension in FileSorter.extensions_dict[key_from_dict]
        ):
            print(
                f"{bcolors.FAIL}'😞Sorry but extension '{bcolors.RESET}'{extension}'❌ {bcolors.FAIL}'does not exist in the '{bcolors.RESET}'{key_from_dict}' {bcolors.FAIL}❗ 'list.\nCurrent extensions in {bcolors.RESET}''{key_from_dict}': {FileSorter.extensions_dict[key_from_dict]}"
            )


def executing_command(responce_from_the_user: str):
    tries = 2
    if responce_from_the_user == "file-sort":
        while tries > 0:
            try:
                sorter = FileSorter(input(f"{bcolors.BOLD}📂 Please etter folder path:✍️  {bcolors.RESET}"))
                sorter.trash_sorting()
                print(f"{bcolors.GREEN}📂 Files are successfully sorted!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter folder path!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n{bcolors.RED}❌ Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    elif responce_from_the_user == "file-extension-add":
        while tries > 0:
            try:
                adding_extension(
                    input(
                        f"{bcolors.BOLD}📝 Please enter file type Image / Audio / Video / Document or Archive:✍️  {bcolors.RESET}"
                    ),
                    input(f"{bcolors.BOLD}📝 Please enter any extension in the format '.***':✍️  {bcolors.RESET}"),
                )
                print(f"{bcolors.GREEN}📂 New extension successfully added!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}\n{bcolors.WARNING}🔄 You have one more last try to enter file type!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n❌ {bcolors.RED}Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue

    elif responce_from_the_user == "file-extension-remove":
        while tries > 0:
            try:
                removing_extension(
                    input(
                        f"{bcolors.BOLD}📝 Please enter file type Image / Audio / Video / Document or Archive:✍️  {bcolors.RESET}"
                    ),
                    input(f"{bcolors.BOLD}📝 Please enter any extension in the format '.***':✍️  {bcolors.RESET}"),
                )
                print(f"{bcolors.GREEN}📝 Extension successfully removed!✅{bcolors.RESET}")
                break
            except Exception as ex:
                tries -= 1
                message = (
                    f"\n❌ {bcolors.FAIL}Exeption❗ - {bcolors.RESET}{ex}.\n{bcolors.WARNING}You have one more last try to enter file type!{bcolors.RESET}\n"
                    if tries > 0
                    else f"\n{ex}\n❌ {bcolors.RED}Attempts ended, please try again later❗ 😞{bcolors.RESET}\n"
                )
                print(message)
                continue
            
    elif responce_from_the_user == "file-extension-show" or responce_from_the_user == "показать все разширения" or responce_from_the_user == "показати всі розширення":
        show_extension()
                    
    
