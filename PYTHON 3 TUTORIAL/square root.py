import tkinter as tk
import math

def calculate():
    num = float(entry.get())
    result.config(text=f"Square root: {math.sqrt(num):.2f}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Calculate", command=calculate).pack()
result = tk.Label(root, text="")
result.pack()
root.mainloop()
