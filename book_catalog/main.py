import tkinter as tk
import sqlite3

# Initialize the database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        UNIQUE(title, author)
    )
""")
conn.commit()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Book Catalog")
root.geometry("400x400")

main_label = tk.Label(root, text="My Library", font=("Helvetica", 14), fg="blue")
main_label.pack()

title_label = tk.Label(root, text="Enter Book Title:")
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

author_label = tk.Label(root, text="Enter Author:")
author_label.pack()

author_entry = tk.Entry(root)
author_entry.pack()

result_label = tk.Label(root, text="")
result_label.pack()

def check_book():
    title = title_entry.get()
    author = author_entry.get()
    cursor.execute("SELECT title, author FROM books WHERE title=? AND author=?", (title, author))
    book = cursor.fetchone()
    if book:
        result_label.config(text=f"{title} by {author} is in the library.")
    else:
        result_label.config(text=f"{title} by {author} is not in the library.")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    try:
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        result_label.config(text=f"{title} by {author} has been added to the library.")
    except sqlite3.IntegrityError:
        result_label.config(text=f"{title} by {author} is already in the library.")

def view_library():
    cursor.execute("SELECT title, author FROM books")
    books = cursor.fetchall()
    if books:
        result_label.config(text="Library Contents:\n")
        for book in books:
            result_label.config(text=result_label.cget("text") + f"\n- {book[0]} by {book[1]}")
    else:
        result_label.config(text="The library is empty.")

def quit_app():
    conn.close()
    root.destroy()

check_button = tk.Button(root, text="Check Book", fg= 'blue', command=check_book)
add_button = tk.Button(root, text="Add Book", fg='blue', command=add_book)
view_button = tk.Button(root, text="View Library", fg='blue', command=view_library)
quit_button = tk.Button(root, text="Quit",fg='blue', command=quit_app)

check_button.pack(pady=10)
add_button.pack(pady=10)
view_button.pack(pady=10)
quit_button.pack(pady=10)

root.mainloop()
