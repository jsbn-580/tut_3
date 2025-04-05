import tkinter as tk
import math
from tkinter import messagebox

def calculate():
    try:
        num = int(entry.get())
        result.delete(0, tk.END)
        result.insert(0, str(math.sqrt(num)))
    except:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
result = tk.Entry(root)
result.pack()
tk.Button(root, text="Square Root", command=calculate).pack()
root.mainloop()
