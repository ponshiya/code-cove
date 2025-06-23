import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

def divide():
    try:
        if float(entry2.get()) == 0:
            raise ZeroDivisionError
        result = float(entry1.get()) / float(entry2.get())
        result_label.config(text="Result: " + str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero!")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers!")

window = tk.Tk()
window.title("calculator")
window.geometry("300x250")

entry1 = tk.Entry(window)
entry1.pack(pady=5)

entry2 = tk.Entry(window)
entry2.pack(pady=5)

tk.Button(window, text="Add ➕", command=add).pack(pady=5)
tk.Button(window, text="Subtract ➖", command=subtract).pack(pady=5)
tk.Button(window, text="Multiply ✖", command=multiply).pack(pady=5)
tk.Button(window, text="Divide ➗", command=divide).pack(pady=5)

result_label = tk.Label(window, text="Result: ")
result_label.pack(pady=10)

window.mainloop()
