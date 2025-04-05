import tkinter as tk

def convert():
    result.delete(0, tk.END)
    result.insert(0, text.get().upper())

root = tk.Tk()
text = tk.Entry(root)
text.pack()
result = tk.Entry(root)
result.pack()
tk.Button(root, text="To Uppercase", command=convert).pack()
root.mainloop()
