from tkinter import Label, messagebox
import tkinter as tk
import subprocess
import threading


def shutdown_with_countdown():

    def force_avada():
        print("Good Bye!")
        # subprocess.run(["shutdown", "/s", "/t", "3"])

    def on_closing():
        background_thread = threading.Thread(target=force_avada)
        background_thread.daemon = True
        background_thread.start()
        messagebox.showwarning(
            "Error", "You cant interrupt Avada Kedavra!\nAnd thats why i will do it emmediately!\n5 seconds left until the completion of the spell - Good Bye!")
        # subprocess.run(["shutdown", "/s", "/t", "5"])

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

    for sec in range(15, 0, -1):
        try:
            label.config(
                text=f"{sec} seconds left until Avada Kedavra completion!")
        except Exception as ex:
            pass
        window.update()
        window.after(1000)

    window.destroy()
    # subprocess.run(["shutdown", "/s", "/t", "5"])

