import tkinter as tk
from tkinter import messagebox
import math

def compute_square_root():
    try:
        num = int(entry.get())
        if num < 0:
            raise ValueError("Negative number")
        result = math.sqrt(num)
        output_label.config(text=f"Square root: {result:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a non-negative integer.")

root = tk.Tk()
root.title("Square Root Calculator")

tk.Label(root, text="Enter an integer:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Compute Square Root", command=compute_square_root).pack(pady=5)
output_label = tk.Label(root, text="")
output_label.pack(pady=5)

root.mainloop()
