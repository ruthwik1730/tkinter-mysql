import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()


def add_user():
    name = entry_name.get()
    email = entry_email.get()
    if name and email:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        messagebox.showinfo("Success", "User added")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        view_users()
    else:
        messagebox.showwarning("Input error", "Please enter both name and email")

def view_users():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

def delete_user():
    try:
        selected = listbox.get(listbox.curselection())
        user_id = selected.split(',')[0].split(':')[1].strip()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        messagebox.showinfo("Deleted", "User deleted")
        view_users()
    except:
        messagebox.showwarning("Selection error", "Please select a user to delete")


root = tk.Tk()
root.title("User Manager")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Button(root, text="Add User", command=add_user).grid(row=2, column=0, columnspan=2, pady=5)

listbox = tk.Listbox(root, width=50)
listbox.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Refresh List", command=view_users).grid(row=4, column=0, pady=5)
tk.Button(root, text="Delete Selected", command=delete_user).grid(row=4, column=1, pady=5)


view_users()

root.mainloop()

