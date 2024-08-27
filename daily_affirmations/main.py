import tkinter as tk
import requests
import tkinter.messagebox


def get_new_affirmation():
    try:
        response = requests.get("https://www.affirmations.dev/")
        affirmation = response.json()["affirmation"]
        affirmation_label.config(text=affirmation)
    except requests.exceptions.RequestException:
        tkinter.messagebox.showerror("Error", "Failed to load affirmation. Please check your internet connection.")


def copy_affirmation():
    affirmation = affirmation_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(affirmation)
    root.update()


root = tk.Tk()
root.title("Daily Affirmation Generator")
root.geometry("500x300")
root.configure(bg="#debfe3")
root.resizable(False, False)

affirmation_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), fg="#525052", bg="#debfe3", wraplength=400)
affirmation_label.place(relx=0.5, rely=0.4, anchor="center")

new_affirmation_btn = tk.Button(root, text="Get new affirmation", font=("Helvetica", 10), fg="#1e1b1f", bg="#969596",
                                activebackground="#969596", command=get_new_affirmation)
new_affirmation_btn.place(relx=0.3, rely=0.7, anchor="center")

copy_clipboard_btn = tk.Button(root, text="Copy to clipboard", font=("Helvetica", 10), fg="#1e1b1f", bg="#969596",
                               activebackground="#969596", command=copy_affirmation)
copy_clipboard_btn.place(relx=0.7, rely=0.7, anchor="center")

quit_btn = tk.Button(root, text="Quit", font=("Helvetica", 10), fg="#1e1b1f", bg="#969596",
                     activebackground="#969596", command=root.quit)
quit_btn.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()
